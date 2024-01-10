import sys

n = int(sys.stdin.readline())
points = []
for _ in range(n):
    x,y = map(int, sys.stdin.readline().split())
    points.append((x,y))

#초기 최소 최대 좌표 설정 
min_x = float('inf')
max_x = float('-inf')
min_y = float('inf')
max_y = float('-inf')

# 최소, 최대 좌표 갱신
for x, y in points:
    min_x = min(min_x, x)
    max_x = max(max_x, x)
    min_y = min(min_y, y)
    max_y = max(max_y, y)

# 직사각형의 넓이 계산
area = (max_x - min_x) * (max_y - min_y)
print(area)