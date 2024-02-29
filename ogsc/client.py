from __future__ import annotations

from typing import Protocol, Sequence

import discord


class OgscClient(discord.Client):
    def __init__(
        self, 
        on_ready_tasks: Sequence[OgscOnReadyTask] = [],
        on_voice_state_changed_tasks: Sequence[OgscOnVoiceStateChangedTask] = []
        ) -> None:
        super().__init__(intents=discord.Intents.default())
        self.on_ready_tasks = [*on_ready_tasks]
        self.on_voice_state_changed_tasks = [*on_voice_state_changed_tasks]

    async def on_ready(self):
        for task in self.on_ready_tasks:
            await task.execute(self)

    async def on_voice_state_update(
        self, 
        member: discord.Member, 
        before: discord.VoiceState, 
        after: discord.VoiceState,
        ):
        for task in self.on_voice_state_changed_tasks:
            await task.execute(self, member, before, after)


class OgscOnReadyTask(Protocol):
    async def execute(
        self, 
        client: OgscClient,
        ):
        ...

class OgscOnVoiceStateChangedTask(Protocol):
    async def execute(
        self, 
        client: OgscClient, 
        member: discord.Member, 
        before: discord.VoiceState, 
        after: discord.VoiceState,
        ):
        ...
