with open('./data.txt') as f:
    lines = f.readlines()

nums = {
    63: '0',
    6: '1',
    91: '2',
    79: '3',
    102:'4',
    109:'5',
    125:'6',
    7:'7',
    127:'8',
    111:'9',
}

total = 0

for line in lines:
    lenMap = {
        5: [],
        6: [],
    }

    for word in line.split(' | ')[0].split(' '):
        stripped = word.strip()
        length = len(stripped)
        if length in [2,3,4,7]:
            lenMap[length] = stripped
        else:
            lenMap[length] += [stripped]

    # print(lenMap)
    one = lenMap[2]
    top = [x for x in lenMap[3] if not x in one][0]
    
    fgcand = [x for x in lenMap[4] if not x in one]

    three = [x for x in lenMap[5] if all([y in x for y in one])][0]
    middle = [x for x in fgcand if x in three][0]
    topleft = [x for x in fgcand if x != middle][0]
    bottom = [x for x in three if x not in (list(one) + [top, middle])][0]

    five = [x for x in lenMap[5] if topleft in x][0]

    bottomright = [x for x in one if x in five][0]
    topright = [x for x in one if x not in five][0]
    
    bottomleft = [x for x in lenMap[7] if x not in [top, middle, bottom, topleft, topright,bottomright]][0]

    mapping = {
        top: 1,
        topright:2,
        bottomright:4,
        bottom:8,
        bottomleft:16,
        topleft:32,
        middle:64
    }

    out = ""

    for word in line.split(' | ')[1].split(' '):
        sum = 0
        for char in word.strip():
            sum += mapping[char]

        out += nums[sum]

    total += int(out)

print(total)