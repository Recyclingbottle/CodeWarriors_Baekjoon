import sys

N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

prefixSum = [0] * (N+1)
for i in range(1, N+1):
    prefixSum[i] = prefixSum[i-1] + arr[i-1]

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    print(prefixSum[j] - prefixSum[i-1])
