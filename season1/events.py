import datetime

from season1.servers import SERVER_ID_OGSC
from season1.channels import CHANNEL_LINK_HANGING_OUT, CHANNEL_LINK_MEMES


class Event:
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

    def to_kwargs(self) -> dict:
        return {
            "server_id": self.server_id,
            "name": self.name,
            "location": self.location,
            "description": self.description,
            "start_time": self.start_time,
            "end_time": self.end_time,
        }


_meme_desc = """Post those hilarious memes and earn those points!

Rules:
* To participate, you must do the following:
  * Post a meme to the [memes]({}) channel. It should be gaming related.
  * React to at least one other meme. If you do not react to another meme, other than your own, you will not be considered a participant!
* Participation in the meme competition will earn you 5 Season Points.
* The meme that earns the highest number of reactions will be deemed the winner, and will earn an additional 25 Season Points.
  * You can win a maximum of one Meme Competition per season. If your meme has the most reactions, and you have already won a competition, congratulations! You're very funny! But the winner will be the meme with the next highest reaction count :)
""".format(
    CHANNEL_LINK_MEMES
)

_meme_start_date = datetime.datetime(2024, 4, 1)


EVENTS_MEMES: dict[int, dict] = {}
for i in range(10):
    EVENTS_MEMES[i + 1] = {
        "server_id": SERVER_ID_OGSC,
        "name": "OGSC Meme Competition #{}".format(i + 1),
        "location": CHANNEL_LINK_MEMES,
        "description": _meme_desc,
        "start_time": _meme_start_date + datetime.timedelta(weeks=i),
        "end_time": _meme_start_date + datetime.timedelta(weeks=i + 1),
    }

EVENT_PRE_GRAND_OPENING = Event(
    server_id=SERVER_ID_OGSC,
    name="OGSC Pre Grand Opening",
    description="""Hey guys!

It's been a while!
If you've got nothing to do, we need some help dusting out the cobwebs in the server and getting back into the online gaming social spirit!

If you have any questions or comments about the server, the OGSC organizers will also be available to hear your thoughts.

Hope to see you there!
""",
    location="{}".format(CHANNEL_LINK_HANGING_OUT),
    start_time=datetime.datetime(2024, 3, 1, 19, 0, 0),
    end_time=datetime.datetime(2024, 3, 1, 21, 0, 0),
)
