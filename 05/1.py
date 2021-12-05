with open('./data.txt') as f:
    lines = f.readlines()

size = 1000

field = [row.copy() for row in [[0] * size]*size]

for line in lines:
    [p1,p2] = line.split(" -> ")
    [x1s,y1s] = p1.split(",")
    [x2s,y2s] = p2.split(",")

    x1,y1,x2,y2 = int(x1s), int(y1s), int(x2s), int(y2s)

    if x1 == x2:
        for y in range(min(y1,y2), max(y1,y2)+1):
            field[y][x1] += 1
    elif y1 == y2:
        for x in range(min(x1,x2), max(x1,x2)+1):
            field[y1][x] += 1

count = 0

for line in field:
    for num in line:
        if num >= 2:
            count += 1

print(count)