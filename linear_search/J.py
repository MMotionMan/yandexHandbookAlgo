N = int(input())
max1 = 0
max2 = 0
for score in input().split():
    score = int(score)
    if score > max2:
        if score > max1:
            max2 = max1
            max1 = score
        elif score == max1:
            pass
        else:
            max2 = score

print(max2)