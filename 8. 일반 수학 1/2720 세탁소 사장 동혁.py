t = int(input())

quater_num = 0
dime_num = 0
nickel_num = 0
penny = 0

for _ in range(t):
    quater_num = 0
    dime_num = 0
    nickel_num = 0
    penny = 0
    
    change = int(input()) 
    while change > 0:
        if change >= 25:
            quater_num += 1
            change -= 25
        elif change >= 10:
            dime_num += 1
            change -= 10
        elif change >= 5:
            nickel_num += 1
            change -= 5
        elif change >= 1:
            penny += 1
            change -= 1
    print(quater_num, dime_num, nickel_num, penny)