
def solution_09(length):
    input = open("Inputs/input-09.txt")
    seen = set()
    curr = input.readline().rstrip()
    knots = [[0, 0] for _ in range(length)]
    while curr:
        instruction = curr.split(" ")
        for i in range(int(instruction[1])):
            if instruction[0] == "U":
                knots[0][1] += 1
            elif instruction[0] == "D":
                knots[0][1] -= 1
            elif instruction[0] == "L":
                knots[0][0] -= 1
            else:
                knots[0][0] += 1
            for i in range(1, length):
                the_next = next_cords(knots[i - 1], knots[i])
                knots[i] = the_next
            seen.add((knots[length-1][0], knots[length-1][1]))
        curr = input.readline().rstrip()
    print(len(seen))

def next_cords(x, y):
    xdist = abs(x[0] - y[0])
    ydist = abs(x[1] - y[1])
    if xdist > 1:
        if ydist > 0:
            if y[1] > x[1]:
                y[1] -= 1
            else:
                y[1] += 1
        if y[0] > x[0]:
            y[0] -= 1
        else:
            y[0] += 1
    elif ydist > 1:
        if xdist > 0:
            if y[0] > x[0]:
                y[0] -= 1
            else:
                y[0] += 1
        if y[1] > x[1]:
            y[1] -= 1
        else:
            y[1] += 1
    return y


if __name__ == "__main__":
    solution_09(2)
    solution_09(10)
