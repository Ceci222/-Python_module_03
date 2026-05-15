import sys
program_name = sys.argv[0]

if(len(sys.argv) == 1):
    print("=== Command Quest ===")
    print("Program name:", program_name)
    print("No arguments provided!")
    print("Total arguments:", 1)
    print()

if(len(sys.argv) > 2):
    print("=== Command Quest ===")
    print("Program name:", program_name)
    print("Arguments received:",len(sys.argv[1:]))
    i = 1
    for arg in sys.argv[1:]:
        print(f"Argument {i}: {arg}")
        i += 1
    print("Total arguments:", len(sys.argv))
    print()

if(len(sys.argv) == 2):
    print("=== Command Quest ===")
    print("Program name:", program_name)
    i = 1
    for arg in sys.argv[1: ]:
        print(f"Arguments received:", len(sys.argv[1:]))
        print(f"Argument {i}: {arg}")
        i += 1
    print("Total arguments:", len(sys.argv))
    print()