import sys
N, b = sys.stdin.readline().split()
ary = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

#뒤집기
N = N[::-1]
result = 0

#뒤집힌 N을 순회하면서 각 문자와 그 위치(i)를 얻고 
#해당하는 진법에 따라 계산 
for i,n in enumerate(N):
    result += (int(b)**i)*(ary.index(n))
print(result)


# enumerate() 함수는 Python에서 반복 가능한(iterable) 객체를 순회할 때, 
# 객체의 각 요소와 그 요소의 인덱스를 동시에 얻기 위해 사용된다.

# enumerate() 함수의 기본 구조
# enumerate(iterable, start=0)
# iterable: 순회할 반복 가능한 객체 (예: 리스트, 문자열, 튜플 등).
# start: 인덱스의 시작 숫자. 기본값은 0이지만, 필요에 따라 다른 시작 값을 지정할 수 있다

# 예시) 

# for index, element in enumerate(N):
#     # 여기서 index는 요소의 인덱스, element는 요소의 값
#     print(index, element)
