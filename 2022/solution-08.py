
def solution_08(option):
    input = open("Inputs/input-08.txt")
    grid = []
    curr = input.readline().rstrip()
    while curr:
        row = []
        for char in curr:
            row.append(int(char))
        grid.append(row)
        curr = input.readline().rstrip()
    seen = set()
    # right and left
    for i in range(len(grid)):
        l = 0
        r = len(grid[i])-1
        high_left = -1
        high_right = -1
        while l < len(grid[i]) and r >= 0:
            if grid[i][l] > high_left and (i,l) not in seen:
                seen.add((i,l))
            high_left = max(high_left, grid[i][l])
            if grid[i][r] > high_right and (i,r) not in seen:
                seen.add((i,r))
            high_right = max(high_right, grid[i][r])
            l += 1
            r -= 1

    for j in range(len(grid[0])):
        t = 0
        b = len(grid)-1
        high_top = -1
        high_bottom = -1
        while t < len(grid[0]) and b >= 0:
            if grid[t][j] > high_top and (t,j) not in seen:
                seen.add((t,j))
            high_top = max(high_top, grid[t][j])
            if grid[b][j] > high_bottom and (b,j) not in seen:
                seen.add((b,j))
            high_bottom = max(high_bottom, grid[b][j])
            t += 1
            b -= 1
    print(len(seen))

    def rec_trav(prev, i, j, direc):
        if i >= len(grid) or i < 0:
            return 0
        if j >= len(grid[0]) or j < 0:
            return 0
        if grid[i][j] >= prev:
            return 1
        if direc == "LEFT":
            j += 1
        elif direc == "RIGHT":
            j -= 1
        elif direc == "TOP":
            i += 1
        elif direc == "BOTTOM":
            i -= 1
        else:
            print("UNSUPPORTED DIRECTION")
        return rec_trav(prev, i, j, direc) + 1

    most_seen = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            left = rec_trav(grid[i][j], i,j+1,"LEFT")
            right = rec_trav(grid[i][j], i, j-1, "RIGHT")
            top = rec_trav(grid[i][j], i+1, j, "TOP")
            bottom = rec_trav(grid[i][j], i-1, j, "BOTTOM")
            curr_score = left * right * top * bottom
            most_seen = max(most_seen, curr_score)
    print(most_seen)



if __name__ == "__main__":
    solution_08(False)