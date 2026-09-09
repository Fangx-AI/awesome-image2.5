# Prompt craft

## New images

Use concrete visual instructions: subject → setting → composition → light/material → exact text → exclusions. Keep API controls (model, size, quality, format) separate from prompt prose. For typography, quote every requested string and specify hierarchy, placement and line breaks.

## Edits

Use a small change contract:
- Change: the specific object, material, lighting or text.
- Preserve: identity, pose, geometry, crop, camera, other objects and untouched text.
- Integrate: match perspective, occlusion, light direction and contact shadows.

For multiple references, explicitly name each image's role. A mask's transparent region requests regeneration; opaque areas request preservation. The mask is guidance, not a guarantee of pixel-perfect locking. Inspect boundaries and unchanged regions after generation.

## Reverse prompting

A visual description cannot recover the original hidden prompt or model settings. Describe visible evidence and label uncertain properties as interpretations. Keep readable text verbatim; never invent text obscured in the image.

## Iteration

Compare one targeted change at a time. Reuse the previous image as the edit target when continuing an edit. Keep the full preservation contract in the revised prompt. For charts or scientific figures, use supplied facts only and verify labels and relationships; a visually plausible diagram is not evidence.
