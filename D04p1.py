assignments = open("data/04_assignments.txt", "r")

number_of_complete_overlaps = 0

def split_pair(str):
    pair = str.split(',')
    assignment1 = pair[0].split('-')
    start1 = int(assignment1[0])
    end1 = int(assignment1[1])

    assignment2 = pair[1].split('-')
    start2 = int(assignment2[0])
    end2 = int(assignment2[1])

    return start1, end1, start2, end2

def completely_overlaps(start1, end1, start2, end2):
    return ((start1 <= start2) & (end1 >= end2)) | ((start2 <= start1) & (end2 >= end1))


for line in assignments:
    s1, e1, s2, e2 = split_pair(line)
    if completely_overlaps(s1, e1, s2, e2):
        number_of_complete_overlaps += 1

print(number_of_complete_overlaps)
