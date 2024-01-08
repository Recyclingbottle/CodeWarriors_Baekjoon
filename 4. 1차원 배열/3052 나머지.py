import sys
arr = [0] * 10

for i in range(10):
    arr[i] = int(sys.stdin.readline())
    arr[i] = arr[i] % 42

#서로 다른 값 갯수 세기 
    
unique_val = set(arr) #중복 제거 집합으로 
count = len(unique_val) #중복 제거했으니 len 이 바로 중복되지 않은 서로 다른 값 갯수

print(count)