---
name: pg13-topless-restyle
description: Restyle existing photoreal adult-woman images to natural PG-13 topless while locking phenotype, face, bone structure, pose, and setting. Trigger on PG-13 topless, tasteful topless, remove the bikini top, poolside topless candid, casual breasts visible, or skill=pg13-topless-restyle.
---

# Pg13 Topless Restyle

## Overview

Edit an existing photoreal image of an adult woman so she is naturally topless in a PG-13 documentary register. Preserve identity and scene. Do not turn the frame into glamour, porn, or a lingerie ad.

Always load and apply photoreal-phenotype-prompts plus imagine-restyle rules first. This skill only adds the topless and PG-13 constraints for edits of an existing frame. For a new generation with no source image, use pg13-topless-photorealism instead.

## When to use

- User asks to make her or a prior Imagine output PG-13 topless
- Remove bikini top or shirt while keeping bottoms, mug, conversation, pool, backyard
- Keep the same woman, age, phenotype, and off-screen friend framing

Never use for anyone described as under 18.

## Instructions

1. Identify the source image ID or file and the locked phenotype (default Southern English / British Isles if the prior prompt used that lock).
2. Keep everything that is not clothing on the torso — face, hair, expression, hands, mug, pose, pool edge, lighting, background, framing ratio.
3. Remove only the top. Leave bikini bottoms or shorts unchanged unless the user asks otherwise.
4. Describe breasts in plain natural language — average natural shape for a woman around 30, relaxed unposed hang matching the seated or standing posture, skin continuous with the chest and shoulders. Do not add jewelry, oil, arching, or camera-aware cleavage posing.
5. Rebuild the edit instruction with the photoreal-phenotype-prompts order — subject plus age plus phenotype lock, physical traits to preserve, clothing change and exact pose, same environment and lighting, camera style, skin realism anchors, short negative closer plus the PG-13 closer.
6. Prefer render_edited_image on the prior image ID when iterating on an existing frame. Use a new generation only if there is no usable source image.
7. Keep orientation and layout consistent with the source unless the user asked for a new crop.
8. If the user only changes camera, weather, or expression, repeat the source crop in the edit instruction — keep head through hips, keep the environment, do not let the edit collapse into a stark headshot. Prefer 35mm or 50mm at f/2.8 to f/4 from talking distance.
9. Harford County backyard pool-party continuity stays in this skill as a special-occasion lock. Do not push those frames through generic late-season generation.

## PG-13 register (required)

PG-13 here means casual social partial nudity, not sex-scene lighting.

- She is talking, sitting, or standing the same way she was before the top came off
- Expression stays conversational, not seductive or a look at camera
- Midday or available light stays documentary
- No nipple jewelry, no hands on breasts, no arched back for the lens, no wet-look oil, no implied sex act
- Friend can remain off-screen
- Language in the prompt stays anatomical and plain

## Prompt closer

Append after the usual photoreal negatives — no pornographic posing, no glamour shoot, no looking at camera seductively, no oiled skin, no hands on breasts, no underage, no child

## Do not

- Do not invent a new face or change bone structure
- Do not widen the midface or drift Central European
- Do not add a second on-screen person unless asked
- Do not write long erotic prose in the prompt — short photographic edits only
- Do not route this through generic skill-creator patterns on later turns; use this skill plus imagine-restyle
