import sys

n1, n2 = map(str, sys.stdin.readline().split())

#뒤집기, 파이썬의 문자열 슬라이싱을 이용하는 방법
#문자열 슬라이싱
#일반적인 구문 'start:stop:step' 으로 되어 있다 
#구문에서 start는 시작 인덱스, stop은 종료 인덱스, step은 간격을 뜻한다
#[::-1]: 시작과 종료 인덱스를 모두 생략하고 간격을 -1로 지정한 경우, 문자열을 뒤집습니다. 즉, 문자열을 역순으로 만듭니다.
n1_r = n1[::-1]
n2_r = n2[::-1]

n1_int = int(n1_r)
n2_int = int(n2_r)

if n1_int > n2_int:
    print(n1_int)
else:
    print(n2_int)