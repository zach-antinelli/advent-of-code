crates, instructions = open('input.txt', 'r').read().split('\n\n')


def part_one():
    for c in crates:
        print(len(c) / 5)

#part_one()
