
def calc_top_stacks(super_crane):
    my_input = open("Inputs/input-05.txt")
    curr_line = my_input.readline().rstrip()
    stacks = {}
    for i in range(1, 10):
        stacks[i] = []
    while curr_line[0] == "[":
        curr_char = 0
        curr_stack = 1
        while curr_char < len(curr_line):
            if curr_line[curr_char+1] != " ":
                stacks[curr_stack].insert(0, curr_line[curr_char+1])
            curr_char += 4
            curr_stack += 1
        curr_line = my_input.readline().rstrip()
    my_input.readline()
    curr_line = my_input.readline().rstrip()
    while curr_line:
        curr_split = curr_line.split(" ")
        move_count = int(curr_split[1])
        move_from = int(curr_split[3])
        move_to = int(curr_split[5])
        curr_line = my_input.readline().rstrip()
        if super_crane:
            buf = []
            for i in range(move_count):
                buf.insert(0, stacks[move_from].pop())
            for item in buf:
                stacks[move_to].append(item)
        else:
            for i in range(move_count):
                stacks[move_to].append(stacks[move_from].pop())
    top_row = ""
    for i in range(1, 10):
        if len(stacks[i]) > 0:
            top_row += stacks[i].pop()
    print(top_row)

if __name__ == "__main__":
    calc_top_stacks(False)
    calc_top_stacks(True)