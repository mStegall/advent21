from collections import defaultdict

with open('./data.txt') as f:
    lines = f.readlines()

chain = lines[0].strip()

pairs = {}
counts = {}

for line in lines[2:]:
    [pair, value] = line.strip().split(" -> ")
    pairs[pair] = pair[0] + value + pair[1]
    count= defaultdict(int)
    for char in pairs[pair]:
        count[char] += 1
    counts[pair] = count


for i in range(39):
    newCounts = {}

    for line in lines[2:]:
        [pair, _] = line.strip().split(" -> ")
        newCount = defaultdict(int)
        for [k,v] in counts[pairs[pair][0:2]].items():
            newCount[k] += v
        
        for [k,v] in counts[pairs[pair][1:3]].items():
            newCount[k] += v

        newCount[pairs[pair][1]] -=1

        newCounts[pair] = newCount
    
    counts = newCounts


finalCounts = defaultdict(int)

for i in range(len(chain)-1):
    for [k,v] in counts[chain[i:i+2]].items():
        finalCounts[k] += v

for char in chain[1:-1]:
    finalCounts[char] -= 1

print(max(finalCounts.values())-min(finalCounts.values()))