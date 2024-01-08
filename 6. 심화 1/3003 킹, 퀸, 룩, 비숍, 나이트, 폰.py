current_p = list(map(int, input().split()))

correct_p = [1,1,2,2,2,8]

missing_p = [correct_p[i] - current_p[i] for i in range(len(correct_p))]

print(*missing_p)