l, k = map(int, input().split())

coords = list(map(int, input().split()))

avg = l // 2


if (l % 2 == 1) and (avg in coords):
    print(avg)

else:
    for i in range(len(coords)):
        if coords[i + 1] >= avg:
            print(coords[i], coords[i + 1])
            break
