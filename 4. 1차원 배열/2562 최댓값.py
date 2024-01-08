import sys

numbers = []
for i in range(9):
    n = int(sys.stdin.readline())
    numbers.append(n)

max_value = max(numbers)
max_index = numbers.index(max_value) + 1 #0부터 시작이니 +1

print(max_value)
print(max_index)