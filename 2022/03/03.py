import string

INPUT = open('input.txt').read().splitlines()
orderedDict = dict(zip(string.ascii_lowercase, range(1, 27)))
orderedDict.update(dict(zip(string.ascii_uppercase, range(27, 53))))

def ruckSackSum(input):
    total = 0
    for rucksack in input:
        c1, c2 = rucksack[:len(rucksack)//2], rucksack[len(rucksack)//2:]
        compartments = [ c1, c2 ]
        commonChar = [char for char in set.intersection(*map(set, compartments))]
        total += orderedDict[commonChar[0]]
    return total

def splitList(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]

def badgeSum(input):
    total = 0
    for group in list(splitList(input, 3)):
        e1, e2, e3 = group[0], group[1], group[2]
        elfGroup = [ e1, e2, e3 ]
        commonChar = [char for char in set.intersection(*map(set, elfGroup))]
        total += orderedDict[commonChar[0]]
    return total 
    
print('Part one:', ruckSackSum(INPUT))
print('Part two:', badgeSum(INPUT))