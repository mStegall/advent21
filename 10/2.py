with open('./data.txt') as f:
    lines = f.readlines()

points = {    
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}

matchClose = {
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<',
}

matchOpen = {
    '(':')',
    '[':']',
    '{':'}',
    '<':'>',
}

scores = []

def lineScore (line):
    stack = []

    for char in line:
        if char in ['(','[','{','<']:
            stack.append(char)
        else:
            open = stack.pop()
            if open != matchClose[char]:
                return 0

    score = 0

    for char in stack[::-1]:
        score *= 5
        score += points[matchOpen[char]]

    return score


for line in lines:
    score = lineScore(line.strip())
    if score != 0:
        scores += [score]

scores.sort()

print(scores[len(scores)//2])