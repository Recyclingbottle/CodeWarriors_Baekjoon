import sys

n = sys.stdin.readline()

sorted_n = ''.join(sorted(n,reverse=True))
print(sorted_n)