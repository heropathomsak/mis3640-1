# team = 'New England Patriots'

# print(type(team))
# a = team[0]
# print(a)
# print(team[4])
# print(len(team))
# print(team[19])
# print(team[-1])


team = 'New England Patriots'

# for i in range(len(team)):
#     print(team[i], end=" ")

# for whatever in team:
#     print(whatever)


prefixes = 'JKLMNOPQ'
suffix = 'ack'
for letter in prefixes:
    # if letter == "O" or letter == "Q":
    # if letter in 'OQ':
    if letter in ['O', 'Q']:
        print(letter + "u" + suffix)
    else:
        print(letter + suffix)
