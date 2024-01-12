import sys
n, m = map(int, sys.stdin.readline().split())
board = []
result = []
for _ in range(n):
    board.append(sys.stdin.readline().strip())

for i in range(n-7):
    for j in range(m-7):
        is_black = 0
        is_white = 0

        for k in range(i,i+8):
            for l in range(j, j+8):
                if (k+l) % 2 == 0:
                    if board[k][l] != 'B':
                        is_black +=1
                    if board[k][l] != 'W':
                        is_white +=1
                else:
                    if board[k][l] != 'W':
                        is_black +=1
                    if board[k][l] != 'B':
                        is_white +=1
        result.append(is_black)
        result.append(is_white)
print(result)
print(min(result))