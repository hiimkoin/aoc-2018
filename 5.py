from string import ascii_lowercase

input = [f for f in open('input/5', 'r')][0]

small = []
for char in '0' + ascii_lowercase:
    
    if char != '0': # p2
        input2 = input.replace(char, '')
        input2 = input2.replace(char.upper(), '')
    else: # p1
        input2 = input

    stack = []
    for char in input2:
        if len(stack) == 0:
            stack.append(char)
        elif stack[-1].lower() == char.lower() and stack[-1] != char:
            stack.pop()
        else:
            stack.append(char)

    small.append(len(stack))

print(small[0]) # p1
print(min(small)) # p2
