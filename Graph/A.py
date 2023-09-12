N = int(input())
a = []
for i in range(N):
    row = list(map(int, input().split()))
    a.append(row)


s = 0

for i in range(N):
    for j in range(i, N):
        if a[i][j] == 1:
            s += 1

print(s)