from collections import deque

# Create an empty deque
d = deque()

# Read the number of operations
n = int(input())

# Perform operations
for _ in range(n):
    operation = input().split()
    if operation[0] == 'append':
        d.append(int(operation[1]))
    elif operation[0] == 'appendleft':
        d.appendleft(int(operation[1]))
    elif operation[0] == 'pop':
        d.pop()
    elif operation[0] == 'popleft':
        d.popleft()

# Print the space-separated elements of deque
print(' '.join(map(str, d)))