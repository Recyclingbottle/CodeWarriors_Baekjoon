n = int(input())
coords = list(map(int, input().split()))

# 좌표를 정렬하고, 중복을 제거하여 서로 다른 좌표만을 가진 리스트 생성
unique_coords = sorted(set(coords))

# 각 좌표에 대한 압축된 좌표 값을 저장하는 딕셔너리 생성
coord_dict = {coord: i for i, coord in enumerate(unique_coords)}

# 각 좌표를 압축된 좌표 값으로 치환
compressed_coords = [coord_dict[coord] for coord in coords]

print(*compressed_coords)