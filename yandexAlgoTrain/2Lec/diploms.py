n = int(input())

folders = list(map(int, input().split()))

max_counter = 0

s = 0

for i in range(len(folders)):
    if folders[i] > max_counter:
        s += max_counter
        max_counter = folders[i]
    else:
        s += folders[i]

print(s)
