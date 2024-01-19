import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    ps = input().strip()  # 문자열의 끝에 있는 개행 문자를 제거합니다.
    stack = []  # 각 테스트 케이스마다 새 스택을 사용합니다.
    is_valid = True  # 괄호 문자열의 유효성을 추적하는 플래그

    for char in ps:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                is_valid = False  # 유효하지 않은 경우 플래그를 False로 설정
                break  # 더 이상 확인할 필요 없으므로 반복문 탈출
            stack.pop()
    
    # 스택이 비어 있고 유효성 플래그가 True인 경우만 "YES"
    print("YES" if not stack and is_valid else "NO")

