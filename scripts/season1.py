from dswog.channels import CHANNEL_TEST_CHAT
from dswog.client import DswogClient
from dswog.secret import BOT_TOKEN
from dswog.tasks import SendMessageTask

def main():
    tasks = [
        SendMessageTask(CHANNEL_TEST_CHAT, "hello again")
    ]

    client = DswogClient(*tasks)
    client.run(BOT_TOKEN)


if __name__ == "__main__":
    main()