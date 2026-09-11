---
name: image25
description: Create and edit images with GPT Image 2.5, adapt gallery prompts, and preserve reference-image details. Use for Image 2.5 generation, compositing, text replacement, and localized edits.
---

# Image 2.5

Turn the user's request into a usable image, preserving explicit content, model choice and editing constraints.

## Choose the route

Start with the bundled [31-category atlas](references/gallery.md). Choose by the requested deliverable, read the matching category file, and inspect the actual prompt before adapting it. Each category includes a practical writing brief, checks, source images and attributed legacy prompts. Usually read one category; combine two or three only for hybrid requests. Do not load the whole atlas or send the user to a website as the default workflow.

The category files distinguish current Image 2.5 source claims, our host-model-unknown demonstrations, original prompt-only practice briefs and GPT Image 2 references. Preserve those distinctions. Some authors disclose no complete prompt or only a repository-level model claim; do not invent missing settings or attach a practice prompt to an unrelated image as its original prompt.

When a task matches one of our demonstrations, use [the real-output case index](references/visual-gallery.md) to find its complete prompt and observed limitations. Preserve composition rules while adapting subject, text and colors. For edits inspect the linked input as well as the result. This is an optional companion to the category atlas, not a second mandatory starting point.

- Prompt-only request: return a tailored prompt without running generation.
- Generation: set canvas and layout, then subject, medium, light, exact text and targeted exclusions. Read [craft notes](references/craft.md) for dense text, UI, multi-panel consistency, technical diagrams or prompt repair. Use the [prompt-only lab](references/prompt-lab-index.md) when no actual case fits; its variants are not independently generated examples.
- Editing: inspect each supplied image using the runtime's image viewer. Identify image 1 as the edit target and assign a role to each other reference. State what changes and what remains fixed. See [craft notes](references/craft.md).
- An image-generation tool supplied by the host may be used when available. If it does not expose its exact model, do not claim its output is a verified Image 2.5 result. When the user requires an exact model, use the CLI route or explain the missing access.

## CLI route

The separately installed `image25` command calls the official Images API. Read [API and CLI notes](references/api.md) before execution. Check whether the command is installed. Installing this Skill does not install the CLI or download repository assets: examples using `assets/` paths assume a repository checkout. Otherwise save the prompt and references into the user's working directory and use those actual paths. Respect existing installation authorization and preserve user changes.

Use `flare` for an unspecified model. Preserve an explicit `sunburst` choice. For precision-heavy edits, offer Sunburst when the user has not chosen a model; do not replace their choice automatically.

Read OPENAI_API_KEY only from the environment. Never print it or ask the user to paste it in chat. If unavailable, complete the prompt and dry run, and explain how to configure the key locally.

Write long prompts to a UTF-8 file and pass `--prompt-file`; do not interpolate untrusted prompt text into shell commands. Inspect `--dry-run` for the requested model, reference order, output path and size. Then make the authorized generation request. The CLI disables automatic retries; resolve an error before retrying and do not loop on timeouts that may already have incurred charges.

## Inspect and deliver

When the CLI is installed, use `image25 catalog "query" --kind original` to find a relevant case, then `image25 catalog --show ID`. A recipe selects prompt text only; explicitly set model and size as needed. For batch work, use `image25 batch jobs.json --dry-run` first. Independent jobs execute sequentially and stop on error.

Inspect the output for exact text, reference identity, requested changes and unexpected modifications. Describe defects honestly. Save the original output and metadata; use a new filename for each revision. Deliver the image and concise generation details. Do not call a prompt-only recipe or host-model-unknown render an API-verified Image 2.5 example.
