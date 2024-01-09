import sys

while True:
    n = int(sys.stdin.readline())
    if n == -1:
        break
    divisors = [m for m in range(1, n) if n % m == 0]
    if sum(divisors) == n:
        divisors_str = " + ".join(map(str, divisors))
        print(f"{n} = {divisors_str}")
    else:
        print(f"{n} is NOT perfect.")