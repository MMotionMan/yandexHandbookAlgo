
dict_words = {}

with open('input.txt', 'r') as f:
    for line in f:
        line = line.split()
        for word in line:
            if word in dict_words.keys():
                dict_words[word] -= 1
            else:
                dict_words[word] = -1

answer = []

for key, value in dict_words.items():
    answer.append((value, key))

answer = sorted(answer)

for key, value in answer:
    print(value)
