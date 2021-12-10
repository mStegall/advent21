with open("./data.txt") as f:
    lines = f.readlines()

grid = [[int(i) for i in line.strip()] for line in lines]

lows = []

for y, line in enumerate(grid):
    for x, num in enumerate(line):
        if (x == 0 or num < line[x-1]) and (x==len(line)-1 or num < line[x+1]) and (y==0 or num < grid[y-1][x]) and (y == len(grid)-1 or num < grid[y+1][x]):
            
            lows += [num]

print(sum([x + 1 for x in lows]))