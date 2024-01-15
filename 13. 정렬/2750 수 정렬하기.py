import sys

n = int(sys.stdin.readline())

arr = []
for i in range(n):
    temp = int(sys.stdin.readline())
    arr.append(temp)

#arr.sort()
for i in range(len(arr)):
    for j in range(0, len(arr)-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            
for num in arr:
    print(num)