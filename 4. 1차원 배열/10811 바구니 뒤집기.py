import sys 

N, M = map(int, sys.stdin.readline().split())
arr = [0] * N 
for i in range(N):
    arr[i] = i+1

for _ in range(M):
    k, j = map(int, sys.stdin.readline().split())
    reverse_range = list(reversed(arr[k-1:j]))
    arr[k-1:j] = reverse_range
for ele in arr:
    print(ele, end=' ')

#수동으로 변경하기 위해서는? k 와 j 변경 후 k 는 한 칸 올리고 j 는 한 칸 내리고 계속 swap 해주는 방법
    # while k < j:
    # arr[k], arr[j] = arr[j], arr[k]
    # k += 1
    # k-= 1