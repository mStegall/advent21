import re

def add(num1,num2):
    return "[{},{}]".format(num1,num2)


numx = re.compile('\d+')
pairx = re.compile('\[(\d+),(\d+)\]')

def explode(num):
    depth = 0

    for i, char in enumerate(num):
        if char == '[':
            if depth >=4:
                exploder = pairx.match(num, pos=i)
                if exploder:
                    leftSide = num[:exploder.start()]
                    rightSide = num[exploder.end():]

                    leftNumB = numx.search(leftSide[::-1])
                    if leftNumB:
                        start = len(leftSide)-leftNumB.end()
                        end = len(leftSide) - leftNumB.start()
                        leftSide = leftSide[:start] +str(int(leftSide[start:end]) + int(exploder.groups()[0])) + leftSide[end:]



                    rightNum = numx.search(rightSide)
                    if rightNum:
                        rightSide= rightSide[:rightNum.start()] + str(int(rightNum.group()) + int(exploder.groups()[1])) + rightSide[rightNum.end():]
                    
                    return True, leftSide + '0' + rightSide                    

            depth += 1
        elif char == ']':
            depth -= 1

    return False, num

def split(num):
    twoDigit = re.compile('\d\d+')
    toSplit = twoDigit.search(num)
    if not toSplit:
        return False, num

    numToSplit = int(toSplit.group())
    left = numToSplit // 2
    right = numToSplit - left

    return True, num[:toSplit.start()] + add(left,right) + num[toSplit.end():]


def simplify(num):
    while True:
        exploding = True
        while exploding:
            exploding, num = explode(num)

        wasSplit, num = split(num)
        if not wasSplit:
            return num

def magnitude(num):
    while '[' in num:
        pair = pairx.search(num)
        mag = 3 * int(pair.groups()[0]) + 2 * int(pair.groups()[1])
        num = num.replace(pair.group(), str(mag))

    return num
        

with open('./data.txt') as f:
    lines = f.readlines()

highest = 0

for i, num1 in enumerate(lines):
    for num2 in lines[i+1:]:
        sum1 = int(magnitude(simplify(add(num1.strip(), num2.strip()))))
        sum2 = int(magnitude(simplify(add(num2.strip(), num1.strip()))))
        # print(num1, num2, sum1, sum2)
        highest = max(highest,sum1,sum2)

print(highest)
        

