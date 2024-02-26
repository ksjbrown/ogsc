from ogsc.client import OgscClient
from ogsc.secret import BOT_TOKEN
from ogsc.tasks import DisconnectClientTask, SendMessageTask 

from season1.channels import CHANNEL_ID_WELCOME, CHANNEL_ID_S1_WELCOME
from season1.messages import MESSAGES_WELCOME, MESSAGES_S1_WELCOME


def main():
    on_ready_tasks = []

    for message in MESSAGES_WELCOME:
        on_ready_tasks.append(SendMessageTask(CHANNEL_ID_WELCOME, message))

    # for message in MESSAGES_S1_WELCOME:
    #     on_ready_tasks.append(SendMessageTask(CHANNEL_ID_S1_WELCOME, message))
        
    on_ready_tasks.append(DisconnectClientTask())

    client = OgscClient(
        on_ready_tasks=on_ready_tasks,
    )
    client.run(BOT_TOKEN)


if __name__ == "__main__":
    main()