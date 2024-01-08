import sys

words = []
for i in range(5):  
  word = sys.stdin.readline().rstrip()
  words.append(word)

#글자수에 제한이 있다 
#최대 15개의 글자로 이루어진다한다
for i in range(15): #최대 15글자
  for j in range(5): #5개의 단어가 존재함
    if i < len(words[j]): #최대 15글자 단어가 5개, 
      #만약 지금 선택된 j 번째 단어의 길이가 i 보다 작으면 의미는 단어가 끝나면 if 문을 통과한다는 뜻이다
      print(words[j][i], end="")
