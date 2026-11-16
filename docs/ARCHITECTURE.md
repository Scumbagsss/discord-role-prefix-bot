# Discord Role Prefix Manager — architecture notes

> This is a **suggested technical boundary for a private-source module**, not a claim that all components are implemented or active in a particular deployment.

## Objective

Roleplay communities often encode a group or clan in a member's nickname. Automated prefix updates become tricky when roles change, users edit their own names, or existing nicknames already contain a managed prefix.

## Conceptual responsibilities

**1. Member role update.** Observe a relevant role or member update.

**2. Prefix policy.** Resolve which configured prefix, if any, should apply.

**3. Name normalization.** Strip only the previously managed prefix from the display name.

**4. Permission check.** Respect exclusions and Discord nickname length/permission limits.

**5. Nickname sync.** Apply the new name and save the mapping change if needed.

## Review risks and recommended tests

| Concern | Failure mode | Verification to add |
|---|---|---|
| Update loops | Changing a nickname may trigger another member update | Make normalization idempotent |
| Role precedence | Members can hold multiple eligible roles | Define and test a stable priority order |
| Permission limits | Discord may prevent editing some members | Record failures without retry storms |
| User name integrity | Unmanaged parts of the nickname must not be lost | Use a reversible base-name strategy |

## Integration and permissions

The Discord interaction layer should treat its inputs as untrusted. A server-side handler must establish the principal, check authorization for the concrete operation and return user-safe errors. The persistence or external API adapter is separately responsible for safe updates, retries and recovery. The public `src/public_interface.py` is only a surface sketch; **none of these safeguards can be confirmed by running it**.

## Production/public boundary

No real member IDs, credentials, channel IDs, private schemas, moderation rules or live logs should appear in this repository. The architectural context belongs to the wider [DeadCity platform case study](https://github.com/Scumbagsss/BOT). For a separately developed runnable example, see the [ticket workflow backend](https://github.com/Scumbagsss/advanced-discord-ticket-bot).
