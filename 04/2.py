with open('./data.txt') as f:
    lines = f.readlines()

class Board:
    nums = []
    marks = []
    numMap = {}
    won = False
    name =""

    def __init__(self, boardstrings, num):
        self.nums = []
        self.marks = []
        self.numMap = {}
        self.name = str(num)
        
        for y, line in enumerate(boardstrings):
            parsedLine =[int(x[0] + x[1]) for x in list(zip(*[iter(line)]*3))]
            self.nums.append(parsedLine)
            for x, numString in enumerate(parsedLine):
                self.numMap[int(numString)] = (x,y)
        
        length = len(boardstrings)
        self.marks = [x.copy() for x in [[False] * length] * length]

    def mark(self,i):
        if i not in self.numMap:
            return 

        (x,y) = self.numMap[i]

        self.marks[y][x] = True

        if all(self.marks[y]) or all([y[x] for y in self.marks]):
            self.won = True
    
    def score(self, i):
        score = 0 

        for y, line in enumerate(self.nums):
            for x, num in enumerate(line):
                if not self.marks[y][x]:
                    score += num

        return score * i
    
    def print(self):
        st = "Board "+self.name+"\n"
        for y, line in enumerate(self.nums):
            for x, num in enumerate(line):
                if not self.marks[y][x]:
                    st += "{:2} ".format(num)
                else:
                    st += "XX "
            st += "\n"
        print(st)

boards = [Board(lines[i: i+5], name) for name, i 
    in enumerate(range(2,len(lines), 6))]


for i in [int(x) for x in lines[0].split(',')]:
    for b in boards:
        b.mark(i)
    
    if len(boards) == 1 and boards[0].won:
        print("score:",boards[0].score(i))

    boards = [b for b in boards if not b.won]