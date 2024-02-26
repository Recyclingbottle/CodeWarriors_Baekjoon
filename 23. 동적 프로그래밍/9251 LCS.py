A_string = input().rstrip()
B_string = input().rstrip()

LCS = [[0] * (len(B_string) + 1) for _ in range(len(A_string) + 1)]

for i in range(1, len(A_string) + 1):
    for j in range(1, len(B_string) + 1):
        if A_string[i-1] == B_string[j-1]:
            LCS[i][j] = LCS[i-1][j-1] + 1
        else:
            LCS[i][j] = max(LCS[i-1][j], LCS[i][j-1])

print(LCS[-1][-1])
