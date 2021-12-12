with open('./data.txt') as f:
    lines = f.readlines()

grid = [[int(x) for x in list(line.strip())] for line in lines]

count = sum([len(line) for line in grid])

i = 1

while True:
    flashes = []
    edge = []

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            grid[y][x] += 1
            if grid[y][x] > 9:
                flashes.append((x,y))
                edge.append((x,y))
    
    while len(edge) > 0:
        (x,y) = edge.pop()
        for (dx,dy) in [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]:
            nx, ny = x + dx, y + dy
            if nx < 0 or ny < 0 or ny >= len(grid) or nx >= len(grid[ny]) :
                continue

            grid[ny][nx] += 1
            if grid[ny][nx] > 9 and (nx,ny) not in flashes:
                flashes.append((nx,ny))
                edge.append((nx,ny))

    for (x,y) in flashes:
        grid[y][x] = 0

    if len(flashes) == count:
        break

    i += 1

print(i)