def create_prefix_sum(arr):
    t_prefix = [0]
    for i in range(1, len(arr) + 1):
        t_prefix.append(t_prefix[i - 1] + arr[i - 1])

    return t_prefix


n, q = map(int, input().split())

elements = list(map(int, input().split()))

prefix_sum = create_prefix_sum(elements)

s = ''

for i in range(q):
    left, right = map(int, input().split())
    s += str(prefix_sum[right] - prefix_sum[left - 1]) + '\n'

s = s[:len(s) - 1]

print(s)

