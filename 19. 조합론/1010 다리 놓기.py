from math import factorial
def calculate_bridge_cases(n, m):
    return factorial(m) // (factorial(n) * factorial(m - n))

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    print(calculate_bridge_cases(N, M))