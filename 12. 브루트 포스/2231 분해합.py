import sys
n = int(sys.stdin.readline())
result = 0
for i in range(1, n+1):
    nums = sum((map(int, str(i))))
    result = i + nums
    if result == n:
        print(i)
        break
    if i == n: 
        print(0)