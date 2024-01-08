import sys

T = int(sys.stdin.readline())
for _ in range(T):
    #readline() 을 사용하면 표준 입력에서 한 줄 씩 읽어오게 된다
    #이때 '\n' 개행 문자를 포함하기 때문에 이를 주의한다 
    str = sys.stdin.readline().strip() #strip()을 통해 개행 문자를 제거할 수 있다
    length = len(str)
    print(str[0], str[-1], sep='')