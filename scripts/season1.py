import datetime
from dswog.channels import CHANNEL_TEST_CHAT, CHANNELS_S1
from dswog.client import DswogClient
from dswog.secret import BOT_TOKEN
from dswog.tasks import DisconnectClientTask, SendMessageTask, CollectVotePointsTask, VoiceStateChangedTask

def main():
    on_ready_tasks = [
        # SendMessageTask(CHANNEL_TEST_CHAT, "hello again"),
        CollectVotePointsTask(
            channel_id=CHANNELS_S1["memes"][0],
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

    client = DswogClient(
        on_ready_tasks=on_ready_tasks,
        # on_voice_state_changed_tasks=on_voice_state_changed_tasks,
    )
    client.run(BOT_TOKEN)


if __name__ == "__main__":
    main()