def calc_strategy():
    my_input = open("Inputs/input-02.txt")
    nextLine = my_input.readline()
    totalScore = 0
    scores = {"A": 1, "B": 2, "C": 3}
    outcomes = {"X": "A", "Y": "B", "Z": "C"}
    lines = 1
    while nextLine:
        moves = nextLine.rstrip().split(" ")
        if len(moves) == 2:
            lines += 1
            you = outcomes[moves[1]]
            them = moves[0]
            totalScore += scores[you]
            if (them == "A" and you == "B") or (them == "B" and you == "C") or (them == "C" and you == "A"):
                totalScore += 6
            elif them == you:
                totalScore += 3
        nextLine = my_input.readline()
    print("Total score:", totalScore)

def real_strategy():
    my_input = open("Inputs/input-02.txt")
    nextLine = my_input.readline()
    totalScore = 0
    scores = {"A": 1, "B": 2, "C": 3}
    win = {"A": "B", "B": "C", "C": "A"}
    lose = {"A": "C", "B": "A", "C": "B"}
    lines = 1
    while nextLine:
        moves = nextLine.rstrip().split(" ")
        if len(moves) == 2:
            lines += 1
            you = moves[1]
            them = moves[0]
            if you == "Z":
                totalScore += 6
                your_move = win[them]
            elif you == "Y":
                totalScore += 3
                your_move = them
            else:
                your_move = lose[them]
            totalScore += scores[your_move]

        nextLine = my_input.readline()
    print("Total score:", totalScore)

if __name__ == '__main__':
    calc_strategy()
    real_strategy()