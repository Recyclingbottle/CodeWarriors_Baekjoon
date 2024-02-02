T = int(input())
p = [0, 1, 1, 1, 2, 2] + [0]*95  

def dp(n):
    if n < len(p) and p[n] != 0: 
        return p[n]
    if n < 1:  
        return 0
    if n < 3:  
        return 1
    if n == 3:  
        return 1
    if n == 4:  
        return 2
    if n == 5:  
        return 2
    for i in range(6, n+1):  
        p[i] = p[i-1] + p[i-5]
    return p[n]

for _ in range(T):
    N = int(input())
    print(dp(N))
