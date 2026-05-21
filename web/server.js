import express from 'express'
import path from 'path'
import fs from 'fs'
import { spawn } from 'child_process'
import { fileURLToPath } from 'url'
import { randomBytes } from 'crypto'

const __dirname = path.dirname(fileURLToPath(import.meta.url))
const REPO_ROOT = path.join(__dirname, '..')
const CHAPTERS_DIR = path.join(REPO_ROOT, 'chapters')
const AUDIO_DIR = path.join(REPO_ROOT, 'build', 'output', 'audiobook')
const DIST_DIR = path.join(__dirname, 'dist')
const LOG_DIR = path.join(AUDIO_DIR, '_logs')
const PORT = parseInt(process.env.PORT || '3080', 10)

const app = express()
app.use(express.json())

// ── Render-defaults: manifest + CHAPTER_PRESET_MAP ───────────────────────────

// Parse CHAPTER_PRESET_MAP straight from the Python source - no import needed.
function loadChapterPresetMap() {
  try {
    const src = fs.readFileSync(path.join(REPO_ROOT, 'build', 'audiobook.py'), 'utf8')
    const block = src.match(/CHAPTER_PRESET_MAP[^=]*=\s*\{([\s\S]*?)\n\}/)
    if (!block) return {}
    const map = {}
    const re = /^\s*"([^"]+)"\s*:\s*"([^"]+)"/gm
    let m
    while ((m = re.exec(block[1])) !== null) map[m[1]] = m[2]
    return map
  } catch { return {} }
}

// Build a slug → settings map from the rendered manifest.
function loadManifest() {
  const p = path.join(AUDIO_DIR, 'manifest.json')
  if (!fs.existsSync(p)) return {}
  try {
    const { chapters = [] } = JSON.parse(fs.readFileSync(p, 'utf8'))
    const out = {}
    for (const ch of chapters) {
      const slug = path.basename(ch.source || '', '.md')
      if (!slug) continue
      out[slug] = {
        engine:       ch.engine       ?? 'kokoro',
        preset:       ch.preset       ?? 'male',
        voice:        ch.voice        ?? '',
        speed:        ch.speed        ?? null,
        exaggeration: ch.exaggeration ?? null,
        cfg_weight:   ch.cfg_weight   ?? null,
        temperature:  ch.temperature  ?? null,
        per_sentence: ch.mode === 'sentence',
      }
    }
    return out
  } catch { return {} }
}

// Read TTS-* TXXX frames from an MP3's ID3 header.
// Reads only the ID3 section (first N bytes) - never the full audio body.
function readMp3TtsTags(mp3Path) {
  try {
    // Read just the 10-byte ID3 header to get the declared tag size
    const hdrBuf = Buffer.alloc(10)
    const fd = fs.openSync(mp3Path, 'r')
    const bytesRead = fs.readSync(fd, hdrBuf, 0, 10, 0)
    if (bytesRead < 10 || hdrBuf.slice(0, 3).toString() !== 'ID3') {
      fs.closeSync(fd); return null
    }
    const id3Size = ((hdrBuf[6] & 0x7f) << 21) | ((hdrBuf[7] & 0x7f) << 14) |
                    ((hdrBuf[8] & 0x7f) << 7)   |  (hdrBuf[9] & 0x7f)
    const frameBuf = Buffer.alloc(id3Size)
    fs.readSync(fd, frameBuf, 0, id3Size, 10)
    fs.closeSync(fd)

    const tags = {}
    let pos = 0
    while (pos < id3Size - 10) {
      const frameId = frameBuf.slice(pos, pos + 4).toString('ascii')
      if (frameId === '\x00\x00\x00\x00') break
      const frameSize = frameBuf.readUInt32BE(pos + 4)
      if (frameSize <= 0 || pos + 10 + frameSize > id3Size) break
      if (frameId === 'TXXX') {
        const payload = frameBuf.slice(pos + 10, pos + 10 + frameSize)
        const text = payload.slice(1).toString('utf8').replace(/\x00+$/, '')
        const sep = text.indexOf('\x00')
        if (sep > 0) tags[text.slice(0, sep)] = text.slice(sep + 1)
      }
      pos += 10 + frameSize
    }
    if (!tags['TTS-Engine']) return null
    return {
      engine:       tags['TTS-Engine'],
      preset:       tags['TTS-Preset']       || null,
      voice:        tags['TTS-Voice']        || null,
      speed:        tags['TTS-Speed']        != null ? parseFloat(tags['TTS-Speed'])        : null,
      per_sentence: tags['TTS-Mode'] === 'sentence',
      exaggeration: tags['TTS-Exaggeration'] != null ? parseFloat(tags['TTS-Exaggeration']) : null,
      cfg_weight:   tags['TTS-CfgWeight']    != null ? parseFloat(tags['TTS-CfgWeight'])    : null,
      temperature:  tags['TTS-Temperature']  != null ? parseFloat(tags['TTS-Temperature'])  : null,
    }
  } catch { return null }
}

