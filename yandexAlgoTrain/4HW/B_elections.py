candidate = {}

with open('input.txt', 'r') as f:
    for line in f:
        name, counter = map(str, line.split())

        if name in candidate.keys():
            candidate[name] += int(counter)
        else:
            candidate[name] = int(counter)


candidate = dict(sorted(candidate.items()))


for key, value in candidate.items():
    print(key, value)