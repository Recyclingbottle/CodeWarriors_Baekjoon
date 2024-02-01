def fib_dynamic(n):
    # n이 1 또는 2일 경우 바로 1을 반환
    if n == 1 or n == 2:
        return 1

    # n이 3 이상일 경우, 동적 프로그래밍을 사용하여 계산
    f = [0] * (n + 1)
    f[1], f[2] = 1, 1

    for i in range(3, n + 1):
        f[i] = f[i - 1] + f[i - 2]

    return f[n]

# 주어진 n값에 대하여 동적 프로그래밍 방식의 피보나치 수 계산
n = int(input())
fib_number = fib_dynamic(n)

# 연산 횟수 출력 (동적 프로그래밍의 경우 n-2번 연산)
print(fib_number, n-2)
