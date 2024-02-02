def count_binary_sequences(N):
    # 초기 조건 설정
    dp = [0] * (N+1)
    dp[1] = 1
    if N >= 2:
        dp[2] = 2

    # 점화식에 따라 dp 배열 채우기
    for i in range(3, N+1):
        dp[i] = (dp[i-1] + dp[i-2]) % 15746

    # 길이가 N인 모든 2진 수열의 개수를 15746으로 나눈 나머지 반환
    return dp[N]

N = int(input())
print(count_binary_sequences(N))
