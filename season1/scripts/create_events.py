from ogsc.client import OgscClient
from ogsc.secret import BOT_TOKEN
from ogsc.tasks import CreateEventTask, DisconnectClientTask

from season1.events import EVENTS_MEMES


def main():
    on_ready_tasks = []
    for event in EVENTS_MEMES.values():
        on_ready_tasks.append(CreateEventTask(**event))

    on_ready_tasks.append(DisconnectClientTask())

    # for message in MESSAGES_S1_WELCOME:
    #     on_ready_tasks.append(SendMessageTask(CHANNEL_ID_S1_WELCOME, message))

    client = OgscClient(
        on_ready_tasks=on_ready_tasks,
    )
    client.run(BOT_TOKEN)


if __name__ == "__main__":
    main()