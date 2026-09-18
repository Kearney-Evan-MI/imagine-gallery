---
name: photoreal-phenotype-prompts
description: Create and rewrite high-quality photorealistic Grok Imagine prompts for women with preferred Northern Western and Southern European phenotypes. Trigger on requests to write or improve image prompts, lock phenotype (British, French, Dutch, North Italian, Southern English), avoid cartoon or Central European looks, apply advanced negative prompting, or refine candid portrait generation.
---

# Photoreal Phenotype Prompts

## Overview

Specialized prompt craft for Grok Imagine that produces photorealistic women matching specific European phenotypes while strongly suppressing cartoon, illustration, plastic, and Central European drift.

## Core Rules

Always prioritize positive photographic language over long negative lists. Grok Imagine responds weakly to pure negatives and can bias toward mentioned concepts.

### Required Prompt Structure (in order)

1. Subject + age + phenotype lock
2. Specific physical traits (hair, skin, face shape, eyes)
3. Clothing and exact pose/framing
4. Environment and lighting
5. Camera and photographic style (heaviest weight)
6. Skin and material realism anchors
7. Short negative closer

### Phenotype Locking

Use explicit regional language early:

- British / Southern English — "British Isles features", "Southern English phenotype", "refined English bone structure", "softer oval face", "Hampshire type", "Dorset type"
- Dutch — "Dutch features", "Northern European", "soft Nordic-adjacent bone structure"
- French — "French features", "refined Franco-European", "elegant Northern French bone structure"
- North Italian — "Northern Italian features", "Alpine Italian", "refined North Italian bone structure"

Always pair with face-shape language that counters Central European breadth:
- "softer oval face shape"
- "refined bone structure"
- "delicate jawline"
- "narrower midface"

Avoid vague "European" or "Caucasian".

### Strongest Photoreal Anchors

Place these early and repeat key ones if needed:

- photorealistic photograph / real unedited photo / candid photograph
- shot on Canon EOS R5 with 50mm f/1.4 (or iPhone 15 Pro natural photo)
- natural skin texture with visible pores and subtle imperfections
- realistic subsurface scattering
- fine individual hair detail
- realistic fabric folds and sheen
- unedited documentary style
- sharp focus on the eyes
- eye-level medium shot (or specify framing)

### Minimal Effective Negatives

Keep short and at the very end. Preferred set:

no cartoon, no anime, no illustration, no 3D render, no CGI, no plastic skin, no airbrushed skin, no beauty filter, no porcelain skin, no over-smoothed skin, no Central European features, no broad face, no text, no watermark

Do not write long negative lists. Prefer positive substitution (force pores and imperfections instead of only saying "no plastic skin").

### Phenotype-Specific Reference

For detailed keyword banks and example full prompts, load `references/phenotype-keywords.md`.

## Advanced Workflow (User-Refined)

Reserve the main prompt box for brand-new conceptual ideas only.

For style refinement and photoreal lift (especially portraits / pretty women):
- Use the conjunctive @image(-) functions heavily.
- Reference prior strong outputs to lift the general style toward Flux-level photorealism.
- After consistent training/usage this produces superior portrait results compared with pure text prompts.

When rewriting prompts, default to producing clean text prompts suitable for the main box on new ideas, while noting that the highest-quality final results usually come from combining them with @image referencing.

## Workflow

When the user asks to rewrite or create a prompt:

1. Identify the target phenotype from context or explicit request.
2. Extract clothing, pose, lighting, and setting.
3. Rebuild using the structure above with heavy photographic anchors.
4. Apply the phenotype lock and face-shape counters.
5. Close with the short negative set.
6. Offer one tightened variant and ask if further regional refinement is needed.
7. Remind that best final quality usually comes from feeding the result through @image style lift.
8. If the source is an existing image, hand off to imagine-restyle.
