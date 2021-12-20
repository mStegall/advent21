with open('./data.txt') as f:
    lines = f.readlines()

key = lines[0]
baseState = False
grid = set()

left, top, bottom, right = 0, 0, len(lines[2:]), len(lines[2])-1

for y, line in enumerate(lines[2:]):
    for x, char in enumerate(line):
        if char == '#':
            grid.add((x,y))

def printGrid():
    string = ""
    for y in range(top, bottom):
        for x in range(left,right):
            if (x,y) in grid:
                string +="#"
            else:
                string += "."
        string += "\n"

    print(string)

for _ in range(50):
    left -= 1
    top -= 1
    bottom += 1
    right += 1

    newGrid = set()
    for y in range(top, bottom):
        for x in range(left,right):
            num = ""

            for point in [(x-1,y-1),(x,y-1),(x+1,y-1),(x-1,y),(x,y),(x+1,y),(x-1,y+1),(x,y+1),(x+1,y+1)]:
                (m,n) = point
                if left < m < right - 1 and top < n < bottom -1 :
                    if point in grid:
                        num += "1"
                    else:
                        num += "0"
                else:
                    if baseState:
                        num += "1"
                    else:
                        num += "0"
            
            if key[int(num, base=2)] == "#":
                newGrid.add((x,y))

    if key[0] == "#":
        baseState = not baseState

    grid = newGrid

print(len(grid))

