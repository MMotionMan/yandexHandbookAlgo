n = 10
street = list(map(int, input().split()))

left_distance = [0] * 10

max_distance = 0

left_mag = -20
right_mag = 20
for i in range(n):
    if street[i] == 1:
        left_distance[i] = abs(i - left_mag)

    elif street[i] == 2:
        left_mag = i

ans = 0

for j in range(n - 1, -1, -1):
    if street[j] == 1:
        right_distance = min(right_mag - j, left_distance[j])
        ans = max(ans, right_distance)

    elif street[j] == 2:
        right_mag = j


print(ans)