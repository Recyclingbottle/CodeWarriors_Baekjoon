def w(a, b, c, memo):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20, memo)
    if memo[a][b][c] != -1:
        return memo[a][b][c]
    if a < b and b < c:
        memo[a][b][c] = w(a, b, c-1, memo) + w(a, b-1, c-1, memo) - w(a, b-1, c, memo)
    else:
        memo[a][b][c] = w(a-1, b, c, memo) + w(a-1, b-1, c, memo) + w(a-1, b, c-1, memo) - w(a-1, b-1, c-1, memo)
    return memo[a][b][c]

# 메모이제이션을 위한 3차원 배열 초기화 (인덱스 조정 필요 없이 직접 사용 가능)
memo = [[[-1 for _ in range(51)] for _ in range(51)] for _ in range(51)]

while True:
    a, b, c = map(int, input().split())  # 사용자로부터 a, b, c 입력받기
    if a == -1 and b == -1 and c == -1:  # 모두 -1인 경우 반복문 종료
        break
    result = w(a, b, c, memo)  # w 함수를 호출하여 결과 계산
    print(f"w({a}, {b}, {c}) = {result}")  # 결과 출력
