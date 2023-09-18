num_messages = int(input())

dict_titles = {}

messages_links = [0] * (num_messages + 1)

titles_counter = 0

for i in range(1, num_messages + 1):
    num = int(input())
    if num == 0:
        title = input()
        message_text = input()
        dict_titles[i] = [title, 0]

        messages_links[i] = num

    else:
        message_text = input()

        messages_links[i] = num

        prev = i
        next = num
        while next != 0:
            prev = next
            next = messages_links[next]

        dict_titles[prev][1] += 1

max_counter = -1
max_ptr = -1

for key, value in dict_titles.items():
    if value[1] > max_counter:
        max_counter = value[1]
        max_ptr = key

print(dict_titles[max_ptr][0])

