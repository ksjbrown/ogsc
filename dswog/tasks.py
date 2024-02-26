import datetime
from typing import Any, Callable, Sequence

import discord

class DisconnectClientTask:
    async def execute(self, client: discord.Client):
        await client.close()

class SendMessageTask:
    def __init__(self, channel_id: int, msg: str) -> None:
        self.channel_id = channel_id
        self.msg = msg

    async def execute(self, client: discord.Client):
        channel = client.get_channel(self.channel_id)
        if not isinstance(channel, discord.TextChannel):
            return

        try:
            await channel.send(self.msg) 
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

class CollectVotePointsTask:
    def __init__(
            self, 
            channel_id: int, 
            start_time: datetime.datetime, 
            stop_time: datetime.datetime,
            participation_points: int,
            win_points: int,
            process_scores: Callable[[dict[discord.User, int]], Any]
        ) -> None:
        
        self.channel_id = channel_id
        self.start_time = start_time
        self.stop_time = stop_time
        self.participation_points = participation_points
        self.win_points = win_points
        self.process_scores = process_scores

    async def execute(self, client: discord.Client):
        channel = client.get_channel(self.channel_id)
        if not channel:
            return
        
        if not isinstance(channel, discord.TextChannel):
            return

        best_messages: list[discord.Message] = []
        best_message_score: int = 0
        participants: dict[int, discord.User] = {}

        async for message in channel.history(limit=None, after=self.start_time, before=self.stop_time):
        # async for message in channel.history(limit=None):
            participants[message.author.id] = message.author
            message_score = len(message.reactions)
            if message_score > best_message_score:
                best_messages.clear()
                best_message_score = message_score
            if message_score == best_message_score:
                best_messages.append(message)

        scores: dict[discord.User, int] = {}

        for author in participants.values():
            scores[author] = self.participation_points

        for best_message in best_messages:
            scores[best_message.author] += self.win_points

        self.process_scores(scores)

class VoiceStateChangedTask:
    def __init__(self) -> None:
        pass
        
    async def execute(self, client: discord.Client, member: discord.Member, before: discord.VoiceState, after: discord.VoiceState):
        print(f"{member.name} switched from {before.channel} to {after.channel}")