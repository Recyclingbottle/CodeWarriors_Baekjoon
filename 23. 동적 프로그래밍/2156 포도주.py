def max_wine(n, wines):
    # DP 테이블 초기화
    dp = [0] * (n+1)
    dp[1] = wines[0]
    if n > 1:
        dp[2] = wines[0] + wines[1]

    # DP를 이용하여 문제 해결
    for i in range(3, n+1):
        dp[i] = max(dp[i-1], dp[i-2] + wines[i-1], dp[i-3] + wines[i-2] + wines[i-1])

    return dp[n]

n = int(input())
wines = []
for _ in range(n):
    wines.append(int(input()))
print(max_wine(n, wines))
