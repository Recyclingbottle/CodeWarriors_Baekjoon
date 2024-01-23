import sys
input = sys.stdin.readline

N = int(input())

chat_history = []
count = 0
for _ in range(N):
    input_chat = input().rstrip()
    if input_chat == "ENTER":
        chat_history = []
    else:
        if input_chat not in chat_history:
            count += 1 
            chat_history.append(input_chat)

print(count)
