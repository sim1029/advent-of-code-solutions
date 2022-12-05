def calc_full_dups():
    my_input = open("Inputs/input-04.txt")
    curr_line = my_input.readline().rstrip()
    total_overlap = 0
    any_overlap = 0
    while curr_line:
        ranges = curr_line.split(",")
        left = ranges[0].split('-')
        right = ranges[1].split('-')

        if int(right[0]) < int(left[0]):
            left, right = right, left
        elif int(right[0]) == int(left[0]):
            if (int(right[1]) > int(left[1])):
                left, right = right, left
        if (int(left[1]) >= int(right[1])):
            total_overlap += 1
        if (int(left[1]) >= int(right[0])):
            print(left, ",", right)
            any_overlap += 1
        curr_line = my_input.readline().rstrip()
    print(total_overlap)
    print(any_overlap)

if __name__ == "__main__":
    calc_full_dups()