from re import search
from collections import defaultdict

claim = [f.strip() for f in open('3.txt', 'r')]
fields = defaultdict(int)

for c in claim:
    m = search(r'#(\d*) @ (\d*),(\d*): (\d*)x(\d*)', c)
    parsed = list(map(int, m.groups()))
    
    id, leftpad, toppad, width, height \
        = parsed[0], parsed[1], parsed[2], parsed[3], parsed[4]
    
    for y in range(toppad, toppad + height):
        for x in range(leftpad, leftpad + width):
            fields[(y, x)] += 1

print(sum(1 for i in fields.values() if i > 1))
