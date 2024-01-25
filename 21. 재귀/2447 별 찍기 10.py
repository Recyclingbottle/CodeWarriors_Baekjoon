def draw_stars(n):
    if n == 1:
        return ['*']
    Stars = draw_stars(n//3)
    pattern = []
    for star in Stars:
        pattern.append(star * 3)
    for star in Stars:
        pattern.append(star + ' ' * (n//3) + star)
    for star in Stars:
        pattern.append(star * 3)
    return pattern

N = int(input())
stars = draw_stars(N)
for star in stars:
    print(star)
