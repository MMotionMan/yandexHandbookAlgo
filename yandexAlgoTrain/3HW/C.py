a = list(map(int, input().split()))

ans = [0] * (max(a) + 1)

for item in a:
    ans[item] += 1


for i in range(len(a)):
    if ans[a[i]] == 1:
        print(a[i], end=' ')
