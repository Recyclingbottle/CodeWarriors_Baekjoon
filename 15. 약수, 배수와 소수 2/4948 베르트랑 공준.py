def is_prime(n):
    if n <= 1: 
        return False
    if n <= 3: 
        return True
    if n % 2 == 0 or n % 3 == 0: 
        return False
    i = 5 
    while i * i <= n: 
        if n % i == 0 or n % (i + 2) == 0: 
            return False
        i += 6
    return True

while True:
    n = int(input())
    if n == 0:
        break
    primes_n_to_2n = []
    for i in range(n+1,2*n + 1):
        if is_prime(i):
            primes_n_to_2n.append(i)
    print(len(primes_n_to_2n))