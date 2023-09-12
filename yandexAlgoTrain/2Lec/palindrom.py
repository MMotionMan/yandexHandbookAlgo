s = input()
i = 0
j = len(s) - 1
counter = 0
while i < j:
    if s[i] != s[j]:
        counter += 1
    i += 1
    j -= 1

print(counter)