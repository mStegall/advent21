with open('./data.txt') as f:
    lines = f.readlines()

p1Pos = int(lines[0].split(':')[1].strip())
p2Pos = int(lines[1].split(':')[1].strip())
p1Score, p2Score = 0,0

p1Turn = True

class ddice:
    def __init__(self):
        self.count = 0
        self.n = 0
    def __iter__(self):
        self
    def __next__(self):
        self.count += 1
        self.n += 1
        if self.n == 101:
            self.n = 1
        
        return self.n

dieRolls = ddice()

while p1Score < 1000 and p2Score < 1000:
    rolls = [next(dieRolls) , next(dieRolls) , next(dieRolls)]
    total = sum(rolls)

    if p1Turn:
        p1Pos += total
        p1Pos =  ((p1Pos -1 )% 10) +1
        p1Score += p1Pos
    else:
        p2Pos += total
        p2Pos = ((p2Pos - 1) % 10) +1
        p2Score += p2Pos
    
    p1Turn = not p1Turn

if p1Score > p2Score:
    loser = p2Score
else:
    loser = p1Score

print(loser * dieRolls.count)