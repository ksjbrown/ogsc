from ogsc.client import OgscClient
from ogsc.secret import BOT_TOKEN
from ogsc.tasks import DisconnectClientTask, SendMessageTask
from season1.channels import CHANNEL_ID_CHAT
from season1.messages import MESSAGE_NOTIFY_PRE_GRAND_OPENING


def main():
    on_ready_tasks = []

    # add messages to send below
    for message in MESSAGE_NOTIFY_PRE_GRAND_OPENING:
        on_ready_tasks.append(
            SendMessageTask(CHANNEL_ID_CHAT, message),
        )
    # add messages to send above

    on_ready_tasks.append(DisconnectClientTask())

    client = OgscClient(
        on_ready_tasks=on_ready_tasks,
    )

    client.run(BOT_TOKEN)


if __name__ == "__main__":
    main()
