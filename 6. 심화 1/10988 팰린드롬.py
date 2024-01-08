import sys
def is_palindrome(input_str):
    input_str = input_str.lower() 
    reversed_str = input_str[::-1]
    return input_str == reversed_str

input_str = sys.stdin.readline().strip()
if is_palindrome(input_str):
    print(1)
else:
    print(0)