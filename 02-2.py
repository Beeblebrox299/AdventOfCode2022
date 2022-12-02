strategy = open("data/02_rock-paper-scissors.txt", "r")

rock = ["A Y", "B X", "C Z"]
paper = ["A Z", "B Y", "C X"]
scissors = ["A X", "B Z", "C Y"]
total_score = 0

for line in strategy:
    if line[2] == 'Y':
        total_score += 3
    elif line[2] == 'Z':
        total_score += 6

    if line[:3] in rock:
        total_score += 1
    elif line[:3] in paper:
        total_score += 2
    elif line[:3] in scissors:
        total_score += 3

print(total_score)
