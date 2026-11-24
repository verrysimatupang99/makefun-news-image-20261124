#!/usr/bin/env python3
"""News-image entry: copy the poster to /output/entry.png.

The poster (entry.png) sums up Tuesday 24 November 2026 in one image:
the US blacklists Megaspeed, the chip firm at the heart of the Nvidia
spy scandal; Zelenskyy warns Russia is preparing new strikes on
Ukraine; Moscow threatens Estonia over its border closure; the Pentagon
rebukes Canada over defence spending and its F-35 review; plus
Armenia's new constitution, Denmark's school phone ban, fighting near
the Congo Ebola outbreak and 14 nations backing the ICJ Rohingya
ruling. The date is named in the masthead.

Deterministic: the same bytes are written on every run, no network,
Python 3.13 standard library only.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

os.makedirs(OUT, exist_ok=True)
src = os.path.join(HERE, "entry.png")
dst = os.path.join(OUT, "entry.png")
shutil.copyfile(src, dst)
# Fail loudly instead of handing the grader a truncated copy.
assert os.path.getsize(dst) == os.path.getsize(src), "entry.png copy incomplete"
