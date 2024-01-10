lengths = sorted(map(int, input().split()))

# 가장 작은 두 막대를 합한 값과 세 번째 막대 중 작은 값을 선택하여 둘레를 계산
# 세 번째 막대가 너무 짧다면 첫 번째와 두 번째 막대를 최대한 합치기 위해 -1을 뺀다.
perimeter = lengths[0] + lengths[1] + min(lengths[2], lengths[0] + lengths[1] - 1)
    
print(perimeter)
