import sys, math

a,b,v = map(int, sys.stdin.readline().split())

#print(v/(a-b))
days = math.ceil((v - a) / (a - b)) + 1

print(days)