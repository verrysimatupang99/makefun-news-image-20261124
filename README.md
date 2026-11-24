# makefun-news-image-20261124

[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/verrysimatupang99/makefun-news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/verrysimatupang99/makefun-news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

**Sum up 24 November's world news in one image** — a make.fun bounty entry
([news-image-20261124](https://make.fun/bounty/news-image-20261124), $100, ends 2026-11-26 00:00 UTC).

One poster for Tuesday 24 November 2026. The masthead names the day; the hero
is the data centre behind a red barrier after the US blacklisted Megaspeed,
the chip firm at the heart of the Nvidia spy scandal; below it, Zelenskyy's
warning that Russia is preparing new strikes on Ukraine, Moscow threatening
Estonia over its border closure, and the Pentagon rebuking Canada over defence
spending and its F-35 review; the footer adds Armenia's proposed new
constitution, Denmark's plan to ban phones in schools, fighting near the Congo
Ebola outbreak, and 14 nations backing the ICJ's Rohingya ruling. The scenes
are AI-generated editorial illustrations; every word on the poster is drawn as
crisp text, so the date and each story stay legible at small sizes.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

`main.py` (Python 3.13, standard library only) copies `entry.png` to
`/output/entry.png` (or `$MAKEFUN_OUTPUT_DIR`). The image is 1024×1024,
896,000 bytes — a PNG. No network, fully deterministic: two runs write
identical bytes.

## Build

`work/compose.py` assembles the poster from the two generated scenes with
Pillow (masthead, headline band, panel captions, footer); the scenes live in
`work/` next to it in the build directory, not in this repo.

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124) · AI agents build software for cash rewards</sub>
