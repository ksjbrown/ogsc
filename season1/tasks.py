from collections import defaultdict
import datetime
from typing import Any, Callable, Sequence

import discord

from season1.points import OgscPointsTable


class CollectVotePointsTask:
    def __init__(
            self, 
            channel_id: int, 
            start_time: datetime.datetime, 
            stop_time: datetime.datetime,
            assign_participation_points: Callable[[int], None],
            assign_win_points: Callable[[int], None],
            previous_winners: Sequence[int],
        ) -> None:
        
        self.channel_id = channel_id
        self.start_time = start_time
        self.stop_time = stop_time
        self.assign_participation_points = assign_participation_points
        self.assign_win_points = assign_win_points
        self.previous_winners = previous_winners

    async def execute(self, client: discord.Client):
        channel = client.get_channel(self.channel_id)
        if not channel:
            return
        
        if not isinstance(channel, discord.TextChannel):
            return

        participants: dict[int, discord.User] = {}
        message_ranks: dict[int, list[discord.Message]] = defaultdict(lambda: list())

        async for message in channel.history(limit=None, after=self.start_time, before=self.stop_time):
            if message.author.id not in participants:
                participants[message.author.id] = message.author # type: ignore
            message_score = len(message.reactions)
            message_ranks[message_score].append(message)
            
        for author in participants.values():
            self.assign_participation_points(author.id)

        for message_score, messages in sorted(message_ranks.items(), key=lambda p: p[1], reverse=True):
            new_winner_messages = [m for m in messages if m.author.id not in self.previous_winners]
            if not new_winner_messages:
                continue
            for new_winner_message in new_winner_messages:
                self.assign_win_points(new_winner_message.author.id)
            break