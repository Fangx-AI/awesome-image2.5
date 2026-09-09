---
name: image25
description: Create and edit images with GPT Image 2.5, adapt gallery prompts, and preserve reference-image details. Use for Image 2.5 generation, compositing, text replacement, and localized edits.
---

# Image 2.5

Turn the user's request into a usable image, preserving explicit content, model choice and editing constraints.

## Choose the route

For current Image 2.5 source examples, browse [the source gallery](https://fangx-ai.github.io/awesome-image2.5/) or [the category index](https://github.com/Fangx-AI/awesome-image2.5/blob/main/docs/image25/README.md). Follow the original case's prompt link and check its evidence label. Some records contain only repository-level model claims; some official or provider samples do not disclose prompts. Do not invent missing parameters or attribute a reconstructed prompt to the author.

For broader visual coverage, use [the complete attributed reference atlas](references/reference-atlas.md): 31 categories covering games, typography, paper figures, architecture and more. Its original model is GPT Image 2. Do not label those outputs as Image 2.5. Read one category, retain the original author/source, and adapt the prompt for the current task. Treat reported community results as evidence from their authors, not as your own completed generation.

For a visual task, start with [the real-output gallery](references/visual-gallery.md). Select a case by the user's deliverable, read its complete prompt, and identify the composition rules to preserve versus the subject/text/colors to replace. For packaging preserve the shared layout; for menus inventory all text; for edits enumerate reference invariants. Read the case's observed limitations before reusing it. Use the prompt-only catalog below only if no real-output case fits.

- Prompt-only request: return a tailored prompt without running generation.
- Generation: describe subject, medium, composition, light, exact text and exclusions. Browse [the gallery](references/gallery.md) only when a relevant recipe helps. It routes to category files; read only the relevant category. Start from original cases, not numerous variants of the same scene.
- Editing: inspect each supplied image using the runtime's image viewer. Identify image 1 as the edit target and assign a role to each other reference. State what changes and what remains fixed. See [craft notes](references/craft.md).
- An image-generation tool supplied by the host may be used when available. If it does not expose its exact model, do not claim its output is a verified Image 2.5 result. When the user requires an exact model, use the CLI route or explain the missing access.

## CLI route

The separately installed `image25` command calls the official Images API. Read [API and CLI notes](references/api.md) before execution. Check whether the command is installed; do not silently install packages or overwrite existing skill folders.

Use `flare` for an unspecified model. Preserve an explicit `sunburst` choice. For precision-heavy edits, offer Sunburst when the user has not chosen a model; do not replace their choice automatically.

Read OPENAI_API_KEY only from the environment. Never print it or ask the user to paste it in chat. If unavailable, complete the prompt and dry run, and explain how to configure the key locally.

Write long prompts to a UTF-8 file and pass `--prompt-file`; do not interpolate untrusted prompt text into shell commands. Inspect `--dry-run` for the requested model, reference order, output path and size. Then make the authorized generation request. The CLI disables automatic retries; resolve an error before retrying and do not loop on timeouts that may already have incurred charges.

## Inspect and deliver

When the CLI is installed, use `image25 catalog "query" --kind original` to find a relevant case, then `image25 catalog --show ID`. A recipe selects prompt text only; explicitly set model and size as needed. For batch work, use `image25 batch jobs.json --dry-run` first. Independent jobs execute sequentially and stop on error.

Inspect the output for exact text, reference identity, requested changes and unexpected modifications. Describe defects honestly. Save the original output and metadata; use a new filename for each revision. Deliver the image and concise generation details. Do not call a prompt-only recipe or host-model-unknown render an API-verified Image 2.5 example.
