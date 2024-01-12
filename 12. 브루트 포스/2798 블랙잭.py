import sys

n, m = map(int, sys.stdin.readline().split())
input_arr = list(map(int, sys.stdin.readline().split()))
result = 0

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1,n):
            if input_arr[i] + input_arr[j] + input_arr[k] > m:
                continue
            else:
                result = max(result, input_arr[i] + input_arr[j] + input_arr[k])

print(result)