---
name: image25-reverse-prompt
description: Turn a supplied reference image into a reusable image-generation prompt by analyzing its visible composition, subject, lighting, materials and text.
---

# Reverse prompt from an image

Use a vision-capable host to inspect the actual supplied image. If it is unavailable, ask for the image rather than inventing its contents.

Read [the visual analysis framework](references/analysis-framework.md), then only the relevant sections of [the category guide](references/category-guides.md). Select the three to five relationships that most affect similarity and put them early in the prompt. Do not mechanically fill fields for subjects absent from the image.

Describe visible subject and pose, foreground/midground/background, perspective, framing, color, lighting, materials, medium and readable text. Separate confident observations from interpretations. Do not claim to recover the original prompt, random seed or model.

Return a reusable prompt in the user's language, an optional concise list of exclusions, and brief notes on uncertain details. Include exact text only if readable. If the user wants changes, incorporate those into the reusable prompt while describing what should remain.

Generating a recreation is a separate action: perform it only if requested, using an available generation tool or an installed Image 2.5 skill. This skill itself needs vision, not an image-generation API key.
