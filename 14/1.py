from collections import defaultdict

with open('./data.txt') as f:
    lines = f.readlines()

chain = lines[0].strip()

pairs = {}

for line in lines[2:]:
    [pair, value] = line.strip().split(" -> ")
    pairs[pair] = value

for _ in range(10):
    inserts = [pairs[chain[i:i+2]] for i in range(len(chain) - 1)]
    chain = ''.join([x for t in zip(chain, inserts) for x in t]+[chain[-1]])

counts = defaultdict(int)

for char in chain:
    counts[char] += 1

print(max(counts.values())-min(counts.values()))