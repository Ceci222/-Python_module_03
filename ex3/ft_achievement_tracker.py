import random

all_achievements = [
    "Crafting Genius",
    "World Savior",
    "Master Explorer",
    "Collector Supreme",
    "Untouchable",
    "Boss Slayer",
    "Strategist",
    "Unstoppable",
    "Speed Runner",
    "Survivor",
    "Treasure Hunter",
    "First Steps",
    "Sharp Mind",
    "Hidden Path Finder"
]

players_list = ["Alice", "Bob", "Charlie", "Dylan"]


def gen_player_achievements(all_achievements: list) -> set:
    random_num = random.randint(5, 13)
    player_achievements_list = random.sample(all_achievements, random_num)
    player_achievements = set(player_achievements_list)
    return set(player_achievements)


def gen_individual_achievements(
        players_list: list, all_achievements: list) -> list:
    players_with_achievements = []
    for player in players_list:
        player_achievement_set = gen_player_achievements(all_achievements)
        players_with_achievements.append((player, player_achievement_set))
        #  append accepts only one arg, needs () for tuple
    return players_with_achievements


def main() -> None:
    print("=== Achievement Tracker System ===")

    individual_achievements = (
        gen_individual_achievements(players_list, all_achievements)
    )
    for player, achievement in individual_achievements:
        print(f"Player {player}: {achievement}")
    print()

    all_player_achievement_sets = []
    for player, player_achievement_set in individual_achievements:
        all_player_achievement_sets.append(player_achievement_set)

    distinct_achievements = set().union(*all_player_achievement_sets)
    #  union needs to be called on a set, empty in this case.
    #  * unpacks the args otherwise I get the full list of args including []

    print(f"All distinct achievements: {distinct_achievements}")
    print()

    common_achievements = None

    for _, player_set_of_achievements in individual_achievements:
        if (common_achievements is None):  # -> == works but flake8 fails
            common_achievements = player_set_of_achievements
        else:
            common_achievements = (
                common_achievements.intersection(player_set_of_achievements)
            )

    print(f"Common achievements: {common_achievements}")
    print()

    (_, alice_set), (_, bob_set), (_, charlie_set), (_, dylan_set) = (
        individual_achievements
    )
    # () -> unpack

    alice_only = alice_set.difference(charlie_set, dylan_set, bob_set)
    bob_only = bob_set.difference(charlie_set, dylan_set, alice_set)
    dylan_only = dylan_set.difference(charlie_set, alice_set, bob_set)
    charlie_only = charlie_set.difference(alice_set, dylan_set, bob_set)

    print(f"Only Alice has: {alice_only}")
    print(f"Only Bob has: {bob_only}")
    print(f"Only Charlie has: {charlie_only}")
    print(f"Only Dylan has: {dylan_only}")
    print()

    for player, player_achievements in individual_achievements:
        player_is_missing = (
            distinct_achievements.difference(player_achievements)
        )
        # from all distinct achievements excluding current player acheivements
        print(f"{player} is missing: {player_is_missing}")
    print()


if __name__ == "__main__":
    main()
