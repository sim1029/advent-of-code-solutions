
def count_calories():
    input = open("Inputs/input-01.txt")
    nextLine = input.readline()
    maxCals = 0
    currCals = 0
    elfCals = []
    while nextLine:
        if nextLine == "\n":
            maxCals = max(maxCals, currCals)
            elfCals.append(currCals)
            currCals = 0
        else:
            currCals += int(nextLine)
        nextLine = input.readline()
    print("Max cals:", maxCals);
    elfCals.sort(reverse=True)
    print("Sum of top 3 cals:", elfCals[0] + elfCals[1] + elfCals[2])



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    count_calories()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
