import datetime
from typing import Any, Callable, Sequence

import discord

from season1.servers import SERVER_ID_OGSC

class DisconnectClientTask:
    async def execute(self, client: discord.Client):
        await client.close()

class SendMessageTask:
    def __init__(self, channel_id: int, msg: str) -> None:
        self.channel_id = channel_id
        self.msg = msg

    async def execute(self, client: discord.Client):
        channel = client.get_channel(self.channel_id)
        try:
            await channel.send(self.msg) #type: ignore
        except:
            ...

class RevealChannelTask:
    def __init__(
            self, 
            channel_id: int,
            time: datetime.datetime,
        ) -> None:
        self.channel_id = channel_id
        self.time = time

    async def execute(self, client: discord.Client):
        ...

class CreateEventTask:

    def __init__(
        self,
        server_id: int,
        name: str,
        location: str,
        description: str,
        start_time: datetime.datetime,
        end_time: datetime.datetime,
        ) -> None:
        self.server_id = server_id
        self.name = name
        self.location = location
        self.description = description
        self.start_time = start_time
        self.end_time = end_time


    async def execute(self, client: discord.Client):
        guild = client.get_guild(self.server_id)

        if guild is None:
            return
        
        await guild.create_scheduled_event(
            name=self.name,
            location=self.location,
            description=self.description,
            start_time=self.start_time.astimezone(),
            end_time=self.end_time.astimezone(),
            entity_type=discord.EntityType.external,
            privacy_level=discord.PrivacyLevel.guild_only,
        )

class VoiceStateChangedTask:
    def __init__(self) -> None:
        pass
        
    async def execute(self, client: discord.Client, member: discord.Member, before: discord.VoiceState, after: discord.VoiceState):
        print(f"{member.name} switched from {before.channel} to {after.channel}")