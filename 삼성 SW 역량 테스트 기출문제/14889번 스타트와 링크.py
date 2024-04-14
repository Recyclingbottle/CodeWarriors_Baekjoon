import sys
input = sys.stdin.readline

def cal_diff(start_team, link_team):
    start_power = sum([S[i][j] for i in start_team for j in start_team])
    link_power = sum([S[i][j] for i in link_team for j in link_team])
    return abs(start_power - link_power)

def backtrack(index, team):
    global min_diff
    if len(team) == n // 2:
        start_team = team
        link_team = [x for x in range(n) if x not in start_team]
        diff = cal_diff(start_team, link_team)
        min_diff = min(min_diff, diff)
        return 
    for i in range(index, n):
        if i not in team:
            team.append(i)
            backtrack(i +1, team)
            team.pop()

n = int(input())
S = [list(map(int, input().split())) for _ in range(n)]

min_diff = float('inf')

backtrack(0, [])

print(min_diff)