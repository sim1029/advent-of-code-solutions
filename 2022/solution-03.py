def calc_priorities():
    my_input = open("Inputs/input-03.txt")
    currLine = my_input.readline().rstrip()
    total = 0
    while(currLine):
        left = set()
        right = set()
        for i in range(len(currLine)):
            if i < len(currLine) // 2:
                left.add(currLine[i])
            else:
                right.add(currLine[i])
        diff_arr = left.intersection(right)
        if len(diff_arr) > 0:
            diff = diff_arr.pop()
            total += calc_ord(diff)
        currLine = my_input.readline().rstrip()
    print(total)

def calc_badges():
    my_input = open("Inputs/input-03.txt")
    line1 = my_input.readline().rstrip()
    line2 = my_input.readline().rstrip()
    line3 = my_input.readline().rstrip()
    total = 0
    while line1 and line2 and line3:
        set1, set2, set3 = set(), set(), set()
        for i in range(max(len(line1), len(line2), len(line3))):
            if i < len(line1):
                set1.add(line1[i])
            if i < len(line2):
                set2.add(line2[i])
            if i < len(line3):
                set3.add(line3[i])
        int1 = set1.intersection(set2)
        diff_set = int1.intersection(set3)
        diff = diff_set.pop()
        total += calc_ord(diff)
        line1 = my_input.readline().rstrip()
        line2 = my_input.readline().rstrip()
        line3 = my_input.readline().rstrip()
    print(total)

def calc_ord(l):
    if l.isupper():
        score = ord(l) - ord("A") + 27
    else:
        score = ord(l) - ord("a") + 1
    return score

if __name__ == '__main__':
    calc_priorities()
    calc_badges()