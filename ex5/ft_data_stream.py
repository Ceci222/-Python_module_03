from typing import Generator
import random

all_actions = [
    "run",
    "eat",
    "sleep",
    "grab",
    "move",
    "climb",
    "swim",
    "release",
    "use"
]

players = [
    "alice",
    "bob",
    "charlie",
    "dylan"
]


def gen_event(players: list[str], all_actions: list[str]) -> Generator[tuple[str,str], None, None]:
    while True:
        player = random.choice(players)
        action = random.choice(all_actions)
        yield (player, action)


def consume_event(event_list: list[tuple[str, str]]) -> Generator[tuple[str,str], None, None]:
    while (len(event_list) != 0):
        single_event = random.choice(event_list)
        event_list.remove(single_event)
        yield single_event

def main() -> None:
    print("=== Game Data Stream Processor ===")

    event_generator = gen_event(players, all_actions)

    for i in range(1000):
        event_player, event_action = next(event_generator)
        print(f"Event {i}: Player {event_player} did action {event_action}")

    event_list = [next(event_generator) for _ in range(10)]
    print(f"Built list of 10 events: {event_list}")

    event_consumer = consume_event(event_list)

    for event in event_consumer:
        print(f"Got event from list: {event}")
        print(f"Remains in list: {event_list}")


if __name__ == "__main__":
    main()