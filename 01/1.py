with open("./data.txt") as f:
    lines = f.readlines()

last = int(lines[0])
count = 0
    
for i in lines:
    new = int(i)
    
    if new > last:
        count += 1
    
    last = new

print(count)