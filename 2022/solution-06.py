from collections import deque

def solution_06(option):
    input = open("Inputs/input-06.txt")
    curr = input.readline().rstrip()
    seen = []
    msg_marker = []
    first = 0
    first_msg = 0
    for i, c in enumerate(curr):
        if len(set(seen)) >= 4 and first == 0:
            first = i
        if len(set(msg_marker)) >= 14:
            first_msg = i
            break
        if len(seen) > 3:
            seen.pop(0)
        seen.append(c)
        if len(msg_marker) > 14:
            msg_marker.pop(0)
        msg_marker.append(c)
    print(first)
    print(first_msg)




if __name__ == "__main__":
    solution_06(False)