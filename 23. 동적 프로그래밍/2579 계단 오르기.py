import sys

# 입력을 빠르게 받기 위한 설정
input = sys.stdin.readline

n = int(input())
stairs = [int(input().strip()) for _ in range(n)]

# dp 배열 초기화
dp = [0] * n
dp[0] = stairs[0]
if n > 1:
    dp[1] = stairs[0] + stairs[1]
for i in range(2, n):
    dp[i] = max(dp[i-2] + stairs[i], dp[i-3] + stairs[i-1] + stairs[i])

print(dp[n-1])