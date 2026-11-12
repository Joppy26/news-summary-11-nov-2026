#!/usr/bin/env python3
"""news-summary-01 entry: write the summary of the world's news of
Wednesday 11 November 2026 to /output/entry.txt.

Pure Python 3.13 standard library. Deterministic: the same bytes on every
run. No network, no clock, no files outside this repository.
"""

import os

SUMMARY = """World news, Wednesday 11 November 2026.

Ukraine and Russia ended a second day of United States mediated talks in Abu Dhabi without a peace deal, after Kyiv rejected a United States proposal on unoccupied parts of Donbas, the AP reported. Ukraine said it damaged five oil tanks at Russia's Ust Luga terminal, while a Russian strike on a Chornomorsk market killed three people and wounded 11.

The United States Justice Department charged three men it calls Iranian backed operatives with plotting nearly 20 attacks in Europe and the United States, including one on RAF Fairford in England. President Donald Trump said the war with Iran was "effectively over" militarily. Treasury Secretary Scott Bessent moved to a military base after threats, the New York Times reported.

Wall Street rallied with the bond market shut for Veterans Day. The Nasdaq rose 1.6 percent to 25,466, the S&P 500 rose 1.3 percent to 7,619 and the Dow added 0.5 percent to 52,486, led by CoreWeave, up almost 25 percent after revenue of 3.66 billion dollars beat forecasts. Traders fully priced a Federal Reserve rate rise in December.

World leaders opened the COP31 climate summit in Antalya, where 102 heads of state and government gathered and hosts proposed electricity meet 35 percent of world energy demand by 2035. China said its trade surplus passed 1.04 trillion dollars in the first 10 months of the year.

The House voted 211 to 204 to send a resolution to impeach Defense Secretary Pete Hegseth to committee, ending the effort. British police arrested a 41 year old United States Army officer on suspicion of spying for Russia. Anthropic offered 825 million shares at 70 to 78 dollars, a sale that would raise up to about 64 billion dollars before a planned Nasdaq listing on Thursday.

Spain held its first general strike in 14 years over housing, Delhi's air stayed poor after Diwali at an index of 299, and Victor Wembanyama scored 32 points as San Antonio beat Chicago 124 to 119 in the NBA.
"""


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(SUMMARY)


if __name__ == "__main__":
    main()
