s = input()

counter = 0

i = 0
for item in s:
    if item == '(':
        counter += 1
    else:
        counter -= 1

    if counter < 0:
        break

if counter == 0:
    print("YES")
else:
    print("NO")
