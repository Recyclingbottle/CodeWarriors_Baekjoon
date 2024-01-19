from collections import deque
import sys

input = sys.stdin.readline
N = int(input())

deque = deque()
for _ in range(N):
    command = input().split()
    cmd_type = command[0]

    if cmd_type == '1':
        deque.appendleft(command[1])
    elif cmd_type == '2':
        deque.append(command[1])
    elif cmd_type == '3':
        print(deque.popleft() if deque else -1)
    elif cmd_type == '4':
        print(deque.pop() if deque else -1)
    elif cmd_type == '5':
        print(len(deque))
    elif cmd_type == '6':
        print(0 if deque else 1)
    elif cmd_type == '7':
        print(deque[0] if deque else -1)
    elif cmd_type == '8':
        print(deque[-1] if deque else -1)
