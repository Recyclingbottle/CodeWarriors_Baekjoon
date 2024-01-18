import sys

a, b = map(int, sys.stdin.readline().split())
a_set = set(map(int, sys.stdin.readline().split()))
b_set = set(map(int, sys.stdin.readline().split()))

# a_b_set = a_set - b_set
# b_a_set = b_set - a_set

# result_set = a_b_set.union(b_a_set)

result_set = a_set ^ b_set

print(len(result_set))

