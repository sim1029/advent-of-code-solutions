


def solution_11(rounds):
    class Monkey:
        def __init__(self, items, equation, divisibility, true_monkey, false_monkey):
            self.items = items
            self.equation = equation
            self.divisibility = divisibility
            self.true_monkey = true_monkey
            self.false_monkey = false_monkey
            self.inspections = 0


    input = open("Inputs/input-11.txt")
    curr = input.readline().rstrip()

    monkies = []
    divis_factor = 1
    while curr:
        if curr.startswith("Monkey"):

            # Get a list of the item values
            items = input.readline().rstrip().split(":")[1].split(",")
            stripped = []
            for item in items:
                stripped.append(int(item.strip()))

            # Get the Monkey's equation
            equation = input.readline().rstrip().split(":")[1].split("=")[1].lstrip()

            # Get divisibility factor
            divisibility = int(input.readline().rstrip().split(":")[1].lstrip().split(" ")[2])
            divis_factor *= divisibility

            # Get next monkey
            true_monkey = int(input.readline().rstrip().split(':')[1].lstrip().split(" ")[3])
            false_monkey = int(input.readline().rstrip().split(':')[1].lstrip().split(" ")[3])

            # Create new monkey
            monkies.append(Monkey(stripped, equation, divisibility, true_monkey, false_monkey))

        curr = input.readline().rstrip()
        if not curr:
            curr = input.readline().rstrip()

    for i in range(rounds):
        for monkey in monkies:
            curr = []
            for j in range(len(monkey.items)):
                curr.append(monkey.items.pop(0))
            for old in curr:
                worry = eval(monkey.equation)
                worry %= divis_factor
                if worry % monkey.divisibility == 0:
                    monkies[monkey.true_monkey].items.append(worry)
                else:
                    monkies[monkey.false_monkey].items.append(worry)
                monkey.inspections += 1

    first, second = 0, 0
    for monkey in monkies:
        if monkey.inspections > first:
            first = monkey.inspections
    for monkey in monkies:
        if monkey.inspections > second and monkey.inspections != first:
            second = monkey.inspections
    print(first * second)

if __name__ == "__main__":
    solution_11(10000)
