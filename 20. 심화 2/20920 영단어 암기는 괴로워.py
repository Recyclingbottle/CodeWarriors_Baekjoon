import sys
from collections import Counter

# 입력 받기
N, M = map(int, input().split())
words = [sys.stdin.readline().strip() for _ in range(N)]

# 길이가 M 이상인 단어들만 필터링
filtered_words = [word for word in words if len(word) >= M]

# 단어 빈도 계산
word_counts = Counter(filtered_words)

# 정렬: 빈도수 내림차순 -> 길이 내림차순 -> 알파벳 오름차순
sorted_words = sorted(word_counts.keys(), key=lambda x: (-word_counts[x], -len(x), x))

# 출력
for word in sorted_words:
    print(word)
