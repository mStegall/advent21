with open('./data.txt') as f:
    lines = f.readlines()

lanternfish = {x:0 for x in range(9)}

for i in lines[0].split(","):
    lanternfish[int(i)] += 1

for i in range(80):
    newLanternfish = {x:0 for x in range(9)}

    newLanternfish[8], newLanternfish[6] = lanternfish[0], lanternfish[0]

    for i in range(8):
        newLanternfish[i] += lanternfish[i+1]
        
    lanternfish = newLanternfish

count = 0

for key in lanternfish:
    count += lanternfish[key]

print(count)