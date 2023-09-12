def max_in_col(matr):
    max_l = matr[0]
    for i in range(len(matr[0])):
        for j in range(len(matr)):
            if matr[j][i] > max_l[i]:
                max_l[i] = matr[j][i]

    return max_l


def min_in_row(matr):
    min_l = [matr[j][0] for j in range(len(a))]
    for i in range(len(matr)):
        for j in range(len(matr[0])):
            if matr[i][j] < min_l[i]:
                min_l[i] = matr[i][j]

    return min_l


n, m = input().split()
n, m = int(n), int(m)
a = []
for i in range(n):
    a.append(list(map(int, input().split())))

min_list = min_in_row(a)
max_list = max_in_col(a)

s = 0

for i in range(n):
    for j in range(m):
        if (a[i][j] == min_list[i]) and (a[i][j] == max_list[j]):
            s += 1

print(s)
