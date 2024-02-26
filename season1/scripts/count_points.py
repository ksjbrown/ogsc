import datetime

from ogsc.client import OgscClient
from ogsc.secret import BOT_TOKEN
from ogsc.tasks import DisconnectClientTask, VoiceStateChangedTask

from season1.channels import CHANNEL_ID_MEMES
from season1.tasks import CollectVotePointsTask

def main():
    on_ready_tasks = [
        # SendMessageTask(CHANNEL_TEST_CHAT, "hello again"),
        CollectVotePointsTask(
            channel_id=CHANNEL_ID_MEMES,
            start_time=datetime.datetime(2024, 2, 22, 0, 0, 0),
            stop_time=datetime.datetime(2024, 2, 23, 23, 59, 59),
            participation_points=2,
            win_points=25,
            process_scores=print,
        ),
        DisconnectClientTask(),
    ]
    on_voice_state_changed_tasks = [
        VoiceStateChangedTask()
    ]

    client = OgscClient(
        on_ready_tasks=on_ready_tasks,
        # on_voice_state_changed_tasks=on_voice_state_changed_tasks,
    )
    client.run(BOT_TOKEN)


if __name__ == "__main__":
    main()