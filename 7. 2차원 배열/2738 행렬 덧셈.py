def read_matrix(n,m):
    #n행 m열 크기의 행렬을 사용자에게 입력받기
    matrix = []
    for _ in range(n): #사용자 입력 한 줄에 한 행을 다 입력받으니 n번 반복
        row = list(map(int, input().split())) #한 줄 읽고 row 라는 변수에 리스트 형태로 저장
        matrix.append(row) #리스트 형태 변수 row 를 matrix의 n번째 행으로 지정 
    return matrix    

def add_matrices(a,b):
    #두 행렬을 더해주는 함수 
    n = len(a) #행렬의 행 크기를 len함수를 통해 읽기
    m = len(a[0]) #행렬의 열 크기를 0번째 행의 길이를 len 함수로 읽기

    # 결과를 저장할 행렬 초기화
    #result = [[0 for _ in range(m)] for _ in range(n)]
    result = []
    for i in range(n):
        result.append([0] * m)


    for i in range(n):
        for j in range(m):
            result[i][j] = a[i][j] + b[i][j]
    return result

# 행렬의 크기 N과 M을 입력받음
n, m = map(int, input().split())

# 행렬 A와 B를 입력받음
matrix_a = read_matrix(n, m)
matrix_b = read_matrix(n, m)

# 행렬 A와 B를 더함
result_matrix = add_matrices(matrix_a, matrix_b)

# 결과 출력
for row in result_matrix:
    print(' '.join(map(str, row)))