# p1
data = [int(f.strip()) for f in open('input/1.txt', 'r')]
print(sum(data))

# p2
def twice():
    seen = set()
    current_freq = 0
    while True:
        for freq in data:
            current_freq += freq
            if current_freq in seen:
                return current_freq
            seen.add(current_freq)
print(twice())
