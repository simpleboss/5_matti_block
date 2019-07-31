front_look = [[0, 0, 0, 0] for i in range(4)]
side_look = [[0, 0, 0, 0] for i in range(4)]


def print_look():
    i = 0
    while i < len(front_look):
        print(str(i) + str(front_look[i]))
        i += 1
    print('')

    i = 0
    while i < len(side_look):
        print(str(i) + str(side_look[i]))
        i += 1


front_list = [1, 1, 1, 1]
side_list = [0, 1, 1, 0]

i = 0
while i < len(front_list):
    j = 0
    while j < len(side_list):
        if front_list[i] == 1 and side_list[j] == 1:
            front_look[i][j] = 1
            side_look[j][i] = 1
        j += 1
    i += 1

print_look()

