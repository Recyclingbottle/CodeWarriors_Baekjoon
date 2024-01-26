import sys
input = sys.stdin.readline

def DFS(N, M, sequence=[]):
    # 수열의 길이가 M에 도달했을 때, 수열을 출력하고 재귀 호출을 종료
    if len(sequence) == M:
        print(' '.join(map(str, sequence)))
        return
    
    for i in range(1, N + 1):
        # 현재 수열에 i가 포함되어 있지 않으면 추가
        if i not in sequence:
            sequence.append(i)  # 숫자 i를 수열에 추가
            DFS(N, M, sequence)  # 다음 숫자를 선택하기 위해 재귀 호출
            sequence.pop() # 백트래킹: 마지막에 추가된 숫자를 제거하고 다음 선택을 위해 되돌림

N, M = map(int, input().strip().split())
DFS(N,M)