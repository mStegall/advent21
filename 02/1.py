with open("data.txt") as f:
    lines = f.readlines()
    
x, y = 0,0

for line in lines:
    words = line.split(" ")
    if len(words) != 2:
        raise Exception
    
    if words[0] == "forward":
        x += int(words[1])
    elif words[0] == "up":
        y -= int(words[1])
    elif words[0] == "down":
        y += int(words[1])

print(x, y, x*y)