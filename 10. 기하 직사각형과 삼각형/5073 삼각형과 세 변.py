while True:
    # 세 변의 길이 입력받기
    a, b, c = map(int, input().split())
    
    # 입력이 0 0 0인 경우 종료
    if a == 0 and b == 0 and c == 0:
        break
    
    # 가장 긴 변의 길이 찾기
    max_length = max(a, b, c)
    
    # 삼각형의 조건을 만족하지 못하는 경우
    if a + b + c - max_length <= max_length:
        print("Invalid")
    else:
        # 세 변의 길이에 따라 삼각형의 종류 판단
        if a == b == c:
            print("Equilateral")
        elif a == b or b == c or a == c:
            print("Isosceles")
        else:
            print("Scalene")
