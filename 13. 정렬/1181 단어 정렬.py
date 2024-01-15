n = int(input())
words = set()

for _ in range(n):
    word = input()
    words.add(word)

# 단어 길이와 사전 순으로 정렬
sorted_words = sorted(words, key=lambda word: (len(word), word))

for word in sorted_words:
    print(word)