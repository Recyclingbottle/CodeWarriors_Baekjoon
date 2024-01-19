import sys

input = sys.stdin.readline

K = int(input())
stack = []
for _ in range(K):
    n = int(input())
    if n > 0: 
        stack.append(n)
    elif n == 0:
        stack.pop()
sum = 0
for i in stack:
    sum += i

print(sum)    