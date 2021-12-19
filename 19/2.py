import re
from itertools import permutations, product

with open('./data.txt') as f:
    lines = f.readlines()

scanners = {}
scanner = None

scannerx = re.compile('--- scanner (\d+) ---')

for line in lines:
    scannerMatch = scannerx.match(line)
    if scannerMatch:
        scanner = scannerMatch.groups()[0]
        scanners[scanner] = []
        continue
    
    if line == '\n':
        continue

    scanners[scanner].append(tuple([int(x) for x in line.strip().split(',')]))

diffs = {}

def index(p1,p2):
    return (p1[p2[0]],p1[p2[1]],p1[p2[2]])

def mul(p1,p2):
    return (p1[0]*p2[0],p1[1]*p2[1],p1[2]*p2[2])

def add(p1,p2):
    return (p1[0]+p2[0],p1[1]+p2[1],p1[2]+p2[2])

def diff(p1,p2):
    return (p1[0]-p2[0],p1[1]-p2[1],p1[2]-p2[2])

def permute(p1):
    return [mul(index(p1, p[0]),p[1]) for p in pperms()]

def findDiffs(points):
    d = {}
    for i, x in enumerate(points):
        for y in points[i+1:]:
            d[diff(x,y)]= [y,x]
    return d

for k, v in scanners.items():
    diffs[k] = findDiffs(v)


baseSet = set(scanners['0'])
baseDiffs = findDiffs(list(baseSet))

# point map maps from point seen by scanner to base point (relative to scanner 0)
def findPointMap( second):
    matches = []
    for i, v in diffs[second].items():
        for j in permute(i):
            if j in baseDiffs.keys():
                matches.append([v, baseDiffs[j]])
        
    pointMap = {}
    for i,v in enumerate(matches):
        point = v[0][0]
        if point in pointMap:
            continue
        possible = v[1]
        for m in matches[i:]:
            if point in m[0]:
                pointMap[point] = [x for x in possible if x in m[1]][0]

    return pointMap

def findSecondScanner(pointMap):
    e = list(pointMap.items())

    candidates = [add(e[0][1], k) for k in permute(e[0][0])]

    for scannerPoint,basePoint in e[1:]:
        c2 = [add(basePoint, j) for j in permute(scannerPoint)]
        candidates = [x for x in candidates if x in c2]
    
    return candidates[0]

def pperms():
    i = [0,1,2]

    d = [
        [1,1,1],
        [-1,1,1],
        [1,-1,1],
        [-1,-1,1],
        [1,1,-1],
        [-1,1,-1],
        [1,-1,-1],
        [-1,-1,-1],
    ]

    return product(permutations(i),d)

def findDirection(pointMap, center):
    perms = pperms()

    canidates = [p for p in perms if all([basePoint == add(center, mul(index(scannerPoint, p[0]),p[1])) for scannerPoint,basePoint in pointMap.items()])]

    return canidates[0]
            

keys = list(scanners.keys())

centers = []

while len(keys) > 0:
    k = keys[0]
    keys = keys[1:]
    try:
        pointMap = findPointMap(k)
        center = findSecondScanner(pointMap)
        mapping = findDirection(pointMap, center)

        mapped = [add(center, mul(index(x, mapping[0]),mapping[1])) for x in scanners[k]]

        for i in mapped:
            baseSet.add(i)

        baseDiffs = findDiffs(list(baseSet))
        centers.append(center)
    except:
        keys.append(k)

def distance(p1,p2):
    return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1]) + abs(p1[2]-p2[2])

maxD = 0

for i, c1 in enumerate(centers):
    for c2 in centers[i+1:]:
        maxD = max(maxD, distance(c1, c2))

print(maxD)

