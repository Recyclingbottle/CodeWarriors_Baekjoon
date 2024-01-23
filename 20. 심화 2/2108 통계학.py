import sys
from collections import Counter

# 입력
n = int(sys.stdin.readline())
numbers = [int(sys.stdin.readline().strip()) for _ in range(n)]

# 산술평균
mean_value = round(sum(numbers) / n)

# 중앙값
numbers.sort()
median_value = numbers[n // 2]

# 최빈값: 가장 많이 나타나는 값 중 두 번째로 작은 값
counter = Counter(numbers)
frequencies = counter.most_common()
if len(frequencies) > 1 and frequencies[0][1] == frequencies[1][1]:
    # 빈도수가 같은 값들만 추출하여 정렬
    same_freq_values = [val for val, count in frequencies if count == frequencies[0][1]]
    mode_value = sorted(same_freq_values)[1]  # 두 번째로 작은 값
else:
    mode_value = frequencies[0][0]

# 범위
range_value = numbers[-1] - numbers[0]

# 출력
print(mean_value)
print(median_value)
print(mode_value)
print(range_value)
