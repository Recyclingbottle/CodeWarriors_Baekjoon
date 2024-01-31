import sys

#연산하는 함수
def calculate(op, a, b):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        # 음수 나눗셈 처리
        if a * b < 0 and a % b != 0:
            return a // b + 1
        return a // b

# 백트래킹
def backtrack(index, current_result):
    global addition_count, subtraction_count, multiplication_count, division_count

    if index == n:
        results.add(current_result)
        return
    
    if addition_count > 0:
        addition_count -= 1
        backtrack(index + 1, calculate('+', current_result, input_arr[index]))
        addition_count += 1
    
    if subtraction_count > 0:
        subtraction_count -= 1
        backtrack(index + 1, calculate('-', current_result, input_arr[index]))
        subtraction_count += 1
    
    if multiplication_count > 0:
        multiplication_count -= 1
        backtrack(index + 1, calculate('*', current_result, input_arr[index]))
        multiplication_count += 1
    
    if division_count > 0:
        division_count -= 1
        backtrack(index + 1, calculate('/', current_result, input_arr[index]))
        division_count += 1    
    
input = sys.stdin.readline

n = int(input())
input_arr = list(map(int, input().strip().split()))

addition_count, subtraction_count, multiplication_count, division_count = map(int, input().strip().split())

results = set()

backtrack(1, input_arr[0])
print(max(results))
print(min(results))
