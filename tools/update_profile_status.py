#!/usr/bin/env python3
"""Rewrite the profile's status section from a public checkout. Rerunnable.

Usage: python3 tools/update_profile_status.py <public-checkout> <YYYY-MM-DD>   (run from the repo root)
Reads generated/index.json and generated/evidence-index.json of the checkout
and rewrites everything between the two status markers in profile/README.md:
the "Status on <date>" heading, the profile and source family counts, the
public commit, the freshness window, and the count of observations verified
on a phone. Fails loudly if a marker is not found exactly once or the two
files disagree on the profiles.
"""
import json
import subprocess
import sys
import textwrap

START = "<!-- status:start (tools/update_profile_status.py rewrites this block) -->"
END = "<!-- status:end -->"
PROFILE = "profile/README.md"
PUBLIC_URL = "https://github.com/open-carrier-data/open-carrier-data"

pub, day = sys.argv[1], sys.argv[2]
commit = subprocess.run(["git", "-C", pub, "rev-parse", "HEAD"], capture_output=True, text=True, check=True).stdout.strip()
index = json.load(open(f"{pub}/generated/index.json", encoding="utf-8"))
evidence = json.load(open(f"{pub}/generated/evidence-index.json", encoding="utf-8"))

profiles = len(index["profiles"])
assert len(evidence["profiles"]) == profiles, ("evidence-index profiles", len(evidence["profiles"]), profiles)
families = len({source for profile in evidence["profiles"] for source in profile["sources"]})
verified = sum(profile["verified_observation_count"] for profile in evidence["profiles"])
if verified == 0:
    verified_text = "No observation is verified on a phone yet."
elif verified == 1:
    verified_text = "1 observation is verified on a phone."
else:
    verified_text = f"{verified:,} observations are verified on a phone."

paragraph = (
    f"{profiles:,} carrier profiles from {families} source families, from public commit "
    f"[`{commit[:8]}`]({PUBLIC_URL}/commit/{commit}). The oldest source check behind "
    f"them is from {index['checks_through']}, and this snapshot should ship until "
    f"{index['stale_after']}. {verified_text}"
)
block = "\n".join([START, f"## Status on {day}", "", textwrap.fill(paragraph, 78, break_on_hyphens=False, break_long_words=False), END])

text = open(PROFILE, encoding="utf-8").read()
assert text.count(START) == 1 and text.count(END) == 1, "status markers"
head, rest = text.split(START)
_, tail = rest.split(END)
open(PROFILE, "w", encoding="utf-8").write(head + block + tail)
print(f"profile: profiles={profiles} families={families} verified={verified} commit={commit[:8]} date={day}")
