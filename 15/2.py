with open('./data.txt') as f:
    lines = f.readlines()

grid = [[int(x) for x in line.strip()] for line in lines]

def addWrap(a,b):
    s = a+b
    if s>9:
        return (s % 10) +1
    return s

grid = [line + [addWrap(x , 1) for x in line] + [addWrap(x , 2) for x in line] + [addWrap(x , 3) for x in line] + [addWrap(x , 4) for x in line] for line in grid]

unit = grid.copy()

for i in range(1,5):
    grid.extend([[addWrap(x,i) for x in line] for line in unit])

grid[0][0]=0

best = [[None for x in line] for line in grid]

# (x,y):risk
candiates = {
    (0,0):0
 }

while len(candiates) > 0 and best[-1][-1] is None:
    [coord, risk] = min(candiates.items(), key= lambda x: x[1])
    candiates.pop(coord)
    (x,y) = coord
    best[y][x] = risk
    neighbors = []
    if x > 0 and best[y][x-1] is None:
        neighbors.append((x-1,y))
    if y > 0 and best[y-1][x] is None:
        neighbors.append((x,y-1))
    if y < len(grid)-1 and best[y+1][x] is None:
        neighbors.append((x,y+1))
    if x < len(grid)-1 and best[y][x+1] is None:
        neighbors.append((x+1,y))
    for (nx,ny) in neighbors:
        nr = risk+grid[ny][nx]
        if (nx,ny) not in candiates:
            candiates[(nx,ny)] = nr
        else: 
            candiates[(nx,ny)] = min(nr, candiates[(nx,ny)])

print(best[-1][-1])

