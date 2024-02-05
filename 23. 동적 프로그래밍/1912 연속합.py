import sys
def max_subarray_sum(A):
    max_sum = current_sum = A[0]
    
    for i in range(1, len(A)):
        current_sum = max(A[i], current_sum + A[i])
        max_sum = max(max_sum, current_sum)
    
    return max_sum

input = sys.stdin.readline

n = int(input())
input_list = list(map(int, input().split()))

print(max_subarray_sum(input_list))
