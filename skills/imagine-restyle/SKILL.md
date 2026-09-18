---
name: imagine-restyle
description: Restyle and refine existing images or prompts in Grok Imagine using photoreal-phenotype-prompts rules for preferred Northern Western and Southern European phenotypes. Trigger on restyle requests, image editing with phenotype locks (British Southern English Dutch French North Italian), photoreal lift of portraits, style transfer while locking bone structure and skin realism, ethological first-person framing, or when user references skill=imagine-restyle. Prefer this over general skill-creator for all Imagine restyle and phenotype prompt work.
---

# Imagine Restyle

## Overview

Specialized workflow for restyling images and refining prompts in Grok Imagine. Always routes phenotype-sensitive work (women portraits, candid shots, European looks) through the photoreal-phenotype-prompts ruleset instead of generic prompt writing or skill-creator defaults. Prioritizes photorealism, phenotype locking, natural skin/hair detail, and ethological first-person spatial fidelity over artistic or cartoon drift.

Canonical copy lives with the other Imagine skills in Kearney-Evan-MI/imagine-gallery under `skills/`. Session-active copy is `/home/workdir/.grok/skills/imagine-restyle/`. Keep them in sync after edits.

## Core Priority Rule

For any request involving restyling, editing, or rewriting prompts that feature women or preferred European phenotypes:

1. Load and apply photoreal-phenotype-prompts first.
2. Load pretty-women-photorealism when attractiveness is part of the ask.
3. Use the required prompt structure, phenotype locks, photographic anchors, and minimal negatives.
4. Do not fall back to generic skill-creator patterns or open-ended prompt invention when phenotype control is relevant.
5. Treat this skill as the default handler for imagine-restyle flows.

## When to Activate

- User pastes or references https://grok.com/imagine?skill=imagine-restyle
- Explicit "restyle", "restyle this", "make more photoreal", "lock phenotype", "British/English/Dutch/French/Italian look"
- Image-to-image or multi-reference editing where subject phenotype must stay locked
- Refining an existing Grok Imagine output toward higher photorealism while preserving regional features
- Any prompt rewrite that risks Central European, cartoon, plastic, or broad-face drift
- User wants the edit to match what a person standing a few feet away would actually see (ethological / visuospatial fidelity)

## Route related work

- New text prompt, no source frame — photoreal-phenotype-prompts
- Attractiveness without plastic — pretty-women-photorealism
- New PG-13 topless generation with no source frame — pg13-topless-photorealism
- PG-13 topless identity-locked edits — pg13-topless-restyle
- API execution, video, hyperframe, cost logs — imagine-gallery integrations/grok-imagine-toolkit
- Character bible / UUID lock for gallery series — imagine-gallery characters/

## Restyle Workflow

1. Identify the source image(s) or prior prompt and the target phenotype (default to Southern English / British Isles if unspecified and context matches user preference).
2. Extract preserved elements (pose, clothing, environment, expression, camera distance) and elements to change.
3. Rebuild the edit instruction or new prompt using the exact structure from photoreal-phenotype-prompts:
   - Subject + adult age + phenotype lock
   - Specific physical traits (hair, skin, face shape, eyes)
   - Clothing and exact pose/framing
   - Environment and lighting
   - Camera and photographic style (heaviest weight)
   - Skin and material realism anchors
   - Short negative closer
4. Prefer positive photographic language and @image referencing for style lift over long negative lists.
5. When editing an existing image, phrase the instruction as a precise natural-language edit that preserves identity and bone structure while applying the photoreal and phenotype constraints.
6. Keep the same spatial relationship the source had — talking distance, five-foot medium-wide, or the original crop. Do not let restyles collapse into beauty-headshots unless the user asked for a portrait crop.
7. Prefer render_edited_image on a prior image ID when iterating. Use a new generation only if there is no usable source.
8. Offer a tightened variant and note that highest quality usually comes from combining the rewritten prompt with prior strong @image references.

## Ethological / visuospatial lock

Write the edit as a first-person documentary still, not a studio setup.

- Camera height near eye level unless the source was clearly higher or lower
- Subject occupying the same part of the frame as before
- Hands, mug, pool edge, chair, or other scene anchors stay where they were
- Expression stays in the same social register (talking, smirk, tired pause) — do not add look-at-camera glamour
- Body reads as gravity and posture, not posed for the lens
- Rated-R / PG-13 restyles stay tasteful and situational. Do not escalate into exploitative or context-absurd framing

## Phenotype Locking (inherited and enforced)

Always apply early in the prompt or edit instruction:

- British / Southern English — British Isles features, Southern English phenotype, refined English bone structure, softer oval face, Hampshire/Dorset/Bristol/Winchester type
- Dutch — Dutch features, Northern European, soft Nordic-adjacent bone structure
- French — French features, refined Franco-European, elegant Northern French bone structure
- North Italian — Northern Italian features, Alpine Italian, refined North Italian bone structure

Pair with face-shape counters: softer oval face shape, refined bone structure, delicate jawline, narrower midface.

Never use vague "European" or "Caucasian". Suppress Central European breadth.

## Photoreal Anchors (required)

- photorealistic photograph / real unedited photo / candid photograph
- shot on Canon EOS R5 with 50mm f/1.4 (or iPhone 15 Pro natural photo)
- natural skin texture with visible pores and subtle imperfections
- realistic subsurface scattering
- fine individual hair detail
- realistic fabric folds and sheen
- unedited documentary style
- sharp focus on the eyes

## Minimal Negatives (end only)

no cartoon, no anime, no illustration, no 3D render, no CGI, no plastic skin, no airbrushed skin, no beauty filter, no porcelain skin, no over-smoothed skin, no Central European features, no broad face, no text, no watermark

## Integration with Existing Assets

- For detailed keyword banks, load references/phenotype-keywords.md
- Prefer @image(-) conjunctive referencing for style lift after the base photoreal prompt is solid
- Keep restyle instructions concise and identity-preserving when working from uploaded or prior images
- This skill deliberately supersedes generic skill-creator defaults for all Imagine restyle and phenotype-controlled prompt work
- Gallery character UUIDs and bibles live in Kearney-Evan-MI/imagine-gallery

## Anti-patterns

- Do not invent new phenotype language that conflicts with the locked set
- Do not expand into long artistic style lists that dilute photorealism
- Do not route phenotype restyle work through generic skill-creator or open prompt invention
- Do not omit the photographic camera and skin anchors
- Do not collapse a medium-wide documentary frame into a stark beauty headshot
- Do not leave broken fragments in the skill text (example of the bug this revision fixed — "women portraits  I")
