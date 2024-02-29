n, m = map(int, input().split())
a = list(map(int, input().split()))

# 누적 합 배열 계산
s = [0] * (n+1)
for i in range(1, n+1):
    s[i] = s[i-1] + a[i-1]

# 나머지에 대한 카운트 배열
remainder_count = [0] * m
for sum_value in s:
    remainder_count[sum_value % m] += 1

# 조건을 만족하는 구간의 개수 계산
result = 0
for count in remainder_count:
    if count > 1:
        result += count * (count - 1) // 2

print(result)