// Build a filename-without-extension → TTS-tag map by scanning all MP3s in the audio dir.
// Keyed by full filename-without-.mp3 (e.g. 'ch01-departure', 'ch01-departure--ciufi-galeazzi').
// Cached in mp3TagDefaults; refreshed whenever a new MP3 lands.
function loadMp3Tags() {
  const out = {}
  for (const vol of ['vol-1', 'vol-2']) {
    const dir = path.join(AUDIO_DIR, vol)
    if (!fs.existsSync(dir)) continue
    for (const f of fs.readdirSync(dir)) {
      if (!f.endsWith('.mp3')) continue
      const key = f.replace(/\.mp3$/, '')
      const tags = readMp3TtsTags(path.join(dir, f))
      if (tags) out[key] = tags
    }
  }
  return out
}

// Per-chapter sidecar: build/output/audiobook/{vol}/{slug}.meta.json
// Written by the web UI on every successful generation; takes priority over manifest.
function loadSidecars() {
  const out = {}
  for (const vol of ['vol-1', 'vol-2']) {
    const dir = path.join(AUDIO_DIR, vol)
    if (!fs.existsSync(dir)) continue
    for (const f of fs.readdirSync(dir)) {
      if (!f.endsWith('.meta.json')) continue
      try {
        const slug = f.replace('.meta.json', '')
        out[slug] = JSON.parse(fs.readFileSync(path.join(dir, f), 'utf8'))
      } catch {}
    }
  }
  return out
}

function writeSidecar(audioPath, meta) {
  const sidecarPath = audioPath.replace(/\.mp3$/, '.meta.json')
  try {
    fs.writeFileSync(sidecarPath, JSON.stringify(meta, null, 2))
  } catch (e) {
    console.error('[sidecar] write failed:', sidecarPath, e.message)
  }
}

let chapterPresetMap = loadChapterPresetMap()
let manifestDefaults = loadManifest()
let sidecarDefaults  = loadSidecars()
let mp3TagDefaults   = loadMp3Tags()

// ── Chapter catalog ──────────────────────────────────────────────────────────

const VOL1_SECTIONS = [
  { dir: 'front-matter',                   label: 'Front Matter',            group: 'front-matter' },
  { dir: 'part-1-thesis-and-pain',         label: 'Part 1 - Thesis & Pain',  group: 'part-1' },
  { dir: 'part-2-council-reads-the-paper', label: 'Part 2 - Council Review', group: 'part-2' },
  { dir: 'part-3-reference-architecture',  label: 'Part 3 - Reference Arch', group: 'part-3' },
  { dir: 'part-4-implementation-playbooks',label: 'Part 4 - Playbooks',      group: 'part-4' },
  { dir: 'part-5-operational-concerns',    label: 'Part 5 - Operations',     group: 'part-5' },
  { dir: 'closing',                        label: 'Closing',                 group: 'closing' },
  { dir: 'epilogue',                       label: 'Epilogue',                group: 'epilogue' },
  { dir: 'appendices',                     label: 'Appendices',              group: 'appendices' },
]

const VOL2_SECTIONS = [
  { dir: 'book-2/act-1', label: 'Act 1 - Sealed Hull', group: 'act-1' },
  { dir: 'book-2/act-2', label: 'Act 2 - Under Ice',   group: 'act-2' },
  { dir: 'book-2/act-3', label: 'Act 3 - Ascent',      group: 'act-3' },
]

