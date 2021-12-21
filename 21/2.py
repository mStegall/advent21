from collections import defaultdict

with open('./data.txt') as f:
    lines = f.readlines()

p1Pos = int(lines[0].split(':')[1].strip())
p2Pos = int(lines[1].split(':')[1].strip())

gameStates = {(p1Pos,0,p2Pos,0):1}

p1Active = True

def playRound(state, player1):
    nextState = defaultdict(int)

    won = 0

    if player1:
        for [(p1pos, p1score,p2pos,p2score), count] in state.items():
            for (step, stepCount) in [(3,1),(4,3),(5,6),(6,7),(7,6),(8,3),(9,1)]:
                nextPos = p1pos + step
                if nextPos > 10:
                    nextPos -= 10
                if p1score+nextPos >= 21:
                    won += count * stepCount
                else:
                    nextState[(nextPos, p1score+nextPos, p2pos,p2score)] += count * stepCount
    else:
        for [(p1pos, p1score,p2pos,p2score), count] in state.items():
            for (step, stepCount) in [(3,1),(4,3),(5,6),(6,7),(7,6),(8,3),(9,1)]:
                nextPos = p2pos + step
                if nextPos > 10:
                    nextPos -= 10
                if p2score+nextPos >= 21:
                    won += count * stepCount
                else:
                    nextState[(p1pos, p1score, nextPos, p2score+nextPos)] += count * stepCount
    
    return nextState, won

p1Wins, p2Wins = 0,0

while len(gameStates) > 0:
    gameStates, wins = playRound(gameStates, p1Active)
    if p1Active:
        p1Wins += wins
    else:
        p2Wins += wins
    
    p1Active = not p1Active

print(max(p1Wins, p2Wins))