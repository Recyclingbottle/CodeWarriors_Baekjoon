import sys

# 출석번호를 저장할 리스트
submitted_numbers = [0] * 31  # 1부터 30까지의 출석번호를 저장하기 위해 31개의 원소를 가진 리스트 생성

# 입력 받기
for _ in range(28):
    submitted_number = int(sys.stdin.readline())
    submitted_numbers[submitted_number] = 1  # 제출한 학생의 출석번호를 해당하는 인덱스의 값으로 표시

# 제출되지 않은 학생의 출석번호 찾기
for i in range(1, 31):
    if submitted_numbers[i] == 0:  # 출석번호가 0이면 제출되지 않은 학생
        print(i)
        break

# 다음 출석번호 찾기
for i in range(i + 1, 31):
    if submitted_numbers[i] == 0:  # 출석번호가 0이면 제출되지 않은 학생
        print(i)
        break
