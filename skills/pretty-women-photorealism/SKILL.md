---
name: pretty-women-photorealism
description: Write and tighten photoreal Grok Imagine prompts for attractive adult women so they look like unedited camera photos, not filters, stock beauty, cartoon, or plastic AI faces. Trigger on pretty women photorealism, pretty photoreal, attractive candid portrait, film-grade pretty woman, make her prettier but real, or skill=pretty-women-photorealism. Use with photoreal-phenotype-prompts for regional locks. Prefer this for attractiveness-plus-realism quality control.
---

# Pretty Women Photorealism

## Overview

Quality-control layer for Grok Imagine prompts of adult women. Goal is a woman who reads as genuinely pretty in a real photograph — healthy, well-lit, camera-true — without beauty-filter skin, stock-model glaze, illustration, or Central European face drift.

Load photoreal-phenotype-prompts when a regional lock is needed. Load imagine-restyle when the source is an existing image. This skill only adds the pretty-plus-photoreal bar.

Never use for anyone described as under 18.

## When to use

- User asks for pretty / attractive / beautiful photoreal women
- A prior output looks AI-smooth, cartoon, stock, or Instagram face
- User wants film-grade candid prettiness rather than glamour retouch
- Combining attractiveness with a locked British, Dutch, French, or North Italian phenotype

## Core rule

Pretty is a photographic outcome, not a synonym list. Encode it with bone structure, skin truth, light, lens, and expression. Do not write gorgeous stunning beautiful supermodel perfect face. Those words pull plastic and stock.

## Required prompt order

1. Subject + adult age band + phenotype lock
2. Face and prettiness structure (oval, refined midface, specific eyes/mouth)
3. Hair as individual strands with natural parting
4. Body only as needed for the frame — keep proportional and unposed
5. Clothing, pose, and exact framing
6. Environment + light that flatters without studio glamour
7. Camera and photographic style (heaviest weight)
8. Skin and material realism anchors
9. Short negative closer

## Pretty without plastic

Use these positive substitutes instead of beautiful / stunning / perfect

- refined bone structure, softer oval face, delicate jawline, narrower midface
- clear even-toned skin with visible pores and tiny imperfections
- bright well-defined irises, sharp catchlights, natural lashes
- relaxed mouth, slight natural lip color, no overfilled look
- healthy color in cheeks and lips from light, not makeup cake
- fine baby hairs at the hairline
- proportioned features, quiet symmetry, no stretched beauty-filter spacing

Age default when unspecified — late 20s to early 30s. State the band explicitly.

## Photoreal anchors (required)

Place early and keep

- photorealistic photograph / real unedited photo / candid photograph
- shot on Canon EOS R5 with 50mm f/1.4 or 85mm f/1.4
- iPhone 15 Pro natural photo only when the brief is phone-candid
- natural skin texture with visible pores and subtle imperfections
- realistic subsurface scattering
- fine individual hair detail
- realistic fabric folds and sheen
- unedited documentary style
- sharp focus on the eyes
- eye-level medium shot unless the user specified another crop

Soft overcast daylight, high window light, or open-shade porch light usually beats hard noon sun and beauty-dish studio light for this look.

## Minimal negatives (end only)

no cartoon, no anime, no illustration, no 3D render, no CGI, no plastic skin, no airbrushed skin, no beauty filter, no porcelain skin, no over-smoothed skin, no Instagram face, no stock model, no Central European features, no broad face, no text, no watermark

Do not write long negative essays. Force pores and lens language instead.

## Workflow

1. Identify phenotype (default Southern English / British Isles if context matches prior work).
2. Identify the pretty register — candid pretty, film still pretty, quiet smile, or conversational face. Default to candid, not posed glamour.
3. Rebuild the prompt in the required order.
4. Keep clothing and setting from the user request. Do not invent lingerie or glamour posing unless asked.
5. Offer one tightened variant.
6. If a prior strong frame exists, note that @image style-lift plus this prompt beats a cold text prompt.

## Route related work

- Regional lock language — photoreal-phenotype-prompts and its phenotype-keywords reference
- Edit an existing image while keeping identity — imagine-restyle
- New-generation PG-13 topless photoreal prompts — pg13-topless-photorealism
- Natural PG-13 topless of an existing adult frame — pg13-topless-restyle
- Example banks and camera recipes — imagine-restyle/references/phenotype-keywords.md and pg13-topless-photorealism/references/pg13-topless-recipes.md

## Anti-patterns

- Do not stack beautiful stunning gorgeous perfect flawless
- Do not use vague European or Caucasian
- Do not default to beauty-dish, wet look, arched-back glamour, or looking-at-camera seduction
- Do not widen the midface or allow Central European drift
- Do not omit camera + pore language
- Do not describe minors
