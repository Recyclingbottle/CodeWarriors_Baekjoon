import sys

input_str = sys.stdin.readline().rstrip()
croatian_alphabets = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

count = 0
i = 0

while i < len(input_str):
    if input_str[i:i+3] in croatian_alphabets:
        #3글자 패턴 확인하기 
        count+=1
        i+=3
    elif input_str[i:i+2] in croatian_alphabets:
        #2글자 
        count+=1
        i+=2
    else:
        #아니라면 그냥 알파벳으로 
        count +=1
        i +=1
print(count)