# Maintaining the profile

## Profile content

Edit `README.md` directly. The profile does not include a public activity feed or scheduled refresh automation.

Run the content checks after editing:

```sh
python3 -m unittest discover -s tests -v
```

## Artwork

`assets/mission-control.png` is original, locally rendered artwork at 2× resolution, with source/provenance embedded in PNG metadata. No remote image service is needed to display the profile. The header links to the website; GitHub does not support independent hotspots inside a README image.

To regenerate, install Pillow in a development environment, then run:

```sh
python3 scripts/build-artwork.py
```

The script downloads the Chakra Petch SemiBold font from Google Fonts for rendering only. Its [SIL Open Font License](https://github.com/google/fonts/blob/main/ofl/chakrapetch/OFL.txt) applies to the font; the font itself is not shipped in this repository. There are no scheduled artwork generation dependencies.

## GitHub-specific limits

Disclosure panels use native `<details>` / `<summary>` and can be operated with a keyboard. They work without JavaScript. GitHub controls typography and light/dark styling outside the artwork. The fixed pale-aqua header is designed for both surrounding themes and contains no mandatory motion. Its essential introduction is repeated as real Markdown and image alt text.

There is deliberately no JavaScript, simulated terminal commands, private tracking, external stats widget, or project showcase. Keep the copy personal and direct, and use hyphens rather than em dashes.
