from collections import deque
import sys

input = sys.stdin.readline

N = int(input())
balloons = deque(enumerate(map(int, input().split()), start=1))

result = []

while balloons:
    idx, move = balloons.popleft()
    result.append(idx)

    if move > 0:
        balloons.rotate(-move +1) #오른쪽으로 이동
    else: 
        balloons.rotate(-move)#왼쪽으로 이동

print(' '.join(map(str, result)))
