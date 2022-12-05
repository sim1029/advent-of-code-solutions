def solution_06(option):
    input = open("Inputs/input-05.txt")
    curr = input.readline().rstrip()
    while curr:
        print(curr)
        curr = input.readline().rstrip()


if __name__ == "__main__":
    solution_06(False)