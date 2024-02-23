n = int(input())
connections = []
for _ in range(n):
    a,b = map(int, input().split())
    connections.append((a,b))

# a 전봇대 기준으로 정렬
connections.sort()

# b 전봇대 위치만 추출
b_positions = [b for a,b in connections]

dp = [1] * n
for i in range(n):
    for j in range(i):
        if b_positions[i] > b_positions[j]:
            dp[i] = max(dp[i], dp[j] +1)

print(n - max(dp))