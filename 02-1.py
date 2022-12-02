strategy = open("data/02_rock-paper-scissors.txt", "r")

wins = ["A Y", "B Z", "C X"]
draws = ["A X", "B Y", "C Z"]
total_score = 0

for line in strategy:
    if line[:3] in wins:
        total_score += 6
    elif line[:3] in draws:
        total_score += 3

    if line[2] == 'X':
        total_score += 1
    elif line[2] == 'Y':
        total_score += 2
    elif line[2] == 'Z':
        total_score += 3

print(total_score)
