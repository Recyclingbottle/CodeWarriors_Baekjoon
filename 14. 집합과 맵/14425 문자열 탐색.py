import sys

N, M = map(int, sys.stdin.readline().split())
S = set(sys.stdin.readline().strip() for _ in range(N))

count = 0 

for _ in range(M):
    query = sys.stdin.readline().strip()
    if query in S:
        count += 1 

print(count)