
def solution_10(length):
    input = open("Inputs/input-10.txt")
    curr = input.readline().rstrip()
    register = 1  # Tracks CPU register
    executing = False
    total = 0
    interval = 21
    for i in range(1, length+1):
        # Update total at start of each instruction
        if interval == 40:
            total += i * register
            interval = 1
        else:
            interval += 1

        instruction = curr.split(" ")
        if len(instruction) > 1 and not executing:
            executing = True
        elif executing:
            executing = False
            register += int(instruction[1])
            curr = input.readline().rstrip()
        else:
            curr = input.readline().rstrip()
    print("Total:", total)

    input = open("Inputs/input-10.txt")
    curr = input.readline().rstrip()

    screen = [[False for j in range(40)] for i in range(6)] #Tracks pixels state
    register = 1
    executing = False
    for i in range(len(screen)):
        for j in range(len(screen[i])):
            if register-1 <= j <= register+1:
                screen[i][j] = True

            instruction = curr.split(" ")
            if len(instruction) > 1 and not executing:
                executing = True
            elif executing:
                executing = False
                register += int(instruction[1])
                curr = input.readline().rstrip()
            else:
                curr = input.readline().rstrip()

    #print out CPU state
    for row in screen:
        for col in row:
            if col:
                print("#", end="", sep="")
            else:
                print(".", end="", sep="")
        print()

#ZUPRFECL

if __name__ == "__main__":
    solution_10(220)
