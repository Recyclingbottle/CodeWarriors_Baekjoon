import sys

def Binary_Search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1 
        else:
            start = mid + 1 
    return False

n = int(sys.stdin.readline())
n_arr = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
m_arr = list(map(int, sys.stdin.readline().split()))

n_arr.sort()

for i in range(m):
    if Binary_Search(n_arr, m_arr[i], 0, n-1) is not False:
        print(1, end=' ')
    else:
        print(0, end= ' ')