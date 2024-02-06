n = int(input())
triangle = []

# 삼각형 데이터 입력받기
for _ in range(n):
    triangle.append(list(map(int, input().split())))

# 동적 프로그래밍을 위한 2차원 DP 테이블 초기화
dp = [[0] * n for _ in range(n)]
dp[0][0] = triangle[0][0]

# 삼각형의 각 층을 순회하며, 각 위치에서의 최대 합 계산
for i in range(1, n):
    for j in range(i + 1):
        # 왼쪽 대각선 위에서 내려오는 경우
        if j > 0:
            left_up = dp[i-1][j-1]
        else:
            left_up = 0
        
        # 바로 위에서 내려오는 경우 (오른쪽 대각선을 고려하지 않음, 삼각형의 형태상 바로 위에서 내려올 수 없음)
        if j < i:
            up = dp[i-1][j]
        else:
            up = 0
        
        # 현재 위치에서의 최대 합 업데이트
        dp[i][j] = max(left_up, up) + triangle[i][j]

# 마지막 층에서의 최대값 찾기
result = max(dp[n-1])

print(result)
