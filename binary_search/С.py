def bin_search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return "YES"
        elif target < arr[mid]:
            right = mid - 1
        elif target > arr[mid]:
            left = mid + 1

    return "NO"


N, K = input().split()
N, K = int(N), int(K)

main_arr = list(map(int, input().split()))
target_arr = list(map(int, input().split()))

for item in target_arr:
    print(bin_search(main_arr, item))
