import sys

from ogsc.client import OgscClient
from ogsc.secret import BOT_TOKEN
from ogsc.tasks import DisconnectClientTask, VoiceStateChangedTask

from season1.channels import CHANNEL_ID_MEMES
from season1.events import EVENTS_MEMES
from season1.points import OgscPointsTable, OgscPointsTableKeys, OgscPointsValues
from season1.tasks import CollectVotePointsTask

def main():
    index = int(sys.argv[1])
    on_ready_tasks = [
        MemePointsTask(index),
        DisconnectClientTask(),
    ]
    client = OgscClient(
        on_ready_tasks=on_ready_tasks,
    )
    client.run(BOT_TOKEN)

def MemePointsTask(index: int) -> CollectVotePointsTask:
    event = EVENTS_MEMES[index]
    points_table = OgscPointsTable()

    def assign_participation_points(id: int):
        points_table.set_points(
            id, 
            OgscPointsTableKeys.MEME_PARTICIPATION[index], 
            OgscPointsValues.MEME_PARTICIPATION,
        )

    def assign_win_points(id: int):
        points_table.set_points(
            id,
            OgscPointsTableKeys.MEME_WIN[index],
            OgscPointsValues.MEME_WIN,
        )

    all_prev_winners = set()
    for i in range(1, index):
        prev_winners = [id for (id, points) in points_table.table.items() if points[OgscPointsTableKeys.MEME_WIN[i]] > 0]
        for winner in prev_winners:
            all_prev_winners.add(winner)

    return CollectVotePointsTask(
        channel_id=CHANNEL_ID_MEMES,
        start_time=event["start_time"],
        stop_time=event["stop_time"],
        assign_participation_points=assign_participation_points,
        assign_win_points=assign_win_points,
        previous_winners=list(all_prev_winners) 
    )

if __name__ == "__main__":

    main()