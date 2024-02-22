N = int(input())
A = list(map(int, input().split()))

increase = [1 for _ in range(N)]
decrease = [1 for _ in range(N)]

for i in range(N):
    for j in range(i):
        if A[j] < A[i]:
            increase[i] = max(increase[i], increase[j]+1)

for i in range(N-1,-1,-1):
    for j in range(N-1, i ,-1):
        if A[j] < A[i]:
            decrease[i] = max(decrease[i], decrease[j] + 1)
        
    
max_length = 0
for i in range(N):
    max_length = max(max_length, increase[i] + decrease[i] - 1)

print(max_length)