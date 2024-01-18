S = input().strip()

substrings = set()

for start in range(len(S)):
    for end in range(start + 1, len(S) + 1):
        substrings.add(S[start:end])

print(len(substrings))
