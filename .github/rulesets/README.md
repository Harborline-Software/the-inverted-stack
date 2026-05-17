# GitHub Rulesets — the-inverted-stack

Source-of-truth JSON for the book repo's GitHub branch and tag rulesets.

## Files

| File | Target | Purpose |
|---|---|---|
| `main-branch.json` | `~DEFAULT_BRANCH` | Gate merges into `main` behind PR review + lightweight CI |
| `release-tags.json` | `refs/tags/v*` | Prevent deletion or rewriting of release tags (book editions) |

## How to apply

```bash
gh api -X POST repos/Harborline-Software/the-inverted-stack/rulesets \
  --input .github/rulesets/main-branch.json

gh api -X POST repos/Harborline-Software/the-inverted-stack/rulesets \
  --input .github/rulesets/release-tags.json
```

## Required checks

- **Lint PR commits** — `.github/workflows/commitlint.yml`
- **Scan workflows for banned triggers** — `.github/workflows/ban-pull-request-target.yml`

Book repo gates are deliberately light — the heavy lifting (audiobook renders,
chapter measurement) runs locally via Galley + OpenWolf and doesn't gate PRs.
