N = int(input())
line = list(map(int, input().split()))

stack = []
current = 1

for student in line:
    while stack and stack[-1] == current:
        stack.pop()
        current += 1
    if student == current:
        current += 1
    else:
        stack.append(student)

while stack and stack[-1] == current:
    stack.pop()
    current += 1

if current - 1 == N:
    print("Nice")
else:
    print("Sad")
