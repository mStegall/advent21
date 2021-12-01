with open("./data.txt") as f:
    lines = f.readlines()

sums = []

for i in range(len(lines) - 3):
    j = int(lines[i]) + int(lines[i+1]) + int(lines[i+2])
    sums.append(j)

last = int(lines[0])
count = 0

for i in sums:
    new = int(i)
    
    if new > last:
        count += 1
    
    last = new

print(count)