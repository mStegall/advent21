import re

with open('./data.txt') as f:
    lines = f.readlines()

p = re.compile('target area: x=(-?\d+)..(-?\d+), y=(-?\d+)..(-?\d+)')

(xls,xrs,ybs,yts) = p.match(lines[0]).groups()

xl,xr,yb,yt = int(xls), int(xrs), int(ybs), int(yts)

print(xl,xr,yb,yt)

def isHit (vx,vy):
    x,y = 0,0

    while y > yb:
        x += vx
        y += vy
        if yb<= y <= yt and xr >= x >= xl:
            return True

        vy -= 1
        if vx > 0:
            vx -= 1
        elif vx < 0:
            vx += 1

    return False

minx = 0

while minx*(minx+1) / 2 < xl:
    minx += 1

highHit = 0

for i in range(1000):
    if isHit(minx, i):
        highHit = i

count = 0

for x in range(minx, minx + 1000):
    for y in range(-1000, highHit+1):
        if isHit(x, y):
            count += 1

print(count)