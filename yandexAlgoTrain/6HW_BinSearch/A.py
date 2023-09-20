def left_bin_search(arr, target):
    l = -1
    r = len(arr)
    while r > l + 1:
        avg = (r + l) // 2
        if arr[avg] > target:
            r = avg
        else:
            l = avg

    return r


def right_bin_search(arr, target):
    l = -1
    r = len(arr)
    while r > l + 1:
        avg = (r + l) // 2
        if arr[avg] >= target:
            r = avg
        else:
            l = avg

    return r


n = int(input())
n_arr = sorted(list(map(int, input().split())))

k = int(input())
answer = []
for i in range(k):
    left, right = map(int, input().split())
    answer.append(left_bin_search(n_arr, right) - right_bin_search(n_arr, left))

print(*answer)
