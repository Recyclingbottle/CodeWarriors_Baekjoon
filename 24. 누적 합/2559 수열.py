# 입력 받기
N, K = map(int, input().split()) # N은 전체 날짜의 수, K는 연속적인 날짜의 수
temperatures = list(map(int, input().split())) # 매일의 온도

# 슬라이딩 윈도우 초기화
current_sum = sum(temperatures[:K]) # 처음 K일 동안의 온도 합
max_sum = current_sum

# 슬라이딩 윈도우를 이용한 최대 온도 합 계산
for i in range(K, N):
    current_sum += temperatures[i] - temperatures[i-K]
    max_sum = max(max_sum, current_sum)

# 최대 온도 합 출력
print(max_sum)
