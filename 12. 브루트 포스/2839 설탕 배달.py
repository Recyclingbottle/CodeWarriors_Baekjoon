n = int(input())

result = 0
while n > 0:
    if n % 5 == 0:  # 5킬로그램 봉지로 정확히 나누어 떨어지는 경우
        result += n // 5
        n = 0
        break
    n -= 3  # 5킬로그램 봉지로 나누어 떨어지지 않으면 3킬로그램 봉지 사용
    result += 1

if n < 0:  # 정확한 무게를 만들 수 없는 경우
    result = -1

print(result)
