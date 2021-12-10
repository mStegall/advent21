with open('./data.txt') as f:
    lines = f.readlines()

points = {    
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}

match = {
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<',
}

score = 0

def lineScore (line):
    stack = []

    for char in line:
        if char in ['(','[','{','<']:
            stack.append(char)
        else:
            open = stack.pop()
            if open != match[char]:
                return points[char]

    return 0


for line in lines:
    score += lineScore(line.strip())


print(score)