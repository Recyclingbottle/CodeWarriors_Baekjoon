# 함수 f(n)의 계수와 상수를 입력받음
a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())

# O(n) 정의를 만족하는지 확인
def is_O_n(a1, a0, c, n0):
    for n in range(n0, 101):  # n0부터 100까지의 모든 n에 대해서 확인
        if a1 * n + a0 > c * n:
            return 0  # O(n) 정의를 만족하지 않음
    return 1  # 모든 n에 대해서 O(n) 정의를 만족

result = is_O_n(a1, a0, c, n0)
print(result)
