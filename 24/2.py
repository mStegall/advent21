with open('./data.txt') as f:
    lines = f.readlines()

class ALU:
    def __init__(self, program):
        self.program = program
        self.pc = 0
        self.mem = {'w':0, 'x': 0, 'y': 0, 'z': 0}
    
    def reset(self):
        self.pc = 0
        self.mem = {'w':0, 'x': 0, 'y': 0, 'z': 0}

    def run(self, n):
        inputUsed = False
        while self.pc < len(self.program):
            inst = self.program[self.pc]
            [op, *args] = inst.split(' ')
            
            if op == "inp":
                if inputUsed:
                    return False
                inputUsed = True
                self.mem[args[0]] = n
            else:
                if args[1] in 'wxyz':
                    arg2 = self.mem[args[1]]
                else:
                    arg2 = int(args[1])
                
                if op == "add":
                    self.mem[args[0]] += arg2
                elif op == "mul":
                    self.mem[args[0]] *= arg2
                elif op == "div":
                    self.mem[args[0]] //= arg2
                elif op == "mod":
                    self.mem[args[0]] %= arg2
                elif op == "eql":
                    self.mem[args[0]] = int(self.mem[args[0]] == arg2)

            self.pc += 1

        return True

    def set(self,w,x,y,z,pc):
        self.pc = pc
        self.mem = {
            'w':w,
            'x':x,
            'y':y,
            'z':z
        }
    
    def stateTuple(self):
        return (self.mem['w'],self.mem['x'],self.mem['y'],self.mem['z']),(self.pc)

alu = ALU([x.strip() for x in lines])

states = {(0,0,0,0):((0),0)}

for i in range(14):
    nextStates = {}
    for (w,x,y,z), ((pc),prefix) in states.items():
        for i in range(1,10):
            alu.set(w,x,y,z,pc)
            alu.run(i)
            state,extra = alu.stateTuple()
            num = prefix*10 + i
            if state not in nextStates:
                nextStates[state] = (extra, num)
            else:
                if nextStates[state][1] > num:
                    nextStates[state] = (extra, num)
        
    print(len(nextStates))
    states = nextStates

best = 9999999999999999999999999999999999999999

for (_,_,_,z), (_,num) in states.items():
    if z == 0 and num < best:
        best = num

print(best)