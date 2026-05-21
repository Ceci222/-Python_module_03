import sys


USAGE = ("No scores provided. "
         "Usage: python3 ft_score_analytics.py <score1> <score2> ...")


def add_scores_to_list() -> list[int]:
    scores = []
    for arg in sys.argv[1:]:
        try:
            scores.append(int(arg))
        except ValueError:
            print(f"Invalid parameter: '{arg}'")
    return scores


def check_args() -> int:
    if (len(sys.argv) == 1):
        print(USAGE)
        print()
        return 1
    return 0


def main() -> None:
    print("=== Player Score Analytics ===")

    if (check_args() == 1):
        return

    scores = add_scores_to_list()

    if (len(scores) == 0):
        print(USAGE)
        print()
        return

    print(f"Scores processed: {scores}")
    print("Total players:", len(scores))
    print("Total score:", sum(scores))
    print("Average score:", sum(scores) / len(scores))
    print("High score:", max(scores))
    print("Low score:", min(scores))
    print("Score range:", max(scores) - min(scores))
    print()


if __name__ == "__main__":
    main()
