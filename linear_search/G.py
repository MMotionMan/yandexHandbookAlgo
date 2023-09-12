N = int(input())
a = list(map(int, input().split()))

if a[0] > a[1]:
    min_arr = [a[1], a[0]]
else:
    min_arr = [a[0], a[1]]
for i in range(2, len(a)):
    if a[i] < min_arr[1]:
        if a[i] < min_arr[0]:
            min_arr[1] = min_arr[0]
            min_arr[0] = a[i]
        else:
            min_arr[1] = a[i]

for item in min_arr:
    print(item, end=' ')