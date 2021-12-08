with open('./data.txt') as f:
    lines = f.readlines()

nums = [int(x) for x in lines[0].split(',')]

def score(i):
    score = 0

    for num in nums:
        score += abs(i - num)
    
    return score

best = 9999999999999999999999

for i in range(max(nums)):
    candidate = score(i)
    if candidate < best:
        best = candidate
    
print(best)
