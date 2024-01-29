def is_promising(row):
    for before_row in range(row):
        # 같은 열이나 대각선에 위치하는 경우 체크
        if (graph_col[before_row] == graph_col[row] or
            abs(graph_col[before_row] - graph_col[row]) == abs(before_row - row)):
            return False
    return True

def dfs(row):
    global result
    if row == n:
        result += 1
        return
    for i in range(n):
        graph_col[row] = i  # 현재 행에 퀸을 놓음
        if is_promising(row):  # 유망성 검사
            dfs(row + 1)  # 다음 행으로 이동

n = int(input())  # 체스판의 크기 N 입력
graph_col = [0] * n  # 각 행의 퀸 위치를 저장하는 배열
result = 0  # 경우의 수를 저장할 변수
dfs(0)  # 첫 번째 행부터 시작
print(result)  # 결과 출력
