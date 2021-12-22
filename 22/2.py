import re

with open('./data.txt') as f:
    lines = f.readlines()

linex = re.compile('(off|on) x=(-?\d+)..(-?\d+),y=(-?\d+)..(-?\d+),z=(-?\d+)..(-?\d+)')

cubes = set()

# return segments that are live, segments that are dead
def lineSegments(r1,r2):
    if r2[0] < r1[0]:
        if r2[1] < r1[0]:
            return [r1],[]
        if r2[1] == r1[0] and r1[0] < r1[1]:
                return [(r1[0]+1, r1[1])],[(r1[0],r1[0])]

    if r2[0] == r1[0] and r2[1] < r1[1]:
            return [(r2[1]+1,r1[1])],[(r1[0],r2[1])]

    if r2[0]==r1[1]:
        if r1[0] == r1[1]:
            return [], [r1]
        else:
            return [(r1[0],r1[1]-1)],[(r1[1],r1[1])]

    if r2[0]<=r1[0] and r1[1]<=r2[1]:
        return [], [r1]
    if r2[0]<=r1[0] and r1[0]<r2[1]<r1[1]:
        return [(r2[1]+1,r1[1])], [(r1[0],r2[1])]
    
    # Middle Case
    if r1[0]<r2[0] and r2[1]<r1[1]:
        return [(r1[0],r2[0]-1),(r2[1]+1,r1[1])], [r2]
    
    # extends to the right
    if r1[0]<r2[0]<r1[1] and r1[1] <= r2[1]:
        return [(r1[0],r2[0]-1)], [(r2[0],r1[1])] 

    return [r1],[]

def squareSegments(s1,s2):
    (x1,y1) = s1
    (x2,y2) = s2

    livex,deadx = lineSegments(x1, x2)
    
    if len(deadx) == 0:
        return [s1],[]

    livey,deady = lineSegments(y1, y2)

    if len(deady) == 0:
        return [s1],[]

    liveSquares = []
    deadSquares = []

    for r in livex:
        liveSquares.append((r,y1))

    for r in deadx:
        for r2 in livey:
            liveSquares.append((r,r2))
        for r2 in deady:
            deadSquares.append((r,r2))    

    return liveSquares, deadSquares

def cubeSegments(c1,c2):
    (x1,y1,z1) = c1
    (x2,y2,z2) = c2
    
    livez, deadz = lineSegments(z1, z2)

    if len(deadz) > 0:
        liveSquares, deadSquares = squareSegments((x1,y1), (x2,y2))
    else:
        return [c1],[]

    liveCubes = []
    deadCubes = []

    for r in livez:
        liveCubes.append((x1,y1,r))

    for r in deadz:
        for (x,y) in liveSquares:
            liveCubes.append((x,y,r))
        for (x,y) in deadSquares:
            deadCubes.append((x,y,r))

    return liveCubes, deadCubes

def subCube(c1,c2):
    return cubeSegments(c1, c2)[0]

def totalCubeVolume (cs):
    v = 0

    for c in cs:
        v += (c[0][1]-c[0][0]+1)*(c[1][1]-c[1][0]+1)*(c[2][1]-c[2][0]+1)

    return v

cubes = set()

for line in lines:
    match = linex.match(line)
    if match == None:
        continue
    
    state = match.groups()[0]

    [x1,x2,y1,y2,z1,z2] = [int(x) for x in match.groups()[1:]]
    cube = ((x1,x2),(y1,y2),(z1,z2))

    nextCubes = set()

    if state == "on":
        nextCubes.add(cube)
        
    for c in cubes:
        nextCubes.update(subCube(c, cube))
    
    cubes = nextCubes

print(totalCubeVolume(cubes))