import sys

while True:
    input_str = sys.stdin.readline().rstrip()  # rstrip()을 사용하여 개행 문자 제거
    if not input_str:  # 더 이상 입력이 없으면 종료
        break
    print(input_str)

#다른 사람이 어떻게 풀었는 지 확인
import sys
for line in sys.stdin:
    print(line, end="")