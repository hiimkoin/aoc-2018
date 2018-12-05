from re import search
from collections import defaultdict

claim = [f.strip() for f in open('input/3', 'r')]
fields = defaultdict(int)

for part in range(1, 3):
    for c in claim:

        m = search(r'#(\d*) @ (\d*),(\d*): (\d*)x(\d*)', c)
        parsed = list(map(int, m.groups()))
        
        id, leftpad, toppad, width, height \
            = parsed[0], parsed[1], parsed[2], parsed[3], parsed[4]
        
        overlaps = False

        for y in range(toppad, toppad + height):
            for x in range(leftpad, leftpad + width):
                if part == 2 and fields[(y, x)] > 1:
                    overlaps = True
                fields[(y, x)] += 1

        if part == 2 and not overlaps: # p2
            print(id)

    if part == 1: # p1
        print(sum(1 for i in fields.values() if i > 1))
