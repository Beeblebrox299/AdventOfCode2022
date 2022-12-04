rucksacks = open("data/03_rucksacks.txt", "r")

values = dict()

for i in range(97, 123):
    values[chr(i)] = i - 96

for i in range(65, 91):
    values[chr(i)] = i - 64 + 26

value_sum = 0

for line in rucksacks:
    comp_1 = line[:(len(line)//2)]
    comp_2 = line[(len(line)//2):]
    for char in comp_1:
        if char in comp_2:
            value_sum += values[char]
            break

print(value_sum)
