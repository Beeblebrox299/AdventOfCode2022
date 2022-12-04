from D04p1 import split_pair, completely_overlaps

assignments = open("data/04_assignments.txt", "r")
total_overlaps = 0

def partly_overlaps(start1, end1, start2, end2):
    return ((start1 <= start2) & (start2 <= end1)) | ((start2 <= start1) & (start1 <= end2))


for line in assignments:
    s1, e1, s2, e2 = split_pair(line)
    if completely_overlaps(s1, e1, s2, e2) | partly_overlaps(s1, e1, s2, e2):
        total_overlaps += 1

print(total_overlaps)
