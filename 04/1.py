with open('./data.txt') as f:
    lines = f.readlines()

class Board:
    nums = []
    marks = []
    numMap = {}

    def __init__(self, boardstrings):
        self.nums = []
        self.marks = []
        self.numMap = {}
        
        for y, line in enumerate(boardstrings):
            parsedLine =[ int(x[0] + x[1]) for x in list(zip(*[iter(line)]*3))]
            self.nums.append(parsedLine)
            for x, numString in enumerate(parsedLine):
                self.numMap[int(numString)] = (x,y)
        
        length = len(boardstrings)
        self.marks = [x.copy() for x in [[False] * length] * length]

    def mark(self,i):
        pair = self.numMap.get(i)

        if not pair:
            return False

        (x,y) = pair

        self.marks[y][x] = True

        if all(self.marks[y]):
            return True
        elif all([y[x] for y in self.marks]):
            return True
        
        return False
    
    def score(self, i):
        score = 0 

        for y, line in enumerate(self.nums):
            for x, num in enumerate(line):
                if not self.marks[y][x]:
                    score += num

        return score * i

nums = lines[0]

boards = []

for i in range(2,len(lines), 6):
    boards.append(Board(lines[i: i+5]))

done = False

for i in [int(x) for x in nums.split(',')]:
    for b in boards:
        if done:
            break

        if b.mark(i):
            print(b.score(i))
            done=True
            break
