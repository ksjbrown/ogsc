import datetime

from season1.servers import SERVER_ID_OGSC
from season1.channels import CHANNEL_LINK_MEMES

_meme_desc = """Post those hilarious memes and earn those points!

Rules:
* To participate, you must do the following:
  * Post a meme to the [memes]({}) channel. It should be gaming related.
  * React to at least one other meme. If you do not react to another meme, other than your own, you will not be considered a participant!
* Participation in the meme competition will earn you 5 Season Points.
* The meme that earns the highest number of reactions will be deemed the winner, and will earn an additional 25 Season Points.
  * You can win a maximum of one Meme Competition per season. If your meme has the most reactions, and you have already won a competition, congratulations! You're very funny! But the winner will be the meme with the next highest reaction count :)
""".format(CHANNEL_LINK_MEMES)

_meme_start_date = datetime.datetime(2024, 4, 1)


EVENTS_MEMES: dict[int, dict] = {}
for i in range(10):
    EVENTS_MEMES[i+1] = {
        "server_id": SERVER_ID_OGSC,
        "name": "OGSC Meme Competition #{}".format(i+1),
        "location": CHANNEL_LINK_MEMES,
        "description": _meme_desc,
        "start_time": _meme_start_date + datetime.timedelta(weeks=i),
        "end_time": _meme_start_date + datetime.timedelta(weeks=i+1),
    }