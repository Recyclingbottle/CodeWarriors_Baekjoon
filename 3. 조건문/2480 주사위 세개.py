dice = list(map(int, input().split()))

count = {}

for d in dice:
    if d in count:
        count[d] += 1 
    else:
        count[d] = 1

prize = 0
if 3 in count.values():
    prize = 10000 + dice[0] * 1000
elif 2 in count.values():
    for key, value in count.items():
        if value == 2:
            prize = 1000 + key * 100
            break
else:
    prize = max(dice) * 100 

print(prize)

