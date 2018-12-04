import re
from datetime import datetime

logs = [f.strip() for f in open('input/4.txt', 'r')]
logs.sort(key=lambda l:datetime.strptime(l[1:17], '%Y-%m-%d %H:%M'))

guards = {}
current_guard = None

for i, log in enumerate(logs):
    m = re.search(r'\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2})\] (\w*) (#\d*)?', log)
    ts, s, id = m.groups()
    if s == 'wakes' and not id:
        continue
    if id:
        current_guard = id.strip('#')
        if not current_guard in guards:
            guards[current_guard] = {
                'time': [0] * 60
            }
    else :
        for j in range(int(ts[14:]), int(logs[i + 1][15:17])):
            guards[current_guard]['time'][j] += 1

for part in range(1, 3):
    most = None
    if part == 1: # p1
        most = [(key, sum(guards[key]['time'])) for key, _ in guards.items()]
    else: # p2
        most = [(key, max(guards[key]['time'])) for key, _ in guards.items()]
    guard = max(most, key=lambda item:item[1])
    minute = guards[guard[0]]['time'].index(max(guards[guard[0]]['time']))

    print(int(guard[0]) * int(minute))
