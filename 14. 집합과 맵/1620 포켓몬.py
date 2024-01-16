import sys

# 포켓몬의 개수 N과 문제의 개수 M을 입력받음
N, M = map(int, sys.stdin.readline().split())

# 포켓몬 이름과 번호를 매핑하는 두 딕셔너리
name_to_number = {}
number_to_name = {}

# 포켓몬 이름을 입력받고, 두 딕셔너리에 저장
for number in range(1, N + 1):
    name = sys.stdin.readline().strip()
    name_to_number[name] = number
    number_to_name[number] = name

# 문제를 하나씩 입력받아 답을 출력
for _ in range(M):
    query = sys.stdin.readline().strip()
    if query.isdigit():  # 숫자인 경우
        print(number_to_name[int(query)])
    else:  # 문자인 경우
        print(name_to_number[query])
