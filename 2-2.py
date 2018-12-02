box_ids = [f.strip() for f in open('2.txt', 'r')]

for i, string in enumerate(box_ids):
    for j, other_string in enumerate(box_ids[i + 1:]):
        if 1 is sum(a is not b for a, b in zip(string, other_string)):
            for c, char in enumerate(string):
                if char is not other_string[c]:
                    print(string[:c] + string[c + 1:])
