def partition(arr, p, r):
    t_arr = arr
    x = t_arr[r]
    i = p - 1
    for j in range(p, r):
        if t_arr[j] <= x:
            i += 1
            (t_arr[i], t_arr[j]) = (t_arr[j], t_arr[i])

    (t_arr[i + 1], t_arr[r]) = (t_arr[r], t_arr[i + 1])
    return i + 1


def quicksort(arr, start, stop):
    new_arr = arr
    if start < stop:
        q = partition(new_arr, start, stop)
        print(new_arr)
        quicksort(new_arr, start, q - 1)
        quicksort(new_arr, q + 1, stop)



a = [10, 1, 5, 2, 15, 34, 21, 42, 36, 45, 61, 1]
quicksort(a, 0, len(a) - 1)