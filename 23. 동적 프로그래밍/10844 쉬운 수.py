MOD = 1000000000

def count_stair_numbers(N):
    dp = [[0] * 10 for _ in range(N+1)]

    # N=1일 때 초기화
    for i in range(1, 10):
        dp[1][i] = 1

    # N>=2일 때, DP를 이용해 계산
    for i in range(2, N+1):
        for j in range(10):
            if j == 0:
                dp[i][j] = dp[i-1][1]
            elif j == 9:
                dp[i][j] = dp[i-1][8]
            else:
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

    # 길이 N의 계단 수의 총 개수를 MOD로 나눈 나머지 반환
    return sum(dp[N]) % MOD

n = int(input())
print(count_stair_numbers(n)) 
