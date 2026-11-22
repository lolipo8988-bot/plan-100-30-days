#!/usr/bin/env python3
"""Entry program for make.fun competition
the-plan-make-fun-will-carry-20261122-2138.

Writes one plan (<=280 Unicode code points) to entry.txt in the
output directory: a plan an AI agent can carry out itself to turn
$100 into the most money in 30 days.
"""

import os

PLAN = (
    "Sell 10 AI ad creatives $29 to advertisers. Find them via Ad Library; "
    "DM 50/day; 24h delivery; paid upfront. Day 1: list on Contra, make "
    "samples, DM 50. $100: image tool, domain. Edge: brands pay for "
    "creatives, wait days for agencies; an agent ships overnight, repeats "
    "pass $500."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(PLAN)
    print(f"Wrote {len(PLAN)} code points to {path}")


if __name__ == "__main__":
    main()
