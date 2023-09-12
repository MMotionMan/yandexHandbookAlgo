n = int(input())

answer = set([_ for _ in range(1, n + 1)])

s = input()

while s != "HELP":
    nums = set(map(int, s.split()))
    s = input()

    if s == 'YES':
        answer.intersection_update(nums)

    elif s == 'NO':
        answer.difference_update(nums)

    s = input()

answer = sorted(answer)

print(*answer)
