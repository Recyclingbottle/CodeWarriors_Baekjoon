n = int(input())
company = set()

for _ in range(n):
    name, status = input().split()
    if status == 'enter':
        company.add(name)
    elif status == 'leave':
        company.remove(name)

for name in sorted(company, reverse=True):
    print(name)