def merge_sort(arr, p, r, k, storage):
    if p < r:
        q = (p + r) // 2
        merge_sort(arr, p, q, k, storage)
        merge_sort(arr, q + 1, r, k, storage)
        merge(arr, p, q, r, k, storage)

def merge(arr, p, q, r, k, storage):
    temp = []
    i, j = p, q + 1
    while i <= q and j <= r:
        if arr[i] <= arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1
        storage['count'] += 1
        if storage['count'] == k:
            storage['kth_value'] = temp[-1]
    while i <= q:
        temp.append(arr[i])
        i += 1
        storage['count'] += 1
        if storage['count'] == k:
            storage['kth_value'] = temp[-1]
    while j <= r:
        temp.append(arr[j])
        j += 1
        storage['count'] += 1
        if storage['count'] == k:
            storage['kth_value'] = temp[-1]
    for i, val in enumerate(temp):
        arr[p + i] = val

N, K = map(int, input().split())
A = list(map(int, input().split()))

storage = {'count': 0, 'kth_value': -1}

merge_sort(A, 0, N-1, K, storage)

print(storage['kth_value'])
