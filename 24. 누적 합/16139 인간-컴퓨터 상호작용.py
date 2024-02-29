# 문자열 입력
string_input = input().strip()

# 쿼리 수 입력
query_count = int(input())

# 누적 합 배열 초기화
cumulative_sums = [[0 for _ in range(26)] for _ in range(len(string_input))]

# 첫 문자에 대한 누적 합 설정
cumulative_sums[0][ord(string_input[0]) - ord('a')] = 1

# 나머지 문자에 대한 누적 합 계산
for index in range(1, len(string_input)):
    cumulative_sums[index][ord(string_input[index]) - ord('a')] = 1
    for char_index in range(26):
        cumulative_sums[index][char_index] += cumulative_sums[index - 1][char_index]
        
# 쿼리 처리
for _ in range(query_count):
    char, start, end = input().split()
    start, end = int(start), int(end)
    # 구간 내 출현 횟수 계산
    if start > 0:
        result = cumulative_sums[end][ord(char) - ord('a')] - cumulative_sums[start - 1][ord(char) - ord('a')]
    else:
        result = cumulative_sums[end][ord(char) - ord('a')]
    # 결과 출력
    print(result)
