n = int(input())

pileup_n = 1
cnt = 1 

while n > pileup_n:
    pileup_n += 6*cnt #벌집은 6의 배수로 증가한다
    cnt += 1 #반복횟수 증가 시킴

print(cnt)