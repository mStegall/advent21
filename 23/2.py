import re

with open('./data.txt') as f:
    lines = f.readlines()

linex = re.compile("#([A-D])#([A-D])#([A-D])#([A-D])#")

cost = {
    'A':1,
    'B':10,
    'C':100,
    'D':1000,
}

gameState = {}

for i,line in enumerate(lines[1:3]+['#D#C#B#A#','#D#B#A#C#']+ lines[3:]):
    match = linex.search(line)

    if match == None:
        continue

    for j,char in enumerate(match.groups()):
        gameState[(j*2+3,i)] = char

def hashable(dict):
    return tuple(sorted(dict.items()))

def fromHashable(tup):
    return {k:v for (k,v) in tup}

rooms = {
    3:'A',
    5:'B',
    7:'C',
    9:'D'
}

roomsLookup = {v:k for k,v in rooms.items()}

roomsX = list(rooms.keys())

roomLength = 4

def validMoves(gameState, curr):
    moves = {}
    
    roomsOpen = {v: all([ (k,y) not in gameState or gameState[(k,y)] == v for y in range(2,roomLength+1)]+[(k,1) not in gameState]) for k,v in rooms.items()}

    for (x,y), ent in gameState.items():
        # optimize case where room tightly packed
        if y > 0 and x == roomsLookup[ent] :
            if all([(x,y) in gameState and gameState[(x,y)]==ent for y in range(y+1, roomLength+1)]):
                continue

        if y == 1:
            step = 1
            while x+step <= 11 and (x+step,0) not in gameState:
                if x+step in roomsX:
                    step +=1
                    continue
                nextState = gameState.copy()
                nextState.pop((x,y))
                nextState[(x+step,0)] = ent
                moves[hashable(nextState)] = cost[ent]*(step+1) + curr
                step +=1
            step = 1
            while x-step >= 1 and (x-step,0) not in gameState:
                if x-step in roomsX:
                    step +=1
                    continue
                
                nextState = gameState.copy()
                nextState.pop((x,y))
                nextState[(x-step,0)] = ent
                moves[hashable(nextState)] = cost[ent]*(step+1) + curr
                step +=1
            
        elif y > 1 :
            if all([(x,iy) not in gameState for iy in range(1,y)]):
                step = 1
                while x+step <= 11 and (x+step,0) not in gameState:
                    if x+step in roomsX:
                        step +=1
                        continue
                    nextState = gameState.copy()
                    nextState.pop((x,y))
                    nextState[(x+step,0)] = ent
                    moves[hashable(nextState)] = cost[ent]*(step+y) + curr
                    step +=1
                step = 1
                while x-step >= 1 and (x-step,0) not in gameState:
                    if x-step in roomsX:
                        step +=1
                        continue
                    
                    nextState = gameState.copy()
                    nextState.pop((x,y))
                    nextState[(x-step,0)] = ent
                    moves[hashable(nextState)] = cost[ent]*(step+y) + curr
                    step +=1
        elif roomsOpen[ent]:
            roomX = roomsLookup[ent]
            if x > roomX:
                spotsBetween = range(roomX, x)
            else:
                spotsBetween = range(x+1, roomX+1)
            
            if all([(x,0) not in gameState for x in spotsBetween]):
                firstSpot = roomLength
                while (roomX,firstSpot) in gameState:
                    firstSpot -= 1
                nextState = gameState.copy()
                nextState.pop((x,y))
                nextState[(roomX,firstSpot)] = ent
                moves[hashable(nextState)] = cost[ent]*(len(spotsBetween)+firstSpot) + curr

    return moves


targetDict = {}
for x,v in rooms.items():
    for y in range(1,roomLength+1):
        targetDict[(x,y)]=v
target = hashable(targetDict)

seen = {}

candidates = {hashable(gameState):0}

while target not in seen and len(candidates) > 0 :
    candidate = min(candidates.items(), key=lambda x: x[1])
    candidates.pop(candidate[0])
    seen[candidate[0]] = candidate[1]
    # print(candidate[1], len(seen), len(candidates))
    moves = validMoves(fromHashable(candidate[0]), candidate[1])
    for state, c in moves.items():
        if state in seen:
            continue
        if state not in candidates:
            candidates[state]=c
        else:
            candidates[state]=min(c,candidates[state])

print(seen[target])