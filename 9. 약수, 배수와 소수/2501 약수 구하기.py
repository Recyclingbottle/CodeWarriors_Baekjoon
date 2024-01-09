import sys

n, k = map(int, sys.stdin.readline().split())

m = 1
measure = []
while m <= n:
    if n % m == 0:
        measure.append(m)
    m += 1
    
if k <= len(measure):
    print(measure[k-1])
else:
    print(0)