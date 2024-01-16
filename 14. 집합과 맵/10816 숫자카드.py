import sys
from collections import Counter

n = int(sys.stdin.readline())
n_arr = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
m_arr = list(map(int, sys.stdin.readline().split()))

# 상근이가 가진 카드에 대한 각 숫자의 출현 횟수 세기
counter = Counter(n_arr)

# 각 숫자가 몇 개 있는지 출력
for num in m_arr:
    print(counter[num], end=' ')