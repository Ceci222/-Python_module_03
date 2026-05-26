import sys


def main() -> None:
    program_name = sys.argv[0]

    print("=== Command Quest ===")
    print("Program name:", program_name)

    if (len(sys.argv) == 1):
        print("No arguments provided!")

    else:
        print("Arguments received:", len(sys.argv[1:]))
        i = 1
        for arg in sys.argv[1:]:
            print(f"Argument {i}: {arg}")
            i += 1

    print("Total arguments:", len(sys.argv))
    print()


if __name__ == "__main__":
    main()
