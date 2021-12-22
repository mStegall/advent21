import re

with open('./data.txt') as f:
    lines = f.readlines()

linex = re.compile('(off|on) x=(-?\d+)..(-?\d+),y=(-?\d+)..(-?\d+),z=(-?\d+)..(-?\d+)')

initPoints = set()

for line in lines:
    match = linex.match(line)
    if match == None:
        continue
    
    state = match.groups()[0]

    [x1,x2,y1,y2,z1,z2] = [int(x) for x in match.groups()[1:]]

    if x1< -50 or x2 >50 or y1<-50 or y2>50 or z1<-50 or z2>50:
        continue

    if state == "on":
        op = initPoints.add
    else: 
        op = initPoints.discard

    for x in range(x1,x2+1):
        for y in range(y1,y2+1):
            for z in range(z1, z2+1):
                op((x,y,z))

print(len(initPoints))