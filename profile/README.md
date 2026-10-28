# Open Carrier Data

> **Early development.** Open Carrier Data is in early development. Data, formats, tools and apps change often, and values can be wrong or missing. Don't rely on it for anything important yet. Feedback and reports are welcome.

A public database of carrier settings for open-source phone systems. It merges
public sources such as AOSP, LineageOS, GNOME's provider list, Apple's carrier
bundles, Google Pixel settings, and Samsung firmware into neutral carrier
profiles, records where every fact came from, and generates the Android files
a ROM can ship.

## Start here

- Database and docs: https://github.com/open-carrier-data/open-carrier-data
- Website: https://open-carrier-data.github.io/
- Report missing or wrong data: https://github.com/open-carrier-data/open-carrier-data/issues/new/choose
- Latest snapshot index: https://raw.githubusercontent.com/open-carrier-data/open-carrier-data/main/generated/index.json

<!-- status:start (tools/update_profile_status.py rewrites this block) -->
## Status on 2026-10-28

6,374 carrier profiles from 12 source families, from public commit
[`a2f96412`](https://github.com/open-carrier-data/open-carrier-data/commit/a2f96412b58fda0ce7599d2b6b9431136f9b3262).
The oldest source check behind them is from 2026-07-14, and this snapshot
should ship until 2027-01-10. No observation is verified on a phone yet.
<!-- status:end -->

The project has no external users yet. Read the limits in the public README
before you ship the data.

## License

Software and documentation are Apache-2.0. The project's own rights in the
data are waived under CC0 1.0, subject to upstream terms. See `DATA-LICENSE.md`
in the public repository.
