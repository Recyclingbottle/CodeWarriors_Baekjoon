def gcd(a,b):
    while b!=0:
        a, b = b, a % b
    return a 

n = int(input())
trees = [int(input()) for _ in range(n)]

intervals = [trees[i+1] - trees[i] for i in range(n-1)]

ideal_interval = intervals[0]
for interval in intervals[1:]:
    ideal_interval = gcd(ideal_interval, interval)

new_trees = 0
for interval in intervals:
    new_trees += (interval // ideal_interval) - 1

print(new_trees)