N, K = map(int, input().split())  # 물품의 수 N, 가방에 넣을 수 있는 무게 K 입력 받기
Things = []  # 물품의 무게와 가치를 저장할 배열

# 입력 받아서 Things에 삽입
for i in range(N):
    w, v = map(int, input().split())  # 물품의 무게 w와 가치 v 입력 받기
    Things.append((w, v))

# 해를 담을 Pack 배열 초기화, 최적해는 Pack[N][K]
Pack = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

# 동적 프로그래밍으로 Pack 배열 채우기
for i in range(1, N + 1):
    for k in range(1, K + 1):
        if Things[i-1][0] > k:  # 물건 i의 무게가 임시 배낭 용량을 초과하면
            Pack[i][k] = Pack[i-1][k]
        else:  # 물건 i를 배낭에 담지 않을 경우와 담을 경우 각각을 고려
            Pack[i][k] = max(Pack[i-1][k], Pack[i-1][k - Things[i-1][0]] + Things[i-1][1])

print(Pack[N][K])  # 모든 물건의 가치 합(최적해) 출력
