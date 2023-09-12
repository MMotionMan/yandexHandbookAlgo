from tqdm import tqdm


def approximate_binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    while left < right - 1:
        mid = (left + right) // 2
        if arr[mid] == target:
            return arr[mid]
        elif target > arr[mid]:
            left = mid
        elif target < arr[mid]:
            right = mid

    if abs(arr[right] - target) >= abs(arr[right - 1] - target):
        return arr[right - 1]
    else:
        return arr[right]


N, K = input().split()
N, K = int(N), int(K)

main_arr = list(map(int, input().split()))
target_arr = list(map(int, input().split()))

ans_arr = []

for item in tqdm(target_arr):
    ans_arr.append(approximate_binary_search(main_arr, item))

for item in ans_arr:
    print(item)
