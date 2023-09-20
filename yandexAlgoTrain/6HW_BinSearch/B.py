def left_bin_search(arr, target):
    l = 0
    r = len(arr) - 1
    while l < r:
        avg = (l + r) // 2
        if arr[avg] >= target:
            r = avg
        else:
            l = avg + 1

    if arr[l] != target:
        return 0
    else:
        return l + 1


def right_bin_search(arr, target):
    l = 0
    r = len(arr) - 1
    while l < r:
        avg = (l + r + 1) // 2
        if arr[avg] > target:
            r = avg - 1
        else:
            l = avg

    if arr[l] != target:
        return 0
    else:
        return l + 1

n = int(input())
n_arr = sorted(list(map(int, input().split())))

k = int(input())
target_arr = list(map(int, input().split()))
for item in target_arr:
    left = right = item
    print(left_bin_search(n_arr, right), right_bin_search(n_arr, left), end='\n')