function extractTitle(stem, filePath) {
  try {
    const content = fs.readFileSync(filePath, 'utf8')
    const yamlMatch = content.match(/^---\n([\s\S]*?)\n---/)
    if (yamlMatch) {
      const titleLine = yamlMatch[1].match(/^title:\s*["']?(.+?)["']?\s*$/m)
      if (titleLine) return titleLine[1].trim()
    }
    const headingMatch = content.match(/^# (.+)$/m)
    if (headingMatch) return headingMatch[1].replace(/<!--.*?-->/g, '').trim()
  } catch {}

  return stem
    .replace(/^ch(\d+)-/, 'Ch $1: ')
    .replace(/^appendix-([a-z])-/, (_, l) => `Appendix ${l.toUpperCase()}: `)
    .replace(/-/g, ' ')
    .replace(/\b\w/g, l => l.toUpperCase())
}

function buildCatalog() {
  const chapters = []

  // Pre-scan each vol dir once for efficiency
  const volFiles = {}
  for (const vol of ['vol-1', 'vol-2']) {
    const dir = path.join(AUDIO_DIR, vol)
    volFiles[vol] = fs.existsSync(dir) ? fs.readdirSync(dir) : []
  }

  for (const section of VOL1_SECTIONS) {
    const sectionDir = path.join(CHAPTERS_DIR, section.dir)
    if (!fs.existsSync(sectionDir)) continue
    for (const file of fs.readdirSync(sectionDir).filter(f => f.endsWith('.md')).sort()) {
      const stem = file.replace('.md', '')
      const audioPath = path.join(AUDIO_DIR, 'vol-1', `${stem}.mp3`)
      // Find all audio variants: files matching {stem}*.mp3 but not temp files containing '__'
      const audioFiles = volFiles['vol-1'].filter(f =>
        f.endsWith('.mp3') && f.startsWith(stem) && !f.includes('__')
      )
      chapters.push({
        id: `vol1-${stem}`,
        slug: stem,
        volume: 'vol-1',
        section: section.group,
        section_label: section.label,
        source_path: path.join('chapters', section.dir, file),
        audio_path: audioPath,
        audio_files: audioFiles,
        has_audio: audioFiles.length > 0,
        title: extractTitle(stem, path.join(sectionDir, file)),
      })
    }
  }

  for (const section of VOL2_SECTIONS) {
    const sectionDir = path.join(CHAPTERS_DIR, section.dir)
    if (!fs.existsSync(sectionDir)) continue
    for (const file of fs.readdirSync(sectionDir).filter(f => f.endsWith('.md')).sort()) {
      const stem = file.replace('.md', '')
      const audioPath = path.join(AUDIO_DIR, 'vol-2', `${stem}.mp3`)
      // Find all audio variants: files matching {stem}*.mp3 but not temp files containing '__'
      const audioFiles = volFiles['vol-2'].filter(f =>
        f.endsWith('.mp3') && f.startsWith(stem) && !f.includes('__')
      )
      chapters.push({
        id: `vol2-${stem}`,
        slug: stem,
        volume: 'vol-2',
        section: section.group,
        section_label: section.label,
        source_path: path.join('chapters', section.dir, file),
        audio_path: audioPath,
        audio_files: audioFiles,
        has_audio: audioFiles.length > 0,
        title: extractTitle(stem, path.join(sectionDir, file)),
      })
    }
  }

  return chapters
}

let chapters = buildCatalog()

// ── SSE broadcast ─────────────────────────────────────────────────────────────

const sseClients = new Set()

function broadcast(event, data = {}) {
  const payload = `event: ${event}\ndata: ${JSON.stringify(data)}\n\n`
  for (const res of sseClients) {
    try { res.write(payload) } catch {}
  }
}

// ── File watching ─────────────────────────────────────────────────────────────

let rebuildTimer = null

function scheduleRebuild(reason) {
  if (rebuildTimer) clearTimeout(rebuildTimer)
  rebuildTimer = setTimeout(() => {
    chapters = buildCatalog()
    const withAudio = chapters.filter(c => c.has_audio).length
    console.log(`[watch] ${reason} → catalog rebuilt: ${chapters.length} chapters, ${withAudio} with audio`)
    broadcast('catalog-updated', { total: chapters.length, with_audio: withAudio })
  }, 400)
}

// Watch chapter markdown files
fs.watch(CHAPTERS_DIR, { recursive: true }, (event, filename) => {
  if (filename && filename.endsWith('.md')) scheduleRebuild(`vol-1/${filename} ${event}`)
})

// Watch audio output directory for new MP3s and manifest updates
fs.mkdirSync(AUDIO_DIR, { recursive: true })
fs.watch(AUDIO_DIR, { recursive: true }, (event, filename) => {
  if (!filename) return
  if (filename === 'manifest.json') {
    manifestDefaults = loadManifest()
    console.log('[watch] manifest.json updated - render defaults reloaded')
  } else if (filename.endsWith('.meta.json')) {
    sidecarDefaults = loadSidecars()
    console.log('[watch] sidecar updated - reloaded sidecars')
  } else if (filename.endsWith('.mp3') && !filename.includes('_chunk_cache')) {
    mp3TagDefaults = loadMp3Tags()
    scheduleRebuild(`audio/${filename} ${event}`)
  }
})

// Watch audiobook.py for CHAPTER_PRESET_MAP changes
fs.watch(path.join(REPO_ROOT, 'build', 'audiobook.py'), () => {
  chapterPresetMap = loadChapterPresetMap()
  console.log('[watch] audiobook.py updated - chapter preset map reloaded')
})

// ── In-memory job registry ────────────────────────────────────────────────────

const jobs = new Map()

// onFinish: optional callback called with the finished job object
function startGeneration(chapterId, options = {}, onFinish) {
  const chapter = chapters.find(c => c.id === chapterId)
  if (!chapter) throw new Error(`Chapter not found: ${chapterId}`)

  const logDir = path.join(AUDIO_DIR, '_logs')
  fs.mkdirSync(logDir, { recursive: true })
  const ts = Date.now()
  const logFile = path.join(logDir, `${chapter.slug}-web-${ts}.log`)

  const args = ['build/audiobook.py', '--only', chapter.slug]
  args.push('--engine', options.engine || 'kokoro')
  if (options.preset)               args.push('--preset', options.preset)
  if (options.voice)                args.push('--voice', options.voice)
  if (options.speed != null)        args.push('--speed', String(options.speed))
  if (options.exaggeration != null) args.push('--exaggeration', String(options.exaggeration))
  if (options.cfg_weight != null)   args.push('--cfg-weight', String(options.cfg_weight))
  if (options.temperature != null)  args.push('--temperature', String(options.temperature))
  if (options.base_url)             args.push('--base-url', options.base_url)
  if (options.api_key)              args.push('--api-key', options.api_key)
  if (options.force)                args.push('--force')
  if (options.per_sentence)         args.push('--per-sentence')
  if (options.no_chapter_map)       args.push('--no-chapter-map')
  if (options.output_suffix)        args.push('--output-suffix', options.output_suffix)

  const env = { ...process.env }
  if (options.api_key) env.TTS_API_KEY = options.api_key

  const logStream = fs.createWriteStream(logFile)
  const proc = spawn('python3', args, {
    cwd: REPO_ROOT,
    detached: true,
    stdio: ['ignore', logStream, logStream],
    env,
  })
  proc.unref()

  const jobId = `job-${ts}`
  const job = {
    id: jobId,
    status: 'running',
    chapter_id: chapterId,
    chapter_slug: chapter.slug,
    started: new Date().toISOString(),
    log_file: logFile,
    pid: proc.pid,
    exit_code: null,
  }
  jobs.set(jobId, job)

  proc.on('close', code => {
    job.status = code === 0 ? 'done' : 'failed'
    job.exit_code = code
    job.finished = new Date().toISOString()
    if (code === 0) {
      // Use output_suffix when writing the sidecar filename
      const sidecarPath = chapter.audio_path.replace('.mp3', (options.output_suffix || '') + '.meta.json')
      const meta = {
        engine:       options.engine || 'kokoro',
        preset:       options.preset || 'male',
        voice:        options.voice  || null,
        speed:        options.speed  ?? null,
        per_sentence: options.per_sentence ?? false,
        exaggeration: options.exaggeration ?? null,
        cfg_weight:   options.cfg_weight   ?? null,
        temperature:  options.temperature  ?? null,
        generated_at: job.finished,
        source:       'web-ui',
      }
      try {
        fs.writeFileSync(sidecarPath, JSON.stringify(meta, null, 2))
      } catch (e) {
        console.error('[sidecar] write failed:', sidecarPath, e.message)
      }
      sidecarDefaults[chapter.slug] = meta
    }
    broadcast('job-done', { job_id: jobId, chapter_id: chapterId, status: job.status })
    if (typeof onFinish === 'function') onFinish(job)
  })

  return job
}

// ── Job queue ─────────────────────────────────────────────────────────────────
const stagedQueue = []  // items staged but not yet processing
const jobQueue = []     // { queue_id, chapter_id, chapter_title, options, added_at, status }
let activeQueueItem = null
const queueHistory = []
const QUEUE_HISTORY_MAX = 30
let batchTotal = 0      // items in the last explicit process() call
let batchDone = 0       // items completed in that batch

function serializeQueue() {
  return {
    active: activeQueueItem ? { ...activeQueueItem, job: jobs.get(activeQueueItem.job_id) || null } : null,
    queue: [...jobQueue],
    staged: [...stagedQueue],
    history: queueHistory.slice(0, 10),
    batch: batchTotal > 0 ? { total: batchTotal, done: batchDone } : null,
  }
}

function processNextInQueue() {
  if (activeQueueItem || jobQueue.length === 0) return
  const item = jobQueue.shift()
  item.status = 'running'
  item.started_at = new Date().toISOString()
  activeQueueItem = item
  broadcast('queue-updated', serializeQueue())
  try {
    const job = startGeneration(item.chapter_id, item.options, (finishedJob) => {
      item.status = finishedJob.status
      item.job_id = finishedJob.id
      item.finished_at = finishedJob.finished
      queueHistory.unshift({ ...item })
      if (queueHistory.length > QUEUE_HISTORY_MAX) queueHistory.pop()
      batchDone++
      activeQueueItem = null
      broadcast('queue-updated', serializeQueue())
      processNextInQueue()
    })
    item.job_id = job.id
  } catch (e) {
    item.status = 'failed'
    item.error = e.message
    item.finished_at = new Date().toISOString()
    queueHistory.unshift({ ...item })
    activeQueueItem = null
    broadcast('queue-updated', serializeQueue())
    processNextInQueue()
  }
}

// ── API routes ────────────────────────────────────────────────────────────────

app.get('/api/events', (req, res) => {
  res.set({
    'Content-Type': 'text/event-stream',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'X-Accel-Buffering': 'no',
  })
  res.flushHeaders()
  res.write('event: connected\ndata: {}\n\n')

  const keepalive = setInterval(() => {
    try { res.write(': ping\n\n') } catch {}
  }, 25000)

  sseClients.add(res)
  req.on('close', () => { sseClients.delete(res); clearInterval(keepalive) })
})

app.get('/api/chapters', (_req, res) => {
  res.json(chapters.map(ch => {
    const relPath = ch.source_path.replace(/^chapters\//, '').replace(/\.md$/, '')

    // Build tracks array from audio_files
    const tracks = ch.audio_files.map(filename => {
      const fileKey = filename.replace(/\.mp3$/, '')
      const stem = ch.slug
      // key: 'primary' for {slug}.mp3, or the voice name for {slug}--{voice}.mp3
      let key
      if (filename === `${stem}.mp3`) {
        key = 'primary'
      } else {
        // Extract voice from {slug}--{voice}.mp3 pattern
        const voiceMatch = filename.match(new RegExp(`^${stem}--(.+)\\.mp3$`))
        key = voiceMatch ? voiceMatch[1] : fileKey
      }
      const tags = mp3TagDefaults[fileKey] ?? null
      return {
        key,
        url: `/api/audio/${ch.volume}/${filename}`,
        engine:       tags?.engine       ?? null,
        preset:       tags?.preset       ?? null,
        voice:        tags?.voice        ?? null,
        speed:        tags?.speed        ?? null,
        per_sentence: tags?.per_sentence ?? false,
      }
    })

    // Priority: MP3 tags (embedded by audiobook.py) > sidecar (web-UI) > manifest (batch) > chapter-map (planned)
    const info = mp3TagDefaults[ch.slug]
              ?? sidecarDefaults[ch.slug]
              ?? manifestDefaults[ch.slug]
              ?? null
    const plannedPreset = !info
      ? (chapterPresetMap[ch.slug] ?? chapterPresetMap[relPath] ?? null)
      : null

    return {
      id: ch.id,
      slug: ch.slug,
      title: ch.title,
      volume: ch.volume,
      section: ch.section,
      section_label: ch.section_label,
      has_audio: ch.has_audio,
      tracks,
      // backward compat: audio_info = first track's tag info (or null)
      audio_info: tracks.length > 0 && tracks[0].engine ? {
        engine:       tracks[0].engine,
        preset:       tracks[0].preset,
        voice:        tracks[0].voice || null,
        speed:        tracks[0].speed,
        per_sentence: tracks[0].per_sentence,
        exaggeration: info?.exaggeration ?? null,
      } : (info ? {
        engine:       info.engine,
        preset:       info.preset,
        voice:        info.voice || null,
        speed:        info.speed,
        per_sentence: info.per_sentence,
        exaggeration: info.exaggeration,
      } : null),
      planned_preset: plannedPreset,
    }
  }))
})

app.get('/api/chapters/:id/content', (req, res) => {
  const chapter = chapters.find(c => c.id === req.params.id)
  if (!chapter) return res.status(404).json({ error: 'Not found' })
  try {
    const content = fs.readFileSync(path.join(REPO_ROOT, chapter.source_path), 'utf8')
    res.json({ content })
  } catch {
    res.status(500).json({ error: 'Failed to read chapter' })
  }
})

app.get('/api/chapters/:id/alignment', (req, res) => {
  const chapter = chapters.find(c => c.id === req.params.id)
  if (!chapter) return res.status(404).json({ error: 'Not found' })
  const alignPath = path.join(CHAPTERS_DIR, '_voice-drafts', '_alignments', `${chapter.slug}.json`)
  try {
    const data = JSON.parse(fs.readFileSync(alignPath, 'utf8'))
    // Check if alignment predates the current audio file
    const alignMtime = fs.statSync(alignPath).mtimeMs
    const mp3Path = path.join(AUDIO_DIR, chapter.volume, `${chapter.slug}.mp3`)
    let stale = false
    try {
      const mp3Mtime = fs.statSync(mp3Path).mtimeMs
      stale = mp3Mtime - alignMtime > 3600_000 // stale if audio is >1h newer
    } catch { /* no mp3 yet */ }
    res.json({ ...data, stale })
  } catch {
    res.status(404).json({ error: 'No alignment data' })
  }
})

app.get('/api/chapters/:id/render-defaults', (req, res) => {
  const chapter = chapters.find(c => c.id === req.params.id)
  if (!chapter) return res.status(404).json({ error: 'Not found' })

  // 1a. MP3 embedded tags - ground truth, written by audiobook.py on every render
  const fromTags = mp3TagDefaults[chapter.slug]
  if (fromTags) return res.json({ ...fromTags, source: 'manifest' })

  // 1b. Web-UI sidecar - reliable for renders done via the web UI
  const fromSidecar = sidecarDefaults[chapter.slug]
  if (fromSidecar) return res.json({ ...fromSidecar, source: 'manifest' })

  // 1c. Batch manifest - may be stale if chapter was later regenerated externally
  const fromManifest = manifestDefaults[chapter.slug]
  if (fromManifest) return res.json({ ...fromManifest, source: 'manifest' })

  // 2. CHAPTER_PRESET_MAP: intended preset from audiobook.py
  //    Keys are either bare slug ("ch05-enterprise-lens") or relative path
  //    ("book-2/act-1/ch01-departure"). Build both forms to check.
  const relPath = chapter.source_path.replace(/^chapters\//, '').replace(/\.md$/, '')
  const preset = chapterPresetMap[chapter.slug] ?? chapterPresetMap[relPath] ?? null
  if (preset) {
    return res.json({ engine: 'chatterbox', preset, voice: '', source: 'chapter-map' })
  }

  // 3. Global default
  res.json({ engine: 'kokoro', preset: 'male', voice: '', source: 'default' })
})

app.get('/api/audio/:volume/:filename', (req, res) => {
  const { volume, filename } = req.params
  if (filename.includes('/') || filename.includes('..')) {
    return res.status(400).json({ error: 'Invalid filename' })
  }
  const audioPath = path.join(AUDIO_DIR, volume, filename)
  if (!fs.existsSync(audioPath)) return res.status(404).json({ error: 'Not found' })

  const stat = fs.statSync(audioPath)
  const fileSize = stat.size
  const range = req.headers.range

  if (range) {
    const [startStr, endStr] = range.replace(/bytes=/, '').split('-')
    const start = parseInt(startStr, 10)
    const end = endStr ? parseInt(endStr, 10) : fileSize - 1
    res.status(206).set({
      'Content-Range': `bytes ${start}-${end}/${fileSize}`,
      'Accept-Ranges': 'bytes',
      'Content-Length': end - start + 1,
      'Content-Type': 'audio/mpeg',
    })
    fs.createReadStream(audioPath, { start, end }).pipe(res)
  } else {
    res.set({
      'Accept-Ranges': 'bytes',
      'Content-Length': fileSize,
      'Content-Type': 'audio/mpeg',
    })
    fs.createReadStream(audioPath).pipe(res)
  }
})

app.post('/api/generate', (req, res) => {
  const { chapter_id, ...options } = req.body
  if (!chapter_id) return res.status(400).json({ error: 'chapter_id required' })
  try {
    const job = startGeneration(chapter_id, options)
    res.json(job)
  } catch (err) {
    res.status(400).json({ error: err.message })
  }
})

app.get('/api/jobs', (_req, res) => res.json([...jobs.values()]))

app.get('/api/jobs/:jobId', (req, res) => {
  const job = jobs.get(req.params.jobId)
  if (!job) return res.status(404).json({ error: 'Job not found' })
  res.json(job)
})

app.get('/api/jobs/:jobId/log', (req, res) => {
  const job = jobs.get(req.params.jobId)
  if (!job) return res.status(404).json({ error: 'Job not found' })
  try {
    const tail = req.query.tail ? parseInt(req.query.tail) : 80
    const raw = fs.existsSync(job.log_file) ? fs.readFileSync(job.log_file, 'utf8') : ''
    const lines = raw.split('\n')
    res.json({ log: lines.slice(-tail).join('\n'), total_lines: lines.length })
  } catch {
    res.json({ log: '', total_lines: 0 })
  }
})

// ── Log viewer API ────────────────────────────────────────────────────────────

const CHUNK_RE = /\[\s*(\d+)\/(\d+)\]\s+([\d.]+)%/
const HEADER_RE = /^(Engine|base_url|preset|voice|speed|exaggeration|cfg_weight|mode|chapter|output|Rendering)\s*[:=]/i

function parseLogMeta(filename, lines) {
  let lastChunk = null, totalChunks = null, lastProgress = 0
  for (let i = lines.length - 1; i >= 0; i--) {
    const m = lines[i].match(CHUNK_RE)
    if (m) { lastChunk = parseInt(m[1]); totalChunks = parseInt(m[2]); lastProgress = parseFloat(m[3]); break }
  }
  const hasError = lines.some(l => l.includes('Traceback') || (l.includes('Error:') && !/retry \d/.test(l)))
  const hasRetry = lines.some(l => /retry \d+\/\d+/.test(l))
  const isBatch = /^(auto-sync|full-render)/.test(filename)
  let status = 'done'
  if (hasError) status = 'error'
  else if (lastChunk !== null && lastProgress < 99.5) status = 'incomplete'
  else if (lastChunk === null && !isBatch) status = 'incomplete'
  return { filename, status, progress: lastProgress, lastChunk, totalChunks, hasRetry, hasError, isBatch }
}

function safeLogFilename(filename) {
  return filename && !filename.includes('/') && !filename.includes('..') && filename.endsWith('.log')
}

app.get('/api/logs', (_req, res) => {
  try {
    if (!fs.existsSync(LOG_DIR)) return res.json([])
    const files = fs.readdirSync(LOG_DIR)
      .filter(f => f.endsWith('.log'))
      .map(filename => {
        try {
          const filepath = path.join(LOG_DIR, filename)
          const stat = fs.statSync(filepath)
          const raw = fs.readFileSync(filepath, 'utf8')
          const lines = raw.split('\n')
          const meta = parseLogMeta(filename, lines)
          const ageMs = Date.now() - stat.mtimeMs
          const isRunning = ageMs < 120_000 && meta.status !== 'error' && meta.status !== 'done'
          return { ...meta, status: isRunning ? 'running' : meta.status, mtime: stat.mtimeMs, size: stat.size, lineCount: lines.length }
        } catch { return null }
      })
      .filter(Boolean)
      .sort((a, b) => b.mtime - a.mtime)
    res.json(files)
  } catch (e) { res.status(500).json({ error: e.message }) }
})

app.get('/api/logs/:filename', (req, res) => {
  const { filename } = req.params
  if (!safeLogFilename(filename)) return res.status(400).json({ error: 'Invalid filename' })
  const filepath = path.join(LOG_DIR, filename)
  if (!fs.existsSync(filepath)) return res.status(404).json({ error: 'Log not found' })
  try {
    const raw = fs.readFileSync(filepath, 'utf8')
    const lines = raw.split('\n')
    const stat = fs.statSync(filepath)
    const meta = parseLogMeta(filename, lines)
    const ageMs = Date.now() - stat.mtimeMs
    const isRunning = ageMs < 120_000 && meta.status !== 'error' && meta.status !== 'done'
    res.json({ ...meta, status: isRunning ? 'running' : meta.status, lines: lines.slice(-1000), total_lines: lines.length, mtime: stat.mtimeMs })
  } catch (e) { res.status(500).json({ error: e.message }) }
})

app.get('/api/logs/:filename/tail', (req, res) => {
  const { filename } = req.params
  if (!safeLogFilename(filename)) return res.status(400).json({ error: 'Invalid filename' })
  const from = Math.max(0, parseInt(req.query.from || '0', 10))
  const filepath = path.join(LOG_DIR, filename)
  if (!fs.existsSync(filepath)) return res.status(404).json({ error: 'Log not found' })
  try {
    const raw = fs.readFileSync(filepath, 'utf8')
    const lines = raw.split('\n')
    const stat = fs.statSync(filepath)
    const meta = parseLogMeta(filename, lines)
    const ageMs = Date.now() - stat.mtimeMs
    const isRunning = ageMs < 120_000 && meta.status !== 'error' && meta.status !== 'done'
    res.json({ lines: lines.slice(from), from, total_lines: lines.length, status: isRunning ? 'running' : meta.status, progress: meta.progress, lastChunk: meta.lastChunk, totalChunks: meta.totalChunks })
  } catch (e) { res.status(500).json({ error: e.message }) }
})

// ── Queue API ─────────────────────────────────────────────────────────────────

app.get('/api/queue', (_req, res) => {
  res.json(serializeQueue())
})

app.post('/api/queue', (req, res) => {
  const { items = [] } = req.body
  if (!Array.isArray(items) || items.length === 0) {
    return res.status(400).json({ error: 'items array required' })
  }
  const added = []
  for (const item of items) {
    const { chapter_id, options = {} } = item
    if (!chapter_id) continue
    const chapterObj = chapters.find(c => c.id === chapter_id)
    if (!chapterObj) continue
    const queueItem = {
      queue_id:      `q-${Date.now()}-${randomBytes(3).toString('hex')}`,
      chapter_id,
      chapter_title: chapterObj.title,
      options,
      added_at:      new Date().toISOString(),
      status:        'staged',
    }
    stagedQueue.push(queueItem)
    added.push(queueItem)
  }
  broadcast('queue-updated', serializeQueue())
  res.json({ added: added.length, queue: serializeQueue() })
})

app.post('/api/queue/process', (_req, res) => {
  if (stagedQueue.length === 0) {
    return res.json({ started: 0, queue: serializeQueue() })
  }
  const toProcess = stagedQueue.splice(0)
  batchTotal = toProcess.length
  batchDone = 0
  for (const item of toProcess) {
    item.status = 'pending'
    jobQueue.push(item)
  }
  processNextInQueue()
  broadcast('queue-updated', serializeQueue())
  res.json({ started: toProcess.length, queue: serializeQueue() })
})

app.delete('/api/queue/staged/:qid', (req, res) => {
  const idx = stagedQueue.findIndex(item => item.queue_id === req.params.qid)
  if (idx === -1) return res.status(404).json({ error: 'Staged item not found' })
  stagedQueue.splice(idx, 1)
  broadcast('queue-updated', serializeQueue())
  res.json(serializeQueue())
})

app.delete('/api/queue/:qid', (req, res) => {
  const idx = jobQueue.findIndex(item => item.queue_id === req.params.qid)
  if (idx === -1) return res.status(404).json({ error: 'Queue item not found' })
  jobQueue.splice(idx, 1)
  broadcast('queue-updated', serializeQueue())
  res.json(serializeQueue())
})

app.delete('/api/queue', (_req, res) => {
  stagedQueue.length = 0
  jobQueue.length = 0
  batchTotal = 0
  batchDone = 0
  broadcast('queue-updated', serializeQueue())
  res.json(serializeQueue())
})

// ── Editorial review session ──────────────────────────────────────────────────
const REVIEW_SESSION_FILE = path.join(REPO_ROOT, 'build', 'output', 'review-session.json')
const PAO_INBOX_DIR = path.join(REPO_ROOT, '.pao-inbox')

function loadReviewSession() {
  try {
    if (fs.existsSync(REVIEW_SESSION_FILE)) {
      return JSON.parse(fs.readFileSync(REVIEW_SESSION_FILE, 'utf8'))
    }
  } catch {}
  return newSession()
}

function newSession() {
  return { id: `review-${Date.now()}`, started: new Date().toISOString(), comments: [] }
}

function saveReviewSession(session) {
  try {
    fs.mkdirSync(path.dirname(REVIEW_SESSION_FILE), { recursive: true })
    fs.writeFileSync(REVIEW_SESSION_FILE, JSON.stringify(session, null, 2))
  } catch (e) {
    console.error('[review] save failed:', e.message)
  }
}

let reviewSession = loadReviewSession()

function buildReviewInboxContent(session) {
  const now = new Date().toISOString()
  const chapterIds = [...new Set(session.comments.map(c => c.chapter_id))]
  const n = session.comments.length
  const nc = chapterIds.length

  const frontmatter = [
    '---',
    `type: co-editorial-review`,
    `session: ${session.id}`,
    `chapters_reviewed: ${nc}`,
    `comment_count: ${n}`,
    `submitted: ${now}`,
    '---',
    '',
    `CO conducted a review session covering ${nc} chapter${nc !== 1 ? 's' : ''} with ${n} editorial note${n !== 1 ? 's' : ''}. Delegate each item to Yeoman using the type as the action verb: EDIT → implement the change directly; FLAG → fix the style or quality violation; NOTE → consider and optionally act; QUESTION → answer and implement if the answer is clear.`,
    '',
  ].join('\n')

  const sections = chapterIds.map(chapterId => {
    const chComments = session.comments.filter(c => c.chapter_id === chapterId)
    const { chapter_title, chapter_slug } = chComments[0]
    const header = `## ${chapter_slug} - ${chapter_title}\n`
    const items = chComments.map((c) => {
      const tag = { edit: 'EDIT', flag: 'FLAG', note: 'NOTE', question: 'QUESTION' }[c.type] || c.type.toUpperCase()
      const excerptLine = c.excerpt
        ? `> *"${c.excerpt.length > 140 ? c.excerpt.slice(0, 140) + '…' : c.excerpt}"*\n`
        : ''
      return `**[${tag}]**\n${excerptLine}${c.comment}\n`
    }).join('\n')
    return header + '\n' + items
  }).join('\n---\n\n')

  return frontmatter + sections
}

app.get('/api/review/session', (_req, res) => {
  res.json({ ...reviewSession, comment_count: reviewSession.comments.length })
})

app.post('/api/review/comment', (req, res) => {
  const { chapter_id, chapter_title, chapter_slug, excerpt, comment, type } = req.body
  if (!chapter_id || !comment || !type) {
    return res.status(400).json({ error: 'chapter_id, comment, and type are required' })
  }
  reviewSession.comments.push({
    chapter_id,
    chapter_title: chapter_title || chapter_id,
    chapter_slug: chapter_slug || chapter_id,
    excerpt: excerpt || '',
    comment,
    type,
    added_at: new Date().toISOString(),
  })
  saveReviewSession(reviewSession)
  res.json({ ...reviewSession, comment_count: reviewSession.comments.length })
})

app.patch('/api/review/comment/:idx', (req, res) => {
  const idx = parseInt(req.params.idx, 10)
  if (isNaN(idx) || idx < 0 || idx >= reviewSession.comments.length) {
    return res.status(400).json({ error: 'Invalid comment index' })
  }
  const { comment } = req.body
  if (!comment) return res.status(400).json({ error: 'comment required' })
  reviewSession.comments[idx] = { ...reviewSession.comments[idx], comment, updated_at: new Date().toISOString() }
  saveReviewSession(reviewSession)
  res.json({ ...reviewSession, comment_count: reviewSession.comments.length })
})

app.delete('/api/review/comment/:idx', (req, res) => {
  const idx = parseInt(req.params.idx, 10)
  if (isNaN(idx) || idx < 0 || idx >= reviewSession.comments.length) {
    return res.status(400).json({ error: 'Invalid comment index' })
  }
  reviewSession.comments.splice(idx, 1)
  saveReviewSession(reviewSession)
  res.json({ ...reviewSession, comment_count: reviewSession.comments.length })
})

app.delete('/api/review/session', (_req, res) => {
  reviewSession = newSession()
  saveReviewSession(reviewSession)
  res.json({ ...reviewSession, comment_count: reviewSession.comments.length })
})

app.post('/api/review/submit', (req, res) => {
  const { clear_after = true } = req.body || {}
  if (reviewSession.comments.length === 0) {
    return res.status(400).json({ error: 'No comments to submit' })
  }
  try {
    fs.mkdirSync(PAO_INBOX_DIR, { recursive: true })
    const ts = new Date().toISOString().slice(0, 16).replace(/[T:]/g, '-')
    const filename = `co-review-${ts}Z.md`
    const filePath = path.join(PAO_INBOX_DIR, filename)
    const content = buildReviewInboxContent(reviewSession)
    fs.writeFileSync(filePath, content)
    const comment_count = reviewSession.comments.length
    if (clear_after) {
      reviewSession = newSession()
      saveReviewSession(reviewSession)
    }
    res.json({
      file: path.relative(REPO_ROOT, filePath),
      comment_count,
      cleared: clear_after,
    })
  } catch (e) {
    console.error('[review] submit failed:', e.message)
    res.status(500).json({ error: 'Failed to write inbox file' })
  }
})

// ── Static file serving (production) ─────────────────────────────────────────

if (fs.existsSync(DIST_DIR)) {
  app.use(express.static(DIST_DIR))
  app.get('*', (_req, res) => res.sendFile(path.join(DIST_DIR, 'index.html')))
} else {
  app.get('/', (_req, res) => {
    res.send('<h2>Run <code>npm run build</code> first, then restart the server.</h2>')
  })
}

app.listen(PORT, () => {
  console.log(`The Inverted Stack reader → http://localhost:${PORT}`)
  console.log(`${chapters.length} chapters, ${chapters.filter(c => c.has_audio).length} with audio`)
  console.log(`Watching: chapters/ and build/output/audiobook/`)
  if (!fs.existsSync(DIST_DIR)) console.log('No dist/ - run: npm run build')
})
