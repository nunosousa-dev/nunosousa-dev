# Maintaining the profile

## Daily public telemetry

`.github/workflows/profile.yml` runs daily at 07:23 UTC, manually from the Actions tab, and when its workflow or updater changes on `main`. Scheduled runs use the default branch and GitHub may delay them. If this repository uses a different default branch, change the push branch filter too.

After pushing these files, enable Actions if prompted. The first run replaces the honest “Awaiting first sync” placeholder. You can also choose **Actions → Refresh public profile → Run workflow**.

The job needs permission to write repository contents with its built-in `GITHUB_TOKEN`. No personal access token or secret setup is required. Branch protections that forbid bot commits need an appropriate repository policy or a PR-based publishing workflow; this workflow does not bypass protections. GitHub may disable scheduled workflows after 60 days without repository activity; re-enable the schedule if needed.

`scripts/update-profile.py` uses **unauthenticated public endpoints** only. The checkout token is for committing, not fetching data. No private events or commit messages are published. It shows the public repository count and up to three supported recent events, deduplicated by UTC day, action, and repository. It does not claim to show all contributions. The events API has a limited historical window and may lag.

Failed requests or validation leave the last snapshot untouched. The timestamp lets readers see its age; no “online” or uptime claims are made. API rate limiting fails the run rather than replacing real data with invented metrics. The next daily or manual run can retry.

Only content inside `<!-- PROFILE:START -->` and `<!-- PROFILE:END -->` is replaced. Keep exactly one pair of markers, in that order. Edit everything outside them normally.

```sh
python3 -m unittest discover -s tests -v
python3 scripts/update-profile.py
```

The second command fetches current public data and updates the local README. It does not commit or push.

## Artwork

`assets/mission-control.png` is original, locally rendered artwork at 2× resolution, with source/provenance embedded in PNG metadata. No remote image service is needed to display the profile. The header links to the website; GitHub does not support independent hotspots inside a README image.

To regenerate, install Pillow in a development environment, then run:

```sh
python3 scripts/build-artwork.py
```

The script downloads the Chakra Petch SemiBold font from Google Fonts for rendering only. Its [SIL Open Font License](https://github.com/google/fonts/blob/main/ofl/chakrapetch/OFL.txt) applies to the font; the font itself is not shipped in this repository. There are no scheduled artwork generation dependencies.

## GitHub-specific limits

Disclosure panels use native `<details>` / `<summary>` and can be operated with a keyboard. They work without JavaScript. GitHub controls typography and light/dark styling outside the artwork. The fixed pale-aqua header is designed for both surrounding themes and contains no mandatory motion. Its essential introduction is repeated as real Markdown and image alt text.

There is deliberately no JavaScript, fake terminal input, private tracking, external stats widget, or project showcase. This is a profile README, not an embedded web application.
