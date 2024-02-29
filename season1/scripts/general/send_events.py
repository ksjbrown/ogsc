from ogsc.client import OgscClient
from ogsc.secret import BOT_TOKEN
from ogsc.tasks import CreateEventTask, DisconnectClientTask
from season1.events import EVENT_PRE_GRAND_OPENING

def main():
    on_ready_tasks = []
    
    # add events to send below
    on_ready_tasks.append(
        CreateEventTask(
            **EVENT_PRE_GRAND_OPENING.to_kwargs(),
        ),
    )
    # add events to send above

    on_ready_tasks.append(DisconnectClientTask())

    client = OgscClient(
        on_ready_tasks=on_ready_tasks,
    )
    client.run(BOT_TOKEN)


if __name__ == "__main__":
    main()
