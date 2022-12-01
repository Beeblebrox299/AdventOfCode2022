calories = open("data/01-1_calories.txt", "r")


all_totals = []
current_total = 0
for line in calories.readlines():
    if line == '\n':
        all_totals.append(current_total)
        current_total = 0
    else:
        current_total += int(line)

all_totals.sort(reverse=True)
print(sum(all_totals[:3]))
