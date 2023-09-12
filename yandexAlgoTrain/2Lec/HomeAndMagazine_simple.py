n = 10

street = list(map(int, input().split()))

max_dist = 0

for i in range(n):
    left = i - 1
    right = i + 1
    min_dist = -1

    if street[i] == 1:
        while True:
            if left < 0:
                if street[right] == 2:
                    min_dist = right - i
                    break

                right += 1

            elif right >= n:
                if street[left] == 2:
                    min_dist = i - left
                    break
                left -= 1

            else:
                if street[right] == 2:
                    min_dist = right - i
                    break
                if street[left] == 2:
                    min_dist = i - left
                    break

                left -= 1
                right += 1

    if min_dist > max_dist:
        max_dist = min_dist

print(max_dist)