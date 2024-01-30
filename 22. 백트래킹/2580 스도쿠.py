import sys
def check(row, col, sudoku):
    numbers = set(range(1, 10))  # 1부터 9까지 숫자들의 집합

    # 행과 열에서 사용된 숫자 제거
    for i in range(9):
        numbers.discard(sudoku[row][i])
        numbers.discard(sudoku[i][col])

    # 3x3 정사각형에서 사용된 숫자 제거
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            numbers.discard(sudoku[i][j])

    return numbers  # 사용 가능한 숫자들의 집합 반환

def solve_sudoku(sudoku, row=0, col=0):
    if row == 9:  # 모든 칸을 성공적으로 채웠다면 True 반환
        return True
    if col == 9:  # 한 줄의 끝에 도달했다면 다음 줄로 이동
        return solve_sudoku(sudoku, row + 1, 0)

    if sudoku[row][col] == 0:  # 빈 칸을 찾았다면
        for num in check(row, col, sudoku):
            sudoku[row][col] = num  # 숫자를 넣어본다
            if solve_sudoku(sudoku, row, col + 1):  # 다음 칸으로 이동
                return True
            sudoku[row][col] = 0  # 숫자가 맞지 않으면 0으로 되돌린다

        return False  # 빈 칸에 들어갈 수 있는 숫자가 없다면 False 반환
    else:  # 빈 칸이 아니면 다음 칸으로 이동
        return solve_sudoku(sudoku, row, col + 1)

# 스도쿠 퍼즐 입력 받기
input = sys.stdin.readline
input_sudoku = [] #스도쿠를 입력 받을 리스트

for _ in range(9):
    row = list(map(int, input().split())) #한줄씩 읽고 리스트에 삽입
    input_sudoku.append(row)

# 스도쿠 퍼즐을 풀어보자
if solve_sudoku(input_sudoku):
    for row in input_sudoku:
        print(' '.join(map(str, row)))
else:
    print("해결할 수 없는 스도쿠입니다.")
