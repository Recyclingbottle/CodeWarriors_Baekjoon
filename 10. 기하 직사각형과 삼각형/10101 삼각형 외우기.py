# 삼각형의 세 각 입력받기
angle1 = int(input())
angle2 = int(input())
angle3 = int(input())

# 세 각의 합이 180인지 확인
if angle1 + angle2 + angle3 == 180:
    # 모든 각이 60이면 Equilateral
    if angle1 == angle2 == angle3 == 60:
        print("Equilateral")
    # 두 각이 같으면 Isosceles
    elif angle1 == angle2 or angle1 == angle3 or angle2 == angle3:
        print("Isosceles")
    # 모든 각이 다르면 Scalene
    else:
        print("Scalene")
else:
    print("Error")
