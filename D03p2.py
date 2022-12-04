from D03p1 import values

rucksacks = open("data/03_rucksacks.txt", "r").read()

content_list = rucksacks.splitlines()
value_sum = 0
i = 0

while i < len(content_list):
    group = content_list[i:i+3]
    for char in group[0] + group[1] + group[2]:
        if (char in group[0]) & (char in group[1]) & (char in group[2]):
            value_sum += values[char]
            break
    i += 3

print(value_sum)
