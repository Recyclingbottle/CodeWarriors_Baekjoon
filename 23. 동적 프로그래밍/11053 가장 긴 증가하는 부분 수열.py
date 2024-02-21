N = int(input())
A = list(map(int, input().split()))

# DP 배열 초기화
dp = [1] * N  # 각 위치에서의 최대 증가 부분 수열 길이

# LIS 계산
for i in range(N):
    for j in range(i):
        if A[i] > A[j]:
            dp[i] = max(dp[i], dp[j] + 1)

# 가장 긴 증가하는 부분 수열의 길이 출력
print(max(dp))
