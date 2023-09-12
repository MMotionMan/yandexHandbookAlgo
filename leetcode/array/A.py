height = list(map(int, input().split()))

i = 0
j = len(height) - 1
max_s = 0

while i < j:
    minimum = min(height[i], height[j])
    s = minimum * (j - i)
    if s > max_s:
        max_s = s

    if height[i] > height[j]:
        j -= 1
    else:
        i += 1

print(max_s)