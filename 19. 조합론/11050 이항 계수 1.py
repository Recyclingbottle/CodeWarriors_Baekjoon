def factorial(n):
    if n == 0:
        return 1
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def binomial_coefficient(N, K):
    return factorial(N) // (factorial(K) * factorial(N - K))
N, K = map(int, input().split())
print(binomial_coefficient(N, K))
