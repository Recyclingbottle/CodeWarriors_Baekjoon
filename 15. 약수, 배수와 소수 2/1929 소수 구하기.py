def is_prime(num):
    if num <= 1:
        return False
    if num == 2 or num == 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i*i <= num:
        if num % i == 0  or num % (i+2) == 0:
            return False
        i += 6
    return True

m, n = map(int, input().split())

result = []
for i in range(m,n+1):
    if is_prime(i):
        result.append(i)

for res in result:
    print(res)