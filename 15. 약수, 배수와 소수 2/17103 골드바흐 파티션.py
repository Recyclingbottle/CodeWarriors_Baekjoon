def sieve_of_eratosthenes(n):
    prime = [True for _ in range(n+1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
    return [p for p in range(2, n+1) if prime[p]]

def goldbach_partitions_count(n, primes_set):
    count = 0
    for p in primes:
        if p > n // 2:
            break
        if (n - p) in primes_set:
            count += 1
    return count

# 주어진 범위 내의 모든 소수를 찾기
max_num = 1000000
primes = sieve_of_eratosthenes(max_num)
primes_set = set(primes)

# 테스트 케이스를 입력받고 결과를 계산
T = int(input())
for _ in range(T):
    N = int(input())
    print(goldbach_partitions_count(N, primes_set))
