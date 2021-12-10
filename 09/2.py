with open("./data.txt") as f:
    lines = f.readlines()

grid = [[int(i) for i in line.strip()] for line in lines]

lows = []

gridLength = len(grid) -1
rowSize = len(grid[0]) -1

for y, line in enumerate(grid):
    for x, num in enumerate(line):
        if (x == 0 or num < line[x-1]) and (x==len(line)-1 or num < line[x+1]) and (y==0 or num < grid[y-1][x]) and (y == len(grid)-1 or num < grid[y+1][x]):
            
            lows += [(x,y)]

basinSizes = []

for (x0,y0) in lows:
    activepoints = [(x0,y0)]
    points = [(x0,y0)]

    while len(activepoints) > 0:
        (x,y) = activepoints.pop()
        if x != 0 and grid[y][x-1] != 9 and (x-1,y) not in points:
            activepoints.append((x-1,y))
            points.append((x-1,y))

        if x != rowSize and grid[y][x+1] != 9 and (x+1,y) not in points:
            activepoints.append((x+1,y))
            points.append((x+1,y))

        if y != 0 and grid[y-1][x] != 9 and (x,y-1) not in points:
            activepoints.append((x,y-1))
            points.append((x,y-1))

        if y != gridLength and grid[y+1][x] != 9 and (x,y+1) not in points:
            activepoints.append((x,y+1))
            points.append((x,y+1))

    basinSizes += [len(points)]

basinSizes.sort()

print(basinSizes[-1] * basinSizes[-2] * basinSizes[-3])



    