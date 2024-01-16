import sys

n, m = map(int, sys.stdin.readline().split())

n_set = set(sys.stdin.readline().strip() for _ in range(n))
m_set = set(sys.stdin.readline().strip() for _ in range(m))

common_elements = n_set & m_set
#common_elements = n_set.intersection(m_set)
print(len(common_elements))
for ele in sorted(common_elements):
    print(ele)