from __future__ import annotations

from typing import Protocol

import discord

from dswog.secret import BOT_TOKEN


class DswogTask(Protocol):
    async def execute(self, client: DswogClient):
        ...


class DswogClient(discord.Client):
    def __init__(self, *tasks: DswogTask) -> None:
        super().__init__(intents=discord.Intents.default())
        self.tasks: list[DswogTask] = [*tasks]

    async def on_ready(self):
        for task in self.tasks:
            await task.execute(self)

