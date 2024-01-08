import sys
def is_group_word(word):
    alphabet_seen = [False] * 26

    for i in range(len(word)):
        # 현재 문자가 이전 문자와 다르면
        if i > 0 and word[i] != word[i - 1]:
            # 현재 문자가 이미 등장한 문자라면 그룹 단어가 아님
            if alphabet_seen[ord(word[i - 1]) - ord('a')]:
                return False
            alphabet_seen[ord(word[i - 1]) - ord('a')] = True
    
    return True


N = int(sys.stdin.readline().rstrip())

group_word_count = 0

for _ in range(N):
    word = sys.stdin.readline().rstrip()
    if is_group_word(word):
        group_word_count += 1

print(group_word_count)