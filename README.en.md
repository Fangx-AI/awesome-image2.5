# Awesome Image 2.5

A visual, source-backed collection for finding useful image-generation ideas.

[中文](README.md) · [Live gallery](https://fangx-ai.github.io/awesome-image2.5/) · [Browse categories](docs/image25/README.md) · [Quick start](docs/getting-started.md)

**146 Image 2.5 source records · 11 categories · 14 original demonstrations · 162 legacy learning cases**

Every Image 2.5 record includes images, author attribution, a source or prompt link, and the strength of its model evidence. The current collection contains 12 official examples, 10 provider claims, one author experiment with a command, four X author claims, and 119 community cases. These are not 146 independently reproduced experiments. Most community cases currently come from one author repository.

Browse the gallery, open a case, and follow the original prompt where it is available. Missing prompts and parameters are never invented. Images remain linked to their publishers and require network access.

## Generate and edit

```sh
uv tool install git+https://github.com/Fangx-AI/awesome-image2.5
image25 --prompt-file your-prompt.txt --model flare --dry-run
image25 --prompt-file your-prompt.txt --model flare -o output.png
```

Live API calls require your own locally configured `OPENAI_API_KEY`. See [installation and skills](docs/getting-started.md), [editing workflows](docs/workflows.md), and [quality checks](docs/quality.md).

The [14 original demonstrations](docs/original-gallery.md) include complete prompts, adaptation advice, and observed defects. Their host did not expose the exact model ID. The [162 legacy cases](docs/legacy-gallery.md), adapted from Wuyoscar's MIT-licensed GPT-Image2-Skill, remain explicitly labeled GPT Image 2.

## Maintain and contribute

```sh
python scripts/build_all.py
python -m unittest discover -s tests -v
```

Network collection is separate from deterministic offline page generation. Read the [source methodology](docs/research.md), [project architecture](docs/architecture.md), [contribution guide](CONTRIBUTING.md), and [third-party notices](THIRD_PARTY_NOTICES.md).

Community project; not affiliated with OpenAI. Third-party images and prompts retain their original rights.
