n = int(input())
members = []

for _ in range(n):
    age, name = input().split()
    members.append((int(age), name))

# 나이를 기준으로 정렬
sorted_members = sorted(members, key=lambda member: member[0])

for member in sorted_members:
    print(member[0], member[1])