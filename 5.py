input = [f for f in open('input/5', 'r')][0]

# p1
stack = []
for char in input:
    if len(stack) == 0:
        stack.append(char)
    elif stack[-1].lower() == char.lower() and stack[-1] != char:
        stack.pop()
    else:
        stack.append(char)

print(len(stack))
