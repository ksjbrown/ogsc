from dswog.client import DswogClient
from dswog.secret import BOT_TOKEN
from dswog.tasks import CreateEventTask, DisconnectClientTask

from season1.events import EVENTS_MEMES


def main():
    on_ready_tasks = []
    for i in range(1, len(EVENTS_MEMES)+1):
        on_ready_tasks.append(CreateEventTask(**EVENTS_MEMES[i]))

    on_ready_tasks.append(DisconnectClientTask())

    # for message in MESSAGES_S1_WELCOME:
    #     on_ready_tasks.append(SendMessageTask(CHANNEL_ID_S1_WELCOME, message))

    client = DswogClient(
        on_ready_tasks=on_ready_tasks,
    )
    client.run(BOT_TOKEN)


if __name__ == "__main__":
    main()