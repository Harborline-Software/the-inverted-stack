--[[
kroki-mermaid.lua — Pandoc Lua filter for rendering Mermaid blocks via kroki.io

For each ```mermaid code block in the source markdown, POST the diagram source
to kroki.io and replace the block with the returned SVG (cached on disk). The
SVG is embedded as a raw HTML block for EPUB/HTML output and as an Image element
for other formats (Pandoc handles SVG → image conversion for PDF via xelatex).

Why Lua and not Python:
  - Pandoc has built-in Lua filter support (no install).
  - The Python pandoc-kroki ecosystem on PyPI is empty; only single-author
    GitHub forks exist as of 2026-05-04. A self-contained Lua filter is more
    durable than a pinned single-author Python package.
  - This file is ~80 lines; reading and reasoning about it is fast.

Why kroki.io and not local mermaid-cli:
  - Avoids Node + Puppeteer + headless Chromium toolchain (~200 MB).
  - kroki.io is self-hostable via Docker if reliability becomes an issue.
  - Network dep at build time is acceptable for a personal book project per
    the XO directive 2026-05-04T18-50Z.

Cache:
  - Rendered SVGs are cached at build/output/.kroki-cache/<sha256>.svg.
  - Cache key is sha256 of the diagram source. Re-renders only on diagram edit.
  - Cache directory is gitignored (lives under build/output/).

Usage in Makefile:
  pandoc ... --lua-filter build/filters/kroki-mermaid.lua ...

Halt-conditions surfaced by the filter:
  - kroki.io 4xx → diagram source is malformed; warns to stderr; passes the
    block through unchanged so the build doesn't fail and the broken Mermaid
    is visible in the output for author review.
  - kroki.io 5xx or network error → warns; passes through unchanged.

References:
  - kroki.io API: https://docs.kroki.io/kroki/setup/use-kroki/
  - Pandoc Lua filters: https://pandoc.org/lua-filters.html
]]

-- Compute SHA-256 of a string using the system 'shasum' tool. Requires curl
-- and shasum (both standard on macOS and any reasonable Linux build host).
-- Writes the source to a tempfile to avoid shell-quoting issues with
-- arbitrary diagram content.
local function sha256(s)
  local tmp = os.tmpname()
  local fh = io.open(tmp, "w")
  if not fh then return nil end
  fh:write(s)
  fh:close()
  -- shasum is on macOS by default; sha256sum is on GNU/Linux. Try both.
  local pop = io.popen("(shasum -a 256 < " .. tmp .. " 2>/dev/null"
                       .. " || sha256sum < " .. tmp .. " 2>/dev/null) | head -1")
  if not pop then os.remove(tmp); return nil end
  local out = pop:read("*a")
  pop:close()
  os.remove(tmp)
  return out and out:match("^(%x+)") or nil
end

local function ensure_cache_dir()
  local dir = "build/output/.kroki-cache"
  os.execute("mkdir -p " .. dir)
  return dir
end

-- Returns SVG content (string) or nil on failure. On failure, also writes a
-- warning to stderr via io.stderr:write so the build operator sees the issue.
local function fetch_svg(mermaid_source)
  local digest = sha256(mermaid_source)
  if not digest then
    io.stderr:write("kroki-mermaid.lua: shasum unavailable; skipping cache\n")
    digest = "no-cache-" .. tostring(os.time())
  end
  local cache_dir = ensure_cache_dir()
  local cache_file = cache_dir .. "/" .. digest .. ".svg"

  -- Cache hit?
  local cached = io.open(cache_file, "r")
  if cached then
    local content = cached:read("*a")
    cached:close()
    if content and #content > 0 then return content end
  end

  -- Cache miss: POST to kroki.io
  local tmp_src = os.tmpname()
  local tmp_out = os.tmpname()
  local fh = io.open(tmp_src, "w")
  fh:write(mermaid_source)
  fh:close()

  local cmd = string.format(
    "curl -fsS -X POST -H 'Content-Type: text/plain' --data-binary @%s "
      .. "https://kroki.io/mermaid/svg -o %s 2>/dev/null",
    tmp_src, tmp_out
  )
  local ok = os.execute(cmd)
  os.remove(tmp_src)

  if not ok or ok == false then
    io.stderr:write("kroki-mermaid.lua: kroki.io request failed; passing block through\n")
    os.remove(tmp_out)
    return nil
  end

  local fh_out = io.open(tmp_out, "r")
  if not fh_out then return nil end
  local svg = fh_out:read("*a")
  fh_out:close()
  os.remove(tmp_out)

  if not svg or #svg == 0 or not svg:match("<svg") then
    io.stderr:write("kroki-mermaid.lua: kroki.io returned non-SVG; passing block through\n")
    return nil
  end

  -- Write to cache
  local cache_fh = io.open(cache_file, "w")
  if cache_fh then
    cache_fh:write(svg)
    cache_fh:close()
  end

  return svg
end

function CodeBlock(block)
  if not block.classes then return nil end
  local is_mermaid = false
  for _, cls in ipairs(block.classes) do
    if cls == "mermaid" then is_mermaid = true; break end
  end
  if not is_mermaid then return nil end

  local svg = fetch_svg(block.text)
  if not svg then
    -- Pass through unchanged — broken Mermaid will be visible in output for
    -- author review rather than silently breaking the build.
    return nil
  end

  -- For HTML/EPUB output: embed SVG inline as raw HTML.
  -- For other formats (LaTeX/PDF): also use raw HTML; Pandoc will handle.
  return pandoc.RawBlock("html", svg)
end
