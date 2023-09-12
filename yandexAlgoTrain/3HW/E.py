m = int(input())

witnesses = []

for i in range(m):
    witnesses.append(set(map(str, input().strip())))

n = int(input())

criminals = []

counter = [0 for j in range(n)]

for i in range(n):
    criminals.append(list(map(str, input().strip())))
    t_criminals = set(criminals[i])

    for j in range(m):
        if len(t_criminals & witnesses[j]) == len(witnesses[j]):
            counter[i] += 1

maximum = max(counter)

for i in range(len(counter)):
    if counter[i] == maximum:
        print(''.join(criminals[i]))

