#입력 받을 행렬을 0으로 초기화
input_matrix = [[0 for _ in range(9)] for _ in range(9)]
#입력 받아서 input_matrix 업데이트
for i in range(9):
    row = list(map(int, input().split()))
    input_matrix[i] = row

max_value = 0 #최댓값을 저장할 변수 
n,m = 0, 0 #최댓값의 위치를 저장할 변수 
for i in range(9):
    for j in range(9):
        if(max_value < input_matrix[i][j]):
            max_value = input_matrix[i][j]
            n = i+1 #파이썬은 list 가 0 부터 시작이니 + 1 로 해준다
            m = j+1


print(max_value)
print(n, m)

# 1. 최대값을 저장하는 변수 이름을 max 로 했다는 점.
# 이는 max 함수와 혼동 될 수 있으니 주의

# 2. 최대값을 판별하기 위한 if 문에서 현재 저장된 max_value 값과 행렬 값을 비교할 때, 
# 작은지 만 비교 할 것이 아닌 작거나 "같은지" 판별해야한다
