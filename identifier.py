def getCommand(command):  # Program to get number identifier
    index = -1

    if command[0] == '|':
        pass
    elif command[0] == 'O':
        if len(command) == 5:
            index = 2
        else:
            index = 1
    elif command == '1/2 1/2':
        index = 12
    elif command[0] in ["R", "N", "B", "Q", "K"]:
        if command[1] == 'x':
            if command[-1] == '+':
                index = 10
            else:
                index = 8
        elif command[-1] == '#':
            index = 11
        elif command[-1] == '+':
            index = 9
        else:
            index = 7
    elif '=' in command:
        if command[-1] == '+':
            index = 14
        else:
            index = 13
        try:
            if command[2] == 'x':
                index += 2
        except IndexError:
            pass
    elif (command[0] in ["a", "b", "c", "d", "e", "f", "g", "h"]) and (command[1] in ["1", "2", "3", "4", "5", "6", "7", "8"]):
        try:
            if command[-1] == '#':
                index = 6
            elif command[2] == 'x':
                index = 3
                if command[-1] == '+':
                    index = 5
            elif command[-1] == '+':
                index = 4
            else:
                index = 0
        except IndexError:
            index = 0

    return index