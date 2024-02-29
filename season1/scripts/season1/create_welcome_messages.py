from ogsc.client import OgscClient
from ogsc.secret import BOT_TOKEN
from ogsc.tasks import DisconnectClientTask, SendMessageTask 

from season1.channels import CHANNEL_ID_NEWS, CHANNEL_ID_WELCOME, CHANNEL_ID_S1_WELCOME, CHANNEL_ID_TEST_BOT_MESSAGES
from season1.messages import MESSAGES_NEWS_INTRODUCING_OGSC_MAKEOVER, MESSAGES_WELCOME, MESSAGES_S1_WELCOME


def main():
    on_ready_tasks = []

    # # main welcome page splash messages, short introduction
    # for message in MESSAGES_WELCOME:
    #     on_ready_tasks.append(SendMessageTask(CHANNEL_ID_WELCOME, message))

    # # welcome to Season 1, event and seaonal specific info
    # for message in MESSAGES_S1_WELCOME:
    #     on_ready_tasks.append(SendMessageTask(CHANNEL_ID_S1_WELCOME, message))

    # news post about makeover of the server
    for message in MESSAGES_NEWS_INTRODUCING_OGSC_MAKEOVER:
        on_ready_tasks.append(SendMessageTask(CHANNEL_ID_NEWS, message))
        
    on_ready_tasks.append(DisconnectClientTask())

    client = OgscClient(
        on_ready_tasks=on_ready_tasks,
    )
    client.run(BOT_TOKEN)


if __name__ == "__main__":
    main()