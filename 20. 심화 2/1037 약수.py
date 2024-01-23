import sys
input = sys.stdin.readline

N = int(input())
divisors = list(map(int, input().split()))
    
min_divisor = min(divisors)
max_divisor = max(divisors)

result = min_divisor * max_divisor
print(result)