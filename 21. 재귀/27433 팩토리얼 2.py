def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
       return num *  factorial(num-1)

import sys
input = sys.stdin.readline

N = int(input())

print(factorial(N))