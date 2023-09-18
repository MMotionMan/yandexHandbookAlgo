import math


def get_command_name(string):
    return ' '.join(string[:len(string) - 1])


dict_commands = {}

with open('input.txt', 'r') as f:
    for line in f:
        line = line.split()
        line = (get_command_name(line), int(line[len(line) - 1]))
        for command, counter in [line]:
            if command in dict_commands.keys():
                dict_commands[command] += counter
            else:
                dict_commands[command] = counter

sum_votes = sum(dict_commands.values())
pointer = sum_votes / 450

empty_places = 450

commands_fraction = []

for key, value in dict_commands.items():
    votes_on_command = value // pointer

    empty_places -= int(votes_on_command)

    dict_commands[key] = int(votes_on_command)

    commands_fraction.append((value % pointer, votes_on_command, key))

commands_fraction = sorted(commands_fraction, reverse=True)

all_commands = len(dict_commands.keys())

for i in range(empty_places):
    dict_commands[commands_fraction[i % all_commands][2]] += 1

for key, value in dict_commands.items():
    print(key, value)
