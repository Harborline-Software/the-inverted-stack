import { useState, useEffect, useRef, useCallback } from 'react'
import ChapterList from './components/ChapterList.jsx'
import ChapterView from './components/ChapterView.jsx'
import QueuePanel from './components/QueuePanel.jsx'
import ReviewPanel from './components/ReviewPanel.jsx'
import LogPanel from './components/LogPanel.jsx'

const SIDEBAR_MIN = 180
const SIDEBAR_MAX = 520
const SIDEBAR_DEFAULT = 280
const READER_STATE_KEY = 'inverted-stack-reader-v1'

function loadReaderState() {
  try { return JSON.parse(localStorage.getItem(READER_STATE_KEY) || '{}') }
  catch { return {} }
}

function saveReaderState(updates) {
  try {
    const cur = loadReaderState()
    localStorage.setItem(READER_STATE_KEY, JSON.stringify({ ...cur, ...updates }))
  } catch {}
}

export default function App() {
  const [chapters, setChapters] = useState([])
  const [selectedId, setSelectedId] = useState(null)
  const [volume, setVolume] = useState('vol-1')
  const [loading, setLoading] = useState(true)
  const [sidebarWidth, setSidebarWidth] = useState(
    () => parseInt(localStorage.getItem('sidebarWidth') || SIDEBAR_DEFAULT, 10)
  )
  const [queue, setQueue] = useState({ active: null, queue: [], staged: [], history: [], batch: null })
  const [showQueue, setShowQueue] = useState(false)
  const [reviewSession, setReviewSession] = useState({ id: null, started: null, comments: [], comment_count: 0 })
  const [showReview, setShowReview] = useState(false)
  const [showLogs, setShowLogs] = useState(false)

  // savedChapterState is passed to ChapterView so it can restore audio time + scroll
  const [savedChapterState, setSavedChapterState] = useState({ audioTime: 0, scrollTop: 0 })

  const dragging = useRef(false)
  const startX = useRef(0)
  const startW = useRef(0)

  const onMouseDown = useCallback(e => {
    e.preventDefault()
    dragging.current = true
    startX.current = e.clientX
    startW.current = sidebarWidth
    document.body.style.cursor = 'col-resize'
    document.body.style.userSelect = 'none'
  }, [sidebarWidth])

  useEffect(() => {
    const onMouseMove = e => {
      if (!dragging.current) return
      const delta = e.clientX - startX.current
      const next = Math.min(SIDEBAR_MAX, Math.max(SIDEBAR_MIN, startW.current + delta))
      setSidebarWidth(next)
    }
    const onMouseUp = () => {
      if (!dragging.current) return
      dragging.current = false
      document.body.style.cursor = ''
      document.body.style.userSelect = ''
      setSidebarWidth(w => { localStorage.setItem('sidebarWidth', w); return w })
    }
    window.addEventListener('mousemove', onMouseMove)
    window.addEventListener('mouseup', onMouseUp)
    return () => {
      window.removeEventListener('mousemove', onMouseMove)
      window.removeEventListener('mouseup', onMouseUp)
    }
  }, [])

  const refreshChapters = useCallback(() => {
    fetch('/api/chapters')
      .then(r => r.json())
      .then(setChapters)
      .catch(() => {})
  }, [])

  const fetchReviewSession = useCallback(() => {
    fetch('/api/review/session').then(r => r.json()).then(setReviewSession).catch(() => {})
  }, [])

  useEffect(() => { fetchReviewSession() }, [fetchReviewSession])

  // Initial load — restore last session after chapters arrive
  useEffect(() => {
    fetch('/api/chapters')
      .then(r => r.json())
      .then(data => {
        setChapters(data)
        setLoading(false)
        const state = loadReaderState()
        if (state.volume) setVolume(state.volume)
        if (state.chapterId) {
          const ch = data.find(c => c.id === state.chapterId)
          if (ch) {
            setSavedChapterState({ audioTime: state.audioTime || 0, scrollTop: state.scrollTop || 0 })
            setSelectedId(state.chapterId)
          }
        }
      })
      .catch(() => setLoading(false))
  }, [])

  // Live updates via SSE
  useEffect(() => {
    let es
    function connect() {
      es = new EventSource('/api/events')
      es.addEventListener('catalog-updated', refreshChapters)
      es.addEventListener('job-done', refreshChapters)
      es.addEventListener('queue-updated', e => setQueue(JSON.parse(e.data)))
      es.onerror = () => { es.close(); setTimeout(connect, 3000) }
    }
    connect()
    return () => es?.close()
  }, [refreshChapters])

  const handleSelectChapter = useCallback((id) => {
    const state = loadReaderState()
    if (state.chapterId === id) {
      // Same chapter — restore saved position
      setSavedChapterState({ audioTime: state.audioTime || 0, scrollTop: state.scrollTop || 0 })
    } else {
      // Different chapter — start fresh
      setSavedChapterState({ audioTime: 0, scrollTop: 0 })
      saveReaderState({ chapterId: id, audioTime: 0, scrollTop: 0 })
    }
    setSelectedId(id)
  }, [])

  const handleVolumeSwitch = useCallback((vol) => {
    setVolume(vol)
    setSelectedId(null)
    saveReaderState({ volume: vol, chapterId: null, audioTime: 0, scrollTop: 0 })
  }, [])

  const handleAddToQueue = useCallback(() => { setShowQueue(true) }, [])

  const selected = chapters.find(c => c.id === selectedId) || null
  const queueBusy = !!(queue.active || queue.queue.length > 0 || queue.staged?.length > 0)

  return (
    <div className="app">
      <div className="sidebar" style={{ width: sidebarWidth, minWidth: sidebarWidth }}>
        <div className="sidebar-header">
          <div className="sidebar-title">The Inverted Stack</div>
          <div className="volume-tabs">
            <button
              className={`vol-tab ${volume === 'vol-1' ? 'active' : ''}`}
              onClick={() => handleVolumeSwitch('vol-1')}
            >
              Vol 1
            </button>
            <button
              className={`vol-tab ${volume === 'vol-2' ? 'active' : ''}`}
              onClick={() => handleVolumeSwitch('vol-2')}
            >
              Vol 2
            </button>
          </div>
        </div>
        {loading ? (
          <div className="sidebar-empty">Loading chapters…</div>
        ) : (
          <ChapterList
            chapters={chapters.filter(c => c.volume === volume)}
            selectedId={selectedId}
            onSelect={handleSelectChapter}
          />
        )}
      </div>

      <div className="resize-handle" onMouseDown={onMouseDown} />

      <div className="main">
        <div className="main-topbar">
          <button
            className={`review-toggle${reviewSession.comment_count > 0 ? ' review-toggle--active' : ''}`}
            onClick={() => setShowReview(v => !v)}
            title="Review Session"
          >
            {reviewSession.comment_count > 0 && (
              <span className="review-badge">{reviewSession.comment_count}</span>
            )}
            Review
          </button>
          <button
            className={`queue-toggle ${queueBusy ? 'queue-toggle--busy' : ''}`}
            onClick={() => setShowQueue(v => !v)}
            title="Render Queue"
          >
            {queueBusy && (
              <span className="queue-badge">
                {(queue.staged?.length || 0) + queue.queue.length + (queue.active ? 1 : 0)}
              </span>
            )}
            Render Queue
          </button>
          <button
            className={`queue-toggle${showLogs ? ' queue-toggle--busy' : ''}`}
            onClick={() => setShowLogs(v => !v)}
            title="Build Logs"
          >
            Logs
          </button>
          <span className="topbar-divider" />
          <a href="http://desktop-umt08rn:8881/" target="_blank" rel="noopener noreferrer" className="topbar-link">API Demo</a>
          <a href="http://desktop-umt08rn:8881/api/docs" target="_blank" rel="noopener noreferrer" className="topbar-link">API Docs</a>
        </div>

        {selected ? (
          <ChapterView
            chapter={selected}
            onAudioGenerated={refreshChapters}
            queueActive={queueBusy}
            onAddToQueue={handleAddToQueue}
            onCommentAdded={fetchReviewSession}
            savedState={savedChapterState}
            onReaderStateChange={saveReaderState}
            reviewComments={reviewSession.comments}
          />
        ) : (
          <div className="welcome">
            <div className="welcome-inner">
              <div className="welcome-icon">📖</div>
              <h2>Select a chapter to begin</h2>
              <p>
                {volume === 'vol-1'
                  ? 'Volume 1 — The Inverted Stack: Local-First Nodes in a SaaS World'
                  : 'Volume 2 — Sunfish-1 Mission Narrative'}
              </p>
              <p className="welcome-stats">
                {chapters.filter(c => c.volume === volume).length} chapters •{' '}
                {chapters.filter(c => c.volume === volume && c.has_audio).length} with audio
              </p>
            </div>
          </div>
        )}
      </div>

      {showQueue && (
        <>
          <div className="queue-overlay" onClick={() => setShowQueue(false)} />
          <QueuePanel
            chapters={chapters}
            queue={queue}
            onClose={() => setShowQueue(false)}
          />
        </>
      )}

      {showReview && (
        <>
          <div className="queue-overlay" onClick={() => setShowReview(false)} />
          <ReviewPanel
            session={reviewSession}
            onClose={() => setShowReview(false)}
            onSessionUpdate={fetchReviewSession}
          />
        </>
      )}

      {showLogs && <LogPanel onClose={() => setShowLogs(false)} />}

      {queue.batch && queue.batch.total > 0 && (
        <div className="render-progress-footer">
          <div className="render-progress-label">
            Rendering {queue.batch.done}/{queue.batch.total} chapters
            {queue.active && <span className="render-progress-current"> — {queue.active.chapter_title}</span>}
          </div>
          <div className="render-progress-track">
            <div
              className="render-progress-fill"
              style={{ width: `${Math.round((queue.batch.done / queue.batch.total) * 100)}%` }}
            />
          </div>
          <div className="render-progress-pct">
            {Math.round((queue.batch.done / queue.batch.total) * 100)}%
          </div>
        </div>
      )}
    </div>
  )
}
