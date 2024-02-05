def find_min_cost(cost, N):
    dp = [[0 for _ in range(3)] for _ in range(N)]

    for color in range(3):
        dp[0][color] = cost[0][color]

    for i in range(1, N):
        dp[i][0] = cost[i][0] + min(dp[i-1][1], dp[i-1][2])
        dp[i][1] = cost[i][1] + min(dp[i-1][0], dp[i-1][2])
        dp[i][2] = cost[i][2] + min(dp[i-1][0], dp[i-1][1])

    return min(dp[N-1][0], dp[N-1][1], dp[N-1][2])

# 집의 수 입력 받기 
N = int(input())
# 각 집을 빨강, 초록, 파랑으로 칠하는 비용 입력 받기
cost = []
for _ in range(N):
    cost.append(list(map(int, input().split())))

# 최소 비용 계산 및 출력
min_cost = find_min_cost(cost, N)
print(min_cost)

