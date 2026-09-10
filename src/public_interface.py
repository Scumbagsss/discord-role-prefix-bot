"""Portfolio-only interface skeleton. This module is intentionally non-runnable."""


class DiscordRolePrefixBotInterface:
    """Architectural surface of the private production implementation."""

    async def resolve_prefix(self, *args, **kwargs):
        """Public portfolio signature only. Production logic is private."""
        raise NotImplementedError("Production implementation is private")

    async def normalize_nickname(self, *args, **kwargs):
        """Public portfolio signature only. Production logic is private."""
        raise NotImplementedError("Production implementation is private")

    async def sync_member_nickname(self, *args, **kwargs):
        """Public portfolio signature only. Production logic is private."""
        raise NotImplementedError("Production implementation is private")

    async def update_prefix_mapping(self, *args, **kwargs):
        """Public portfolio signature only. Production logic is private."""
        raise NotImplementedError("Production implementation is private")

