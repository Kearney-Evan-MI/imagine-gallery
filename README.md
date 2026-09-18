# Imagine Gallery

Personal library for Grok Imagine assets, consistent characters, prompts, and generation history.

**Live Gallery:**
https://kearney-evan-mi.github.io/imagine-gallery/

## Current Series: Green-Eyed Woman

Young woman with:
- Ash-brown / dark hair
- Vivid green eyes
- Fair freckled skin/chest
- Wide, joyful open-mouthed smile
- Outfit: turquoise/teal ribbed tank top + yellow skirt/shorts

### Key Assets (UUIDs from Grok Imagine)
- Original refs: `@8474ea85-0287-4877-a905-f0b848b40eea`, `@a4d36878-e1aa-4610-a567-0e1caf9e55fd`, `@6ef8dfcf-188a-48df-8f89-b3aae3867443`, `@0dce1ee3-8f0f-4363-a1e0-1a595f35a454`
- **Latest post set (2026-09-11):** `@ff0116d1-7647-49a9-a4a1-7c05b5e80c7f` — [Grok Imagine post](https://grok.com/imagine/post/ff0116d1-7647-49a9-a4a1-7c05b5e80c7f)
- Prior kneeling pose: `@6a1a0a3d-eca0-4f3b-b2f2-8752bdda856b` (and previous `@7f08a2b1-97cc-4d8e-bd88-62535eea6cc4`)

## Also active: New Forest Spunk

Hampshire / Solent outdoor lock (messy curly hair, freckles, soft smirk, heatwave jeans look). See `characters/new-forest-spunk/`.

## How to use with Grok
1. Tag the UUIDs or say “use the green-eyed woman from my imagine-gallery repo”
2. Re-upload the original 4 photos if needed for perfect face lock
3. Keep adding new generations here for version history
4. For restyles and phenotype-locked prompts, use the skills in `skills/` (start with `imagine-restyle`)

## Structure
- `characters/green-eyed-woman/` – bible, refs, prompts, gens
- `characters/new-forest-spunk/` – bible + version notes
- `sessions/` – dated chat logs
- `docs/` – GitHub Pages gallery source
- `skills/` – Grok Imagine prompt/restyle skills (canonical copies)
- `integrations/grok-imagine-toolkit/` – imported xAI Grok Imagine image/video toolkit

## Prompt / restyle skills

The gallery now keeps the Imagine prompt cluster under `skills/`:

- `skills/imagine-restyle` — identity-locked restyle of an existing frame or prompt
- `skills/photoreal-phenotype-prompts` — new photoreal prompt with a regional lock
- `skills/pretty-women-photorealism` — pretty without plastic/filter faces
- `skills/pg13-topless-photorealism` — new PG-13 documentary generation
- `skills/pg13-topless-restyle` — PG-13 restyle of an existing adult frame

Copy a skill folder into a Grok session at `/home/workdir/.grok/skills/<name>/` to load it.

## Grok Imagine toolkit

The referenced `pattalkslaw-del/grok-imagine-toolkit` release is included under
`integrations/grok-imagine-toolkit/` as a disjoint subtree, so it does not
overwrite the gallery's existing files. Its upstream MIT license and usage
documentation are included alongside the scripts.

The import source is commit
[`1013da76c74de1e2aa9fcde3583ef38dd2531910`](https://github.com/pattalkslaw-del/grok-imagine-toolkit/commit/1013da76c74de1e2aa9fcde3583ef38dd2531910).
Run the toolkit commands from that directory and configure `XAI_API_KEY`
locally; do not commit credentials.

## Enabling / deploying the Gallery Site

The site is built from the static files in `docs/` and deployed by [`.github/workflows/pages.yml`](.github/workflows/pages.yml) on every push to `main` that touches `docs/` (or via **Actions → Deploy GitHub Pages → Run workflow**).

**One-time repo setting (required once):**
1. Repo → **Settings** → **Pages**
2. Under **Build and deployment** → **Source**: choose **GitHub Actions**
3. Save. The next successful `Deploy GitHub Pages` run publishes
   https://kearney-evan-mi.github.io/imagine-gallery/

> Note: Private repositories require a paid GitHub plan for GitHub Pages. If the site doesn’t appear, either make the repo public or upgrade the account.

## Gallery performance
The GitHub Pages site under `docs/` is tuned for mobile load speed:
- Responsive Drive **thumbnail** URLs (`srcset` + `sizes`) instead of full-file `uc?export=view` links
- LCP preload + `fetchpriority="high"` on the hero image; lazy-load for the rest
- Explicit `width`/`height` and CSS `aspect-ratio` to avoid layout shift
- `content-visibility` / `contain` to reduce off-screen paint cost on long pages

For the best results, replace remote images with optimized local WebP/JPEG files in `docs/images/`.

### Local preview
Open `docs/index.html` in a browser, or serve the folder:

```bash
python3 -m http.server --directory docs 8080
```
