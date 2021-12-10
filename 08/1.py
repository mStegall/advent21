with open('./data.txt') as f:
    lines = f.readlines()

count = 0

for line in lines:
    for word in line.split('|')[1].split(' '):
        if len(word.strip()) in [2,3,4,7]:
            count += 1

print(count)