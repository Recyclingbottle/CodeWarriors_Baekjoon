import sys

N, M = map(int, sys.stdin.readline().split())

arr = [0] * N 
for i in range(N):
    arr[i] = i+1

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    arr[i-1], arr[j-1] = arr[j-1], arr[i-1]

for ele in arr:
    print(ele, end=' ')