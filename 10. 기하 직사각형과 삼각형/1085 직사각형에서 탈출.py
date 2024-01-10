import sys

x, y, w, h = map(int, sys.stdin.readline().split())

# x와 y가 각각 w와 h 범위 내에 있는지 확인
if x >= 1 and y >= 1 and x <= w - 1 and y <= h - 1:
    # 직사각형 내부에 있는 경우
    distance = min(x, y, w - x, h - y)  # 네 방향 중 가장 가까운 거리 계산
else:
    # 직사각형 외부에 있는 경우
    distance = min(x, y, w - x, h - y, 0)  # 직사각형 경계선까지 가는 거리 계산

print(distance)
