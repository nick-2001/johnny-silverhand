<div align="center">

# Johnny Silverhand

A Relic hologram companion for Codex.

Realistic bust · Silver cyberarm · Cyan glitch effects

<img src="archive/v2-workbench/qa/previews/idle.gif" alt="Johnny Silverhand idle animation" width="192" height="208">

**9 animations · 57 frames · v1 sprite format**

[Install](#install) · [Preview](#preview) · [Project layout](#project-layout)

</div>

## Install

On macOS, run these commands from the repository root:

```sh
mkdir -p "$HOME/.codex/pets/johnny-silverhand"
cp johnny-silverhand/{pet.json,spritesheet.png} "$HOME/.codex/pets/johnny-silverhand/"
```

Refresh the Codex pet picker and select **强尼·银手** (Johnny Silverhand). Restart Codex if needed. This replaces any existing installation with the same ID; loading in the app has not yet been verified.

To rename your companion, edit `displayName` in [pet.json](johnny-silverhand/pet.json).

## Preview

Open [preview.html](preview.html) locally in your browser to view every animation, pause playback, adjust speed, and switch backgrounds.

The current package uses the corrected **v1** spritesheet. Experimental v2 gaze animations remain unfinished in the archive.

<details>
<summary>Animation specifications</summary>

1536 × 1872 RGBA spritesheet · 8 columns × 9 rows · 192 × 208 pixels per frame.

| Row | Animation | Frames |
| ---: | --- | ---: |
| 0 | Idle | 6 |
| 1 | Move right | 8 |
| 2 | Move left | 8 |
| 3 | Wave | 4 |
| 4 | Projection activation (jump) | 5 |
| 5 | Error | 8 |
| 6 | Waiting | 6 |
| 7 | Working | 6 |
| 8 | Review | 6 |

The September 15, 2026 alignment fix keeps all 57 active frames inside their cells; the remaining 15 cells are transparent.

</details>

## Project layout

| Path | Contents |
| --- | --- |
| [johnny-silverhand/](johnny-silverhand/) | Installable manifest and spritesheet |
| [preview.html](preview.html) | Standalone animation viewer |
| [assets/source/](assets/source/) | Original character artwork |
| [docs/prompts/](docs/prompts/) | Image generation prompts |
| [archive/](archive/) | Earlier designs, v2 experiments, and historical QA |

## Credits

A personal fan project inspired by Johnny Silverhand from *Cyberpunk 2077*. Character and brand rights belong to their respective owners. No open-source license is included.

Format references: [codexpets](https://github.com/ApurvK032/codexpets) and [codex-pets](https://github.com/senyo888/codex-pets). No character artwork was copied from these projects.
