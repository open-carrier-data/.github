# Open Carrier Data

Open Carrier Data is a public carrier settings database for open-source phone
systems.

It helps ROMs, carrier configuration apps, eSIM tools, and build pipelines
package current carrier data locally. The goal is better APN, MMS, IMS, RCS,
eSIM, and Android CarrierConfig support without every project maintaining the
same fixes alone.

## Start Here

- Website: https://open-carrier-data.github.io/
- Public database: https://github.com/open-carrier-data/open-carrier-data
- Report missing or wrong data: https://github.com/open-carrier-data/open-carrier-data/issues/new/choose
- Contribution guide: https://github.com/open-carrier-data/open-carrier-data/blob/main/CONTRIBUTING.md
- Stable snapshot: https://raw.githubusercontent.com/open-carrier-data/open-carrier-data/main/generated/index.json
- Schema: https://github.com/open-carrier-data/open-carrier-data/tree/main/schemas

## How The Project Works

```text
maintained sources
-> private import and sanitizing
-> public neutral carrier profiles
-> generated snapshots and Android files
-> ROMs/apps/build tools package the data locally
```

Community reports are handled as claims. Claims are useful for fast edge-case
testing, but they do not silently become stable phone defaults.

Stable data is conservative. Maintained public sources can be refreshed
directly. Private vendor or OEM source snapshots must be refreshed and checked
before they can affect stable output. Missing data is better than stale data
that looks current.

Phones should use local generated data. They should not depend on a live GitHub
request while loading a SIM, starting a call, sending messages, registering IMS,
or handling emergency service.

## How To Help

If carrier data is missing or wrong, open a guided issue in the public repo.
You do not need write access.

If you tested a specific fix, either open a tested-claim issue or fork the
public repo and submit a pull request with a claim under `community/claims/`.

If you know a maintained source that should be imported, open a source
suggestion issue.

Do not submit phone numbers, account data, personal passwords, private vendor
credentials, tokens, full IMSI values, full ICCID values, IMEI, raw logs, raw
firmware dumps, or private vendor responses. Public APN usernames/passwords are
okay only when they are carrier settings, not private account credentials.

## Principles

- Keep public data neutral and source-independent.
- Prefer maintained, repeatable sources over one-off manual entries.
- Keep community claims separate from stable defaults.
- Publish only safe carrier facts.
- Treat stale or untrusted data as worse than missing data.

## License Status

No final project license has been added yet. A clear license for data and
tooling should be added before broad reuse is encouraged.
