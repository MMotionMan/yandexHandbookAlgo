def solve(arr):
    t_prefix = [0]
    for i in range(1, len(arr) + 1):
        t_prefix.append(t_prefix[i - 1] + arr[i - 1])

    return t_prefix


n = int(input())

elements = list(map(int, input().split()))

maximum = max(elements)

prefix_sum = solve(elements)

for i in range(len(prefix_sum)):
    for j in range(i, len(prefix_sum)):
        if i == j:
            if elements[i - 1] == maximum:
                maximum = elements[i - 1]

        elif prefix_sum[j] - prefix_sum[i] > maximum:
            maximum = prefix_sum[j] - prefix_sum[i]

print(maximum)