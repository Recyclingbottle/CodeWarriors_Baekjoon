N = int(input())

if N == 1:
    # N이 1인 경우 아무것도 출력하지 않음
    pass
else:
    divisor = 2
    while N > 1:
        if N % divisor == 0:
            print(divisor)
            N //= divisor
        else:
            divisor += 1
