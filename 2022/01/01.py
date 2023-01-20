input_file = open('input.txt').read()

def challenge(input):
    inputList = input.split('\n')
    results = []
    total = 0
    for i in inputList:
        if i == '':
            results.append(total)
            total = 0
            continue
        total = total + int(i)
    results.sort()
    print('Most calories held by one elf: ' + str(results[-1]))
    print('Calories held by top three elves combined: ' + str(results[-1] + results[-2] + results [-3]))

challenge(input_file)
