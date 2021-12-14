with open('./data.txt') as f:
    lines = f.readlines()

sectionIndex = lines.index("\n")

coordsS = [line.strip().split(',') for line in lines[:sectionIndex]]
coords = [[int(x) for x in line] for line in coordsS]

paperX = max([coord[0] for coord in coords])
paperY = max([coord[1] for coord in coords])

def printGrid():
    grid = [line.copy() for line in [[False] * (paperX+1)] * (paperY+1)]

    for [x,y] in coords:
        grid[y][x] = True
    print('\n'.join([''.join(['#' if x else '.' for x in line]) for line in grid]))


for direction in lines[sectionIndex+1:sectionIndex+2]:
    [plane,valueS] = direction.strip().split(' ')[2].split('=')
    value = int(valueS)
    if plane == 'x':
        coords = [[coord[0] if coord[0] < value else 2 * value - coord[0], coord[1]] for coord in coords]
        paperX = value -1
    else:
        coords = [[coord[0], coord[1] if coord[1] < value else 2 * value - coord[1]] for coord in coords]
        paperY = value -1

uniques = []

for coord in coords:
    if coord not in uniques:
        uniques.append(coord)

print(len(uniques))

