n = int(input())

box = {}

for i in range(n):
    key, value = map(int, input().split())
    if key in box.keys():
        box[key] += value
    else:
        box[key] = value

box = dict(sorted(box.items()))

for key, value in box.items():
    print(key, value)