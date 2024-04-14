N = int(input())
T = []
P = []
    
for _ in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)
    
DP = [0] * (N+1)
    
for i in range(1, N+1):
    for j in range(1, i+1):
        if j + T[j-1] - 1 <= i:
            DP[i] = max(DP[i], DP[j-1] + P[j-1])
    
result = max(DP)

print(result)