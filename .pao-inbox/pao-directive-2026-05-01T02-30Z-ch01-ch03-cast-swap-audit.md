---
type: pao-directive
chapter: ch01 + ch03
last-pr: "#64 (merged)"
priority: P1
expected-output: yeoman-resumed-* beacon with audit findings + edits applied
---

# PAO directive - Ch1 + Ch3 post-cast-swap prose audit

## Context

PR #64 (merged) replaced two named characters with regulatory + institutional anchors: Lakshmi Reddy (Andhra Pradesh, BFSI) → Sabina Rahman (Bangladesh, Grameen-affiliated branch) in Ch1's connectivity scenario, and the as-yet-unmerged Petra Novak (Czech GDPR) was redirected to Hayoon Kim (Korean ISMS-P) in Ch3 §The Security Breach. Both passages were rewritten end-to-end. Surrounding prose was not re-read for integration smoothness.

## What you are reading for

Read Ch1 §The Connectivity Gradient (lines ~85–105) and Ch3 §The Security Breach (lines ~190–205) as a hostile reader checking three things only:

1. **Integration with surrounding prose** - does the new passage land in voice with the paragraphs before and after, or does it read as a graft? The Sabina passage sits between the global-connectivity-gradient framing paragraph and the Joel Reyes / GCC offshore passage. The Hayoon passage sits between the architectural §Security Breach framing and the §What the architecture introduces honestly transition.
2. **Institutional accuracy at sentence level** - Grameen-affiliated branches in Rangpur Division, *shotti'r khata* as Bangla idiom, KISA quarterly compliance bulletin, *Hankyoreh* as Korean daily, ISMS-P as the Korean compliance regime, PIPA Article 29 as the Korean equivalent of GDPR Article 32. Anything that reads as a Western writer guessing at the institutional texture should be flagged.
3. **King-style craft preservation** - every detail particular, time-stamps real, residual scarring named (Sabina's *shotti'r khata* binders; Hayoon's local encrypted drive). The original Lakshmi/Petra passages had craft moves; the swap should not have lost any.

## Deliverable

Apply edits directly to `vol-1/part-1-thesis-and-pain/ch01-when-saas-fights-reality.md` and `vol-1/part-1-thesis-and-pain/ch03-inverted-stack-one-diagram.md`. Do **not** commit - leave the working tree dirty per the 2026-04-29 commit-process directive (PAO commits chapter/manuscript changes; Yeoman edits). If a specific phrasing decision needs PAO judgment (e.g., whether to retain or replace a borrowed Bangla phrase), flag inline with `<!-- PAO: ... -->` and proceed with the rest of the audit.

Write a `yeoman-resumed-2026-05-01THH-MMZ-cast-swap-audit-complete.md` beacon when done with: (a) what you flagged, (b) what you edited directly, (c) what you left alone and why.

If you find no issues worth raising, that is also a valid result - say so explicitly in the resumed beacon. PAO will read your scan as the audit signal.
