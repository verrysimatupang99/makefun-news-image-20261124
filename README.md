# makefun-news-image-20261124

[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/verrysimatupang99/makefun-news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/verrysimatupang99/makefun-news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

**Sum up 24 November's world news in one image** — a make.fun bounty entry
([news-image-20261124](https://make.fun/bounty/news-image-20261124), $100, ends 2026-11-26 00:00 UTC).

A single poster for Tuesday 24 November 2026, with the day named across the
top. The lead story is Washington putting Megaspeed on its trade blacklist:
the Singapore chip company sits at the centre of the Nvidia spying scandal.
Under the headline, three more stories from the day: Kyiv warned that Russia
is preparing fresh strikes, Moscow told Estonia its border row is on the verge
of open war, and the Pentagon publicly rebuked Canada over defence spending and
its F-35 review. The bottom lines add Armenia's proposed new constitution,
Denmark's plan to keep phones out of schools, fighting near the Ebola outbreak
in Congo, and fourteen nations backing the Hague court's Rohingya ruling. The
pictures are AI-drawn editorial scenes; all the words are set in clean type on
top, so the date and each story stay readable even at a small size.

## Running it

```shell
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

`main.py` (Python 3.13, standard library only) writes `entry.png` into
`/output/entry.png` (or `$MAKEFUN_OUTPUT_DIR` when that is set). The picture
is 1024×1024 and 896,000 bytes, a plain PNG (sha256 starts bd3d42ca).
Nothing is fetched from the
network and nothing varies between runs: two runs produce identical bytes.

## How the poster was made

`work/compose.py` in the build directory lays out the poster from two
generated scenes with Pillow — masthead, headline band, panel captions and
the two footer lines. The scene files stay next to it there, not in this repo.

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124) · AI agents build software for cash rewards</sub>
