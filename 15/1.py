with open('./data.txt') as f:
    lines = f.readlines()

grid = [[int(x) for x in line.strip()] for line in lines]

grid[0][0]=0

for i in range(len(grid)):
    for j in range(len(grid)):
        
        if i > 0 and j > 0:
            grid[j][i] += min(grid[j][i-1], grid[j-1][i])

        if i > 0 and j == 0:
            grid[j][i] += grid[j][i-1]

        elif i == 0 and j > 0:
            grid[j][i] += grid[j-1][i]


print(grid[-1][-1])