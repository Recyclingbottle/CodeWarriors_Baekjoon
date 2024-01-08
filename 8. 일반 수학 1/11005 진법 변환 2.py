import sys

# 10진법 수와 목표 진법을 입력받음
N, b = map(int, sys.stdin.readline().split())
ary = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
result = ""

# N을 b로 나눈 나머지를 구하고, 이를 해당하는 진법의 숫자로 변환하여 결과 문자열에 추가
while N > 0:
    result = ary[N % b] + result
    N //= b

print(result)
