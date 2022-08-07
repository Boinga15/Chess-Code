from identifier import getCommand

lines = [] # Code lines

# Prepare database and variables
database = []
for i in range(0, 8):
    line = []
    for j in range(0, 8):
        line.append(0)
    database.append(line)

variables = [0, 0, 0, 0, 0]

# Get coding lines
f = open("code.txt", 'r')
for line in f.readlines():
    if line.strip() != "" and line.strip() != " ":
        lines.append(line.strip())
f.close()

# Identifiers
letters = ["a", "b", "c", "d", "e", "f", "g", "h"]
pieces = ["R", "N", "B", "Q", "K"]

# Compiler
outputASCII = False
counter = 0

def setCounterBack():
    global counter

    buffer = 0
    for j in range(1, counter + 1):
        line = lines[counter - j]
        if '=' in line:
            buffer += 1
        elif line == "1/2 1/2":
            if buffer > 0:
                buffer -= 1
            else:
                counter = counter - j
                break

while counter < len(lines):
    chosenIndex = getCommand(lines[counter])
    i = lines[counter]
    if chosenIndex == -1:
        pass
    else:
        match chosenIndex:
            case 0:
                if outputASCII:
                    print(chr(database[letters.index(i[0])][int(i[1]) - 1]), end='')
                else:
                    print(database[letters.index(i[0])][int(i[1]) - 1], end='')
            case 1:
                outputASCII = True
            case 2:
                outputASCII = False
            case 3:
                database[letters.index(i[0])][int(i[1]) - 1] = database[letters.index(i[3])][int(i[4]) - 1]
            case 4:
                database[letters.index(i[0])][int(i[1]) - 1] += 1
            case 5:
                database[letters.index(i[0])][int(i[1]) - 1] += database[letters.index(i[3])][int(i[4]) - 1]
            case 6:
                try:
                    database[letters.index(i[0])][int(i[1]) - 1] = int(input("> "))
                except ValueError:
                    raise Exception("ERROR ENCOUNTERED - LINE " + str(lines.index(i) + 1) + ": Expected number, non numeric input given.")
            case 7:
                variables[pieces.index(i[0])] = database[letters.index(i[1])][int(i[2]) - 1]
            case 8:
                database[letters.index(i[2])][int(i[3]) - 1] = variables[pieces.index(i[0])]
            case 9:
                variables[pieces.index(i[0])] += database[letters.index(i[1])][int(i[2]) - 1]
            case 10:
                database[letters.index(i[2])][int(i[3]) - 1] += variables[pieces.index(i[0])]
            case 11:
                try:
                    value = int(input("> "))
                    variables[pieces.index(i[0])] = value
                    database[letters.index(i[1])][int(i[2]) - 1] = value
                except ValueError:
                    raise Exception("ERROR ENCOUNTERED - LINE " + str(lines.index(i) + 1) + ": Expected number, non numeric input given.")
            case 12:
                pass
            case 13:
                if database[letters.index(i[0])][int(i[1]) - 1] == variables[pieces.index(i[3])]:
                    setCounterBack()
            case 14:
                if database[letters.index(i[0])][int(i[1]) - 1] != variables[pieces.index(i[3])]:
                    setCounterBack()
            case 15:
                if database[letters.index(i[0])][int(i[1]) - 1] == variables[pieces.index(i[6])] and database[letters.index(i[0])][int(i[1]) - 1] == database[letters.index(i[3])][int(i[4]) - 1]:
                    setCounterBack()
            case 16:
                if database[letters.index(i[0])][int(i[1]) - 1] != variables[pieces.index(i[6])] and database[letters.index(i[0])][int(i[1]) - 1] != database[letters.index(i[3])][int(i[4]) - 1]:
                    setCounterBack()
    
    counter += 1