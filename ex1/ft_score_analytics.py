import sys

print("=== Player Score Analytics ===")

arguments = sys.argv[1:]
players = len(arguments)
total = sum(arguments)
average_score = sum(arguments) / len(arguments)
top_score = max(arguments)
lowest_score = min(arguments)
score_range =  max(arguments) - min(arguments)

try:
    for arg in arguments:
        int(arg)
    
    print(f"Scores processed: [{arguments}]")
    print(f"Total players: {players}")
    print(f"Total score: {total}")
    print(f"Average score: {average_score}")
    print(f"High score: {top_score}")
    print(f"Low score: {lowest_score}")
    print(f"Score range: {score_range}")

except:
    for arg in arguments:
    print("Invalid parameter:")