# Discord Role Prefix Bot

> **Portfolio showcase — production source is private and this repository is intentionally non-runnable.**

Synchronizes Discord nicknames with role-based clan and faction prefixes.

## What it demonstrates

- Role ID to prefix mapping
- Automatic nickname sync
- Old-prefix cleanup
- Excluded-role rules
- Discord manager UI
- Persistent mappings

## Technology

Python • discord.py • JSON storage • Member update events

## High-level workflow

1. Observe role/nickname state
2. Resolve active managed prefix
3. Normalize base nickname
4. Apply synchronized nickname
5. Persist manager changes

## Public interface preview

The public skeleton exposes only the architectural surface:

- `resolve_prefix(...)`
- `normalize_nickname(...)`
- `sync_member_nickname(...)`
- `update_prefix_mapping(...)`

The production implementations behind these methods are withheld. See [`NOTICE.md`](NOTICE.md).

## Repository contents

- `src/public_interface.py` — non-runnable interface skeleton;
- `docs/ARCHITECTURE.md` — high-level design;
- `examples/config.example.jsonc` — sanitized configuration shape;
- `LICENSE` — explicit all-rights-reserved notice.

## Status

Production-tested private project / portfolio edition.
