#도화지 역할을 할 배열, 가로세로 100
paper = [[[0] for _ in range(100)] for _ in range(100)]

#색종이 수 
confetti_num = int(input())

for i in range(confetti_num):
    confetti_x, confetti_y = map(int, input().split()) #색종이를 붙일 x,y 좌표
    for k in range(confetti_y, confetti_y+10): #색종이 크기 10x10 
        for j in range(confetti_x, confetti_x+10):
            paper[k][j] = 1 #붙여진 곳을 1로 변경 

is_attached = 0 #붙여진 영역 수 (넓이)
for i in range(100):
    for j in range(100):
        if paper[i][j] == 1:
            is_attached += 1 
        
print(is_attached)