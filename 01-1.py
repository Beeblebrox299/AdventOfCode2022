calories = open("data/01-1_calories.txt", "r")


biggest_total = 0
current_total = 0
for line in calories.readlines():
    if line == '\n':
        current_total = 0
    else:
        current_total += int(line)
        if current_total > biggest_total:
            biggest_total = current_total

print(biggest_total)

