input_file = open('input.txt', 'r').read().splitlines()
pairs = [i for i in input_file]


def part_one():
    count = 0
    for pair in pairs:
        a, b = pair.split(',')
        a = [int(i) for i in a.split('-')]
        b = [int(i) for i in b.split('-')]
        if a[0] <= b[0] and a[1] >= b[1]:
            count += 1
        elif b[0] <= a[0] and b[1] >= a[1]:
            count += 1
    print('Part one answer:', count)

def part_two():
    count = 0
    for pair in pairs:
        a, b = pair.split(',')
        a = [int(i) for i in a.split('-')]
        b = [int(i) for i in b.split('-')]
        if a[0] in range(b[0], b[1] + 1) or a[1] in range(b[0], b[1] + 1):
            count += 1
        elif b[0] in range(a[0], a[1] + 1) or b[1] in range(a[0], a[1] + 1):
            count += 1
    print('Part two answer:', count)

part_one()
part_two()
