#학점을 평점으로 바꾸기 위한 딕셔너리 
grades = {
    'A+': 4.5,
    'A0': 4.0,
    'B+': 3.5,
    'B0': 3.0,
    'C+': 2.5,
    'C0': 2.0,
    'D+': 1.5,
    'D0': 1.0,
    'F': 0.0
}

total_points = 0 #모든 과목에서 얻은 총 점수 
total_credits = 0 #모든 과목의 총 학점 수 P 제외 

for _ in range(20):
    subject_name, credit, letter_grade = input().strip().split()
    credit = float(credit)
    
    if letter_grade != 'P':
        total_points += grades[letter_grade] * credit #총 점수는 모든 과목의 학점 x 평점을 더한 것
        total_credits += credit

gpa = total_points / total_credits
print(f"{gpa:.6f}")
