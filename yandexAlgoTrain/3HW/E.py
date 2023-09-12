def count_similarity(arr1, arr2):
    s = 0
    for item1 in arr1:
        if item1 in arr2:
            s += 1

    if abs(len(arr1) - len(arr2)) == len(arr2) - s:
        return True
    else:
        return False


m = int(input())

witnesses = []

for i in range(m):
    witnesses.append(list(map(str, input().strip())))

n = int(input())

criminals = []

counter = [0 for j in range(n)]

for i in range(n):
    criminals.append(list(map(str, input().strip())))
    for j in range(m):
        if count_similarity(witnesses[j], criminals[i]):
            counter[i] += 1


maximum = max(counter)

for i in range(len(counter)):
    if counter[i] == maximum:
        print(''.join(criminals[i]))