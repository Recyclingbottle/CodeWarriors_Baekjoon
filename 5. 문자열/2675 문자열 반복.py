import sys
T = int(sys.stdin.readline().strip())

for _ in range(T):
    R, S = sys.stdin.readline().split()
    R = int(R)
    result = ''
    
    for char in S:
        result += char * R
    
    print(result)