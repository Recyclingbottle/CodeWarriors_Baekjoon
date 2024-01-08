import sys

#sys.stdin은 표준 입력의 끝(EOF)에 도달하면 반복이 중단된다
#파일의 끝에 도달하는 것은 사용자가 Ctrl+D (Unix/Linux) 또는 Ctrl+Z (Windows)를 누르거나 입력 스트림이 끝날 때 발생
for line in sys.stdin:
    A, B = map(int, line.split())
    print(A + B)
