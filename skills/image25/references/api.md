# Image 2.5 API / CLI

Verified against official documentation on 2026-09-09:
- [Flare model](https://developers.openai.com/api/docs/models/gpt-image-2.5-flare)
- [Sunburst model](https://developers.openai.com/api/docs/models/gpt-image-2.5-sunburst)
- [Image generation guide](https://developers.openai.com/api/docs/guides/image-generation)

Model IDs: `gpt-image-2.5-flare` and `gpt-image-2.5-sunburst`. CLI aliases: `flare`, `sunburst`.
Quality: `auto low medium high xhigh max`. Flare targets everyday speed; Sunburst emphasizes editing precision.

The CLI calls `images.generate` for text-only input and `images.edit` when any `-i` is supplied. Repeat `-i` for multiple references. `--mask` applies to the first image, must be PNG with alpha and matching dimensions. Transparent pixels identify the edit region.

```sh
image25 --prompt-file prompt.txt --model flare -o generated/draft.png
image25 --prompt-file edit.txt --model sunburst -i base.png -i reference.png -o generated/edit.png
image25 --prompt-file edit.txt -i base.png --mask mask.png -o generated/masked.png
image25 -p "A ceramic toy fox, isolated" --background transparent -o generated/fox.png
```

`--size` accepts `auto` or dimensions: multiples of 16, longest edge <=3840, ratio <=3:1, pixel count 655360–8294400. Common choices: 1024x1024, 1536x1024, 1024x1536. Above 2560x1440 is experimental per the guide.
`--format`: png / jpeg / webp. Transparent output requires png or webp.
`--quality` defaults to auto. Only one result is requested per invocation.
`--dry-run` validates local inputs and prints the request without network access.

Install separately with `uv tool install git+https://github.com/Fangx-AI/awesome-image2.5`.
Only the process environment's OPENAI_API_KEY is read. The endpoint is fixed to https://api.openai.com/v1.
Output filenames must match the format. Existing files are never overwritten. Each image gets a .json sidecar containing the prompt, requested model and parameters; inspect it before publishing private prompts.
No live access is implied by installation. A billed API request needs valid account access. Host image tools may use a different backend and do not test this CLI.
