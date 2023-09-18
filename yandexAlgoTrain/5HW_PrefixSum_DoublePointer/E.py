def create_arr():
    t_arr = list(map(int, input().split()))[1:]

    complete_arr = [t_arr[0]]

    j = 1

    for i in range(1, len(t_arr)):
        if complete_arr[i - j] == t_arr[i]:
            j += 1
        else:
            complete_arr = (t_arr[i], i)
    t_arr.sort()
    return t_arr

n = int(input())

arr1 = create_arr()
arr2 = create_arr()
arr3 = create_arr()

print(arr1)
print(arr2)
print(arr3)

answer = None


if answer is not None:
    print(*answer)
else:
    print(-1)
