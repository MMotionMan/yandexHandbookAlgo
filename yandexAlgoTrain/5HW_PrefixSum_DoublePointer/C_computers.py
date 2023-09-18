def read_num():
    x = list(map(int, input().split()))
    for i in range(len(x)):
        x[i] = (x[i], i)
    x.sort()

    return x


n, m = map(int, input().split())

groups = read_num()
rooms = read_num()

answer = []

group_counter = 0

j = 0

for i in range(len(groups)):

    while j < len(rooms) and rooms[j][0] <= groups[i][0]:
        j += 1

    if j == len(rooms):
        break

    group_counter += 1
    answer.append(rooms[j])
    j += 1

if len(answer) > 0:
    print(group_counter)
    for room in answer:
        print(room[1] + 1, end=' ')
else:
    print(group_counter)
    print(group_counter)
