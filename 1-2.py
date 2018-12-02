def twice():
    frequencies = [int(f.strip()) for f in open('1.txt', 'r')]
    seen = set()
    current_freq = 0
    while True:
        for freq in frequencies:
            current_freq += freq
            if current_freq in seen:
                return current_freq
            seen.add(current_freq)
            
print(twice())
