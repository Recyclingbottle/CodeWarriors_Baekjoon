import sys

N, M = map(int, sys.stdin.readline().split())

arr = [0] * N

for _ in range(M):
    i, j, k = map(int, sys.stdin.readline().split())
    for a in range(i,j+1):
        arr[a-1] = k

for ele in arr:
    print(ele, end=' ')