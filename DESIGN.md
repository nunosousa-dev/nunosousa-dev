---
name: Nuno Sousa - Personal Mission Control
description: Authored instrument-panel artwork paired with GitHub-native Markdown.
colors:
  ground: "#d6f1e8"
  ink: "#123e3c"
  rule: "#87b6a8"
  signal: "#c44422"
typography:
  artwork-display:
    fontFamily: "Chakra Petch"
    fontSize: "108px"
    fontWeight: 600
  artwork-title:
    fontFamily: "Chakra Petch"
    fontSize: "27px"
    fontWeight: 600
  artwork-descriptor:
    fontFamily: "Chakra Petch"
    fontSize: "24px"
    fontWeight: 600
  artwork-subtitle:
    fontFamily: "Chakra Petch"
    fontSize: "20px"
    fontWeight: 600
  artwork-label:
    fontFamily: "Chakra Petch"
    fontSize: "18px"
    fontWeight: 600
  artwork-caption:
    fontFamily: "Chakra Petch"
    fontSize: "12px"
    fontWeight: 600
components:
  mission-control-artwork:
    backgroundColor: "{colors.ground}"
    textColor: "{colors.ink}"
    width: "1800px"
    height: "720px"
---

# Design System: Nuno Sousa - Personal Mission Control

## Overview

**Creative North Star: "Personal Mission Control"**

A pale aqua instrument panel gives this profile an authored, technical identity: oversized geometric lettering, deep petrol ink, measured orbital marks, and one orange routing signal. The finished artwork is calm and static, not a simulated live dashboard.

The system has two ownership boundaries. `scripts/build-artwork.py` controls the raster nameplate; GitHub controls the Markdown typography, theme, spacing, links, tables, and disclosure states around it. Tokens above describe only the artwork, not a README stylesheet.

**Key Characteristics:**
- Original, flat instrument-panel artwork.
- Dominant name lettering with restrained routing detail.
- Native, keyboard-operable disclosures and real links.
- Static imagery with honest public-data snapshot language.

Evidence: `README.md`, `assets/mission-control.png`, `scripts/build-artwork.py`, and the six desktop/mobile/dark review captures, including expanded states. Captures approximate GitHub locally; they do not verify live GitHub sanitization. The approved direction is recorded in `.impeccable/surface-briefs/profile.md`; product constraints remain in `PRODUCT.md`.

## Colors

The artwork pairs cool instrument materials with one warm point of emphasis; GitHub's page and link colors are deliberately outside this palette.

Sidecar tonal ramps are synthesized panel previews only, not additional shipped colors or an approved palette expansion. The four frontmatter colors remain normative.

### Primary
- **Signal orange (`signal`):** the filled SHIP node; a compositional accent, never a service-health indicator.

### Neutral
- **Pale aqua ground (`ground`):** opaque artwork field and the interior of outlined nodes; unchanged between host themes.
- **Deep petrol ink (`ink`):** lettering, crosshair accents, name divider, and node outlines.
- **Calibration green (`rule`):** orbital rings, calibration ticks, and the footer rule; supporting geometry rather than body text.

**The Signal Is Not Status Rule.** The orange node belongs to the illustration; public activity is a snapshot, not evidence of live service health.

## Typography

The artwork uses Chakra Petch SemiBold, rasterized from the Google Fonts TTF; it has no runtime webfont dependency or fallback. Its angular forms supply the instrument character. Font sizes in frontmatter are drawing coordinates on the logical canvas (900 × 360); rendering at scale 2 doubles those values in the PNG, and display scaling reduces them proportionally.

- **Display:** the two-line name.
- **Title / subtitle:** CODE / TO CLOUD in the orbit centre.
- **Descriptor:** AI platforms, cloud, and DevOps beneath the name divider.
- **Label:** BUILD, SHIP, and RUN around the orbit.
- **Caption:** mission-control and location annotations along the bottom rule.

Outside the artwork, headings, paragraphs, and bold emphasis use GitHub's native styles. No local body-font, line-height, tracking, or type-scale tokens are asserted.

**The Native Type Rule.** Keep essential information and interactive labels in real Markdown; do not make raster annotations the sole source of profile facts.

## Layout

The nameplate is a single opaque PNG (1800 × 720, aspect ratio 5:2), drawn on a logical canvas (900 × 360). Large name lettering occupies the left; concentric routing geometry occupies the right. Name text begins at x=36; descriptors and their divider align at x=42. The orbit centres at (694, 156), with radii of 105 and 72 logical pixels. These are artwork coordinates, not CSS spacing tokens.

The README image uses `width="100%"`; its composition scales intact rather than reflowing. Below it, a centred three-link paragraph can wrap, followed by ordinary single-column Markdown. Command summaries wrap naturally, and expanded panels expose headings, prose, lists, and tables in document flow. GitHub owns container width, table overflow, margins, and breakpoints; the repository defines no custom responsive CSS or spacing scale.

Small orbital captions are secondary at mobile scale; identity and role remain available in the image alt text and visible introduction. Check narrow widths with disclosures both closed and expanded rather than treating the desktop composition as proof of mobile readability.

## Elevation & Depth

The authored artwork is flat: no shadows, gradients, glass, or layered cards. Fine rules, concentric circles, and outlined nodes provide structure without simulated elevation. Host-provided code backgrounds, table fills, and focus outlines are native GitHub treatments, not local elevation tokens. Imagery has no animation, pulsing, or motion dependency.

## Shapes

A square-edged rectangular artwork field contains circular instrument geometry. Rules and ticks use a single logical-pixel stroke; outlined nodes use a double stroke and a seven-pixel radius. Calibration marks repeat every 15 degrees, with longer marks every 45 degrees. These measured marks are intentional instrument material, not ornamental UI icons. There is no project-defined corner-radius scale.

## Components

### Mission-control nameplate
An original linked image, not a stats widget. Preserve the authored proportions, palette, oversized name, orbital diagram, and metadata provenance. The website link and descriptive `alt` text remain real HTML in `README.md`; there are no hover or focus styles baked into the PNG.

### Profile disclosures
Each native `<details>` starts closed and has a `<summary>` with a short, bold, plain-language label. Multiple panels may remain open independently. Native markers, keyboard activation, focus indication, and expanded-state behavior belong to the browser/GitHub. The README uses personal language rather than simulated commands.

### Navigation, tables, and telemetry
The centred navigation uses real anchors separated by slashes. A visible Markdown table puts the current toolchain first, followed by a short list of planned writing topics. Secondary disclosures hold earlier work, personal-project tools, and credentials, not custom cards. Recent activity is a separate Markdown region with an honest first-sync empty state and a public-activity link; daily automation populates that region rather than animating the illustration. The project-showcase exclusion is a surface requirement in `PRODUCT.md`, not a reusable visual component rule.

## Do's and Don'ts

### Do:
- **Do** regenerate the artwork from its Python source and preserve PNG provenance metadata.
- **Do** keep profile facts, navigation, command explanations, and telemetry readable as real text.
- **Do** preserve native disclosure markers, keyboard behavior, and visible focus.
- **Do** check narrow and wide layouts, light and dark hosts, and expanded disclosures.

### Don't:
- **Don't** claim project CSS controls GitHub's typography, colors, layout, or focus styles.
- **Don't** turn the orange routing node or a daily snapshot into a live-health claim.
- **Don't** add animated imagery or require motion to understand the profile.
- **Don't** treat locally approximated GitHub previews as live sanitizer verification.
