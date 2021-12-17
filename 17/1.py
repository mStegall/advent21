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
        # print(y)
        if yb<= y <= yt and xr >= x >= xl:
            return True

        vy -= 1
        if vx > 0:
            vx -= 1
        elif vx < 0:
            vx += 1

    return False

# find x min
x = 0

while x*(x+1) / 2 < xl:
    x += 1

highHit = 0

for i in range(1000):
    if isHit(x, i):
        highHit = i
    
print(highHit)
print(highHit*(highHit + 1)/2)