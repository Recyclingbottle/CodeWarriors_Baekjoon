def DFS(N, M, sequence=[], start=1):
    if len(sequence) == M:
        print(' '.join(map(str, sequence)))
        return
    
    for i in range(start, N + 1):
        sequence.append(i)
        DFS(N, M, sequence, i)  # i를 시작으로 하여 중복 선택을 허용
        sequence.pop()

N, M = map(int, input().split())
DFS(N, M)
