def hanoi(n, start, end, aux):
    if n == 1:
        print(start, end)
        return
    # n-1개의 원판을 aux 장대로 이동
    hanoi(n-1, start, aux, end)
    # 가장 큰 원판을 목적지로 이동
    print(start, end)
    # n-1개의 원판을 aux 장대에서 목적지로 이동
    hanoi(n-1, aux, end, start)

N = int(input())
# 옮긴 횟수는 2^N - 1
print(2**N - 1)
hanoi(N, 1, 3, 2)
