from dswog.client import DswogClient


class SendMessageTask:
    def __init__(self, channel_id: int, msg: str) -> None:
        self.channel_id = channel_id
        self.msg = msg

    async def execute(self, client: DswogClient):
        channel = client.get_channel(self.channel_id)
        try:
            await channel.send(self.msg)
        except:
            ...
    