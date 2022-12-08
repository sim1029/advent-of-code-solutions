from collections import deque

def solution_07(option):
    input = open("Inputs/input-07.txt")
    global curr
    global curr_dir
    global curr_total
    curr = input.readline().rstrip()
    file_sizes = {"/": 0}
    directories = {"/": set()}
    curr_dir = "/"
    while curr:
        # get commands
        if curr[0] == "$":
            command = curr.split(" ")
            if command[1] == "cd":
                if command[2] == "/":
                    curr_dir = "/"
                elif command[2] == "..":
                    sep = curr_dir.split("/")
                    minus = sep[:-2]
                    curr_dir = "/".join(minus) + "/"
                else:
                    curr_dir += command[2] + "/"
                    if curr_dir not in file_sizes:
                        file_sizes[curr_dir] = 0
                        directories[curr_dir] = set()
                curr = input.readline().rstrip()
            elif command[1] == "ls":
                curr = input.readline().rstrip()
                while curr and curr[0] != "$":
                    listing = curr.split(" ")
                    if listing[0] == "dir":
                        directories[curr_dir].add(curr_dir + listing[1] + "/")
                    else:
                        file_sizes[curr_dir] += int(listing[0])
                    curr = input.readline().rstrip()
        else:
            print("ERORR not a command")

    total_sizes = {}
    for dir in file_sizes.keys():
        if dir in total_sizes:
            continue
        dir_tree = deque()
        curr_total = file_sizes[dir]
        for unseen_dir in directories[dir]:
            dir_tree.append(unseen_dir)
        while len(dir_tree) > 0:
            curr_dir = dir_tree.popleft()
            if curr_dir in total_sizes:
                curr_total += total_sizes[curr_dir]
            else:
                if len(directories[curr_dir]) > 0:
                    for rec_dir in directories[curr_dir]:
                        dir_tree.append(rec_dir)
                curr_total += file_sizes[curr_dir]
        total_sizes[dir] = curr_total

    ans = 0
    for total in total_sizes.values():
        if total <= 100000:
            ans += total
    print(ans)

    min_delete = float('inf')
    threshold = 30000000 - (70000000 - total_sizes["/"])
    for total in total_sizes.values():
        if total >= threshold:
            min_delete = min(min_delete, total)
    print(min_delete)

if __name__ == "__main__":
    solution_07(False)