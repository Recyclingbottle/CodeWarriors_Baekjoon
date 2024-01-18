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

def next_prime(n):
    while True:
        if is_prime(n):
            return n
        n += 1

test_case_number = int(input())

for _ in range(test_case_number):
    n = int(input())
    result = next_prime(n)
    print(result)