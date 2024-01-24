recursion_count = 0

def recursion(s, l, r):
    global recursion_count
    recursion_count += 1  
    
    if l >= r: return 1
    elif s[l] != s[r]: return 0
    else: return recursion(s, l+1, r-1)

def isPalindrome(s):
    global recursion_count
    recursion_count = 0
    
    result = recursion(s, 0, len(s)-1)
    return result, recursion_count

T = int(input())
for _ in range(T):
    S = input()
    result, count = isPalindrome(S)
    print(f"{result} {count}")
