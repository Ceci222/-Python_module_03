import random


def capitalizer(list_of_players: list[str]) -> list[str]:
    caps_list = [player.capitalize() for player in list_of_players]
    return caps_list


def gen_dictionary(caps_list: list[str]) -> dict[str, int]:
    player_score_dict = {key: random.randint(0, 1000) for key in caps_list}
    return player_score_dict


def main() -> None:
    print("=== Game Data Alchemist ===")
    players_list = [
        "Alice", "bob", "Charlie", "dylan", "Emma",
        "Gregory", "john", "kevin", "Liam"
    ]

    print(f"Initial list of players: {players_list}")
    caps_players_list = capitalizer(players_list)
    print(f"New list with all names capitalized: {caps_players_list}")

    title = [player for player in players_list if player.istitle()]
    print(f"New list of capitalized names only: {title}")

    scores_dict = gen_dictionary(caps_players_list)
    print(f"Score dict: {scores_dict}")

    score_average = sum(scores_dict.values()) / len(scores_dict.values())
    print(f"Score average is {round(score_average, 2)}")

    high_scores = {
        key: value for key, value in scores_dict.items()
        if value > score_average
    }

    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    main()
