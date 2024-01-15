import sys

n = int(sys.stdin.readline())

temp = 0
title_num = 666
while True:
    if '666' in str(title_num):
        temp += 1 
    if temp == n:
        print(title_num)
        break
    title_num += 1 
