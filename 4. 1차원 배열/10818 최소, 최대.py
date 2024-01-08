import sys 

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
#map 함수가 iterable한 객체를 반환하는데, 한 번 이터레이션을 통해 데이터를 소비하면 다시 사용할 수 없기 때문에 list 로 변환하거나 다른 변수에 저장한 후 최소 최대값을 계산해야함
print(min(arr), max(arr))