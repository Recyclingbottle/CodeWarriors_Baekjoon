n = int(input())

numbers = []
numbers = list(map(int, input().split()))

prime_count = 0

for number in numbers:
    if number <= 1:
        continue
    is_prime = True
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            is_prime = False
            break
    if is_prime:
        prime_count += 1

print(prime_count)
