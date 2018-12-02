box_ids = [f.strip() for f in open('2.txt', 'r')]
final_result = {2: 0, 3: 0}
for string in box_ids:
    counting = {}
    for char in string:
        counting[char] = counting[char] + 1 if char in counting else 1
    if any(n in counting.values() for n in (2, 3)):
        for n in set(filter(lambda n: n is 2 or n is 3, counting.values())):
            final_result[n] += 1

print(final_result[2] * final_result[3])
    