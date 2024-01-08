import sys

input_str = sys.stdin.readline().rstrip().upper()

alphabet_count = [0] * 26

for char in input_str:
    if 'A' <= char <= 'Z':
        index = ord(char) - ord('A')
        alphabet_count[index] += 1

max_count = max(alphabet_count)
most_frequent_alphabet = chr(ord('A')+ alphabet_count.index(max_count))

if alphabet_count.count(max_count) >= 2:
    print("?")
else:
    print(most_frequent_alphabet)
