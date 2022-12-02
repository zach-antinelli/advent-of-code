INPUT = open('input.txt').read().splitlines()

def partOne(inputStrategy):
    total = 0
    for i in INPUT:
        op, me = i.split()
        total += {'X': 1,'Y': 2, 'Z': 3}[me]
        total += {  ('A', 'X'): 3, ('A', 'Y'): 6, ('A', 'Z'): 0,
                    ('B', 'Y'): 3, ('B', 'Z'): 6, ('B', 'X'): 0,
                    ('C', 'Z'): 3, ('C', 'X'): 6, ('C', 'Y'): 0  }[(op, me)]
    return total

print('Total number of points for part one:', partOne(INPUT))

def partTwo(inputStrategy):
    total = 0
    for i in INPUT:
        op, me = i.split()
        total += {'X': 0,'Y': 3, 'Z': 6}[me]
        total += {  ('A', 'X'): 3, ('A', 'Y'): 1, ('A', 'Z'): 2,
                    ('B', 'Y'): 2, ('B', 'Z'): 3, ('B', 'X'): 1,
                    ('C', 'Z'): 1, ('C', 'X'): 2, ('C', 'Y'): 3  }[(op, me)]
    return total

print('Total number of points for part two:', partTwo(INPUT))

