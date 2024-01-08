import sys 

word = sys.stdin.readline().strip()

first_appearance = [-1] * 26 

for i in range(len(word)):
    char = word[i]
    index = ord(char) - ord('a') #알파벳 인덱스를 계산하는 방법, 아스키 코드 사용
    if first_appearance[index] == -1:
        first_appearance[index] = i

for index in first_appearance:
    print(index, end = ' ')