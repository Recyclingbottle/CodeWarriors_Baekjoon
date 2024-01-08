x = int(input())

line = 0 #대각선 라인
max_num = 0 #해당하는 라인에 최대 분수 번호 

while x > max_num:
    line += 1
    max_num += line

diff = max_num - x
if line % 2 == 0:
    numerator = line - diff  # 분자
    denominator = diff + 1  # 분모
else:  # 홀수 라인일 경우 (왼쪽 아래로 이동)
    numerator = diff + 1  # 분자
    denominator = line - diff  # 분모

print(f"{numerator}/{denominator}")