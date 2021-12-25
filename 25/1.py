with open('./data.txt') as f:
    lines = f.readlines()

height = len(lines)
width = len(lines[0].strip())

easts = set()
souths = set()

for y,line in enumerate(lines):
    for x, char in enumerate(line.strip()):
        if char == '>':
            easts.add((x,y))
        elif char == 'v':
            souths.add((x,y))

changed = True
step = 0

while changed:
    changed = False
    newEasts = set()
    newSouths = set()

    for (x,y) in easts:
        newX = (x + 1) % width
        if (newX,y) not in souths and (newX,y) not in easts:
            newEasts.add((newX,y))
        else:
            newEasts.add((x,y))
    
    if newEasts != easts:
        changed = True
        easts = newEasts

    for (x,y) in souths:
        newY = (y + 1) % height
        if (x,newY) not in souths and (x,newY) not in easts:
            newSouths.add((x,newY))
        else:
            newSouths.add((x,y))

    if newSouths != souths:
        changed = True
        souths = newSouths

    step += 1

print(step)