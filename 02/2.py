with open("data.txt") as f:
    lines = f.readlines()
    
x, y, aim = 0,0,0

for line in lines:
    words = line.split(" ")
    if len(words) != 2:
        raise Exception
    
    if words[0] == "forward":
        x += int(words[1])
        y += int(words[1]) * aim
    elif words[0] == "up":
        aim -= int(words[1])
    elif words[0] == "down":
        aim += int(words[1])

print(x, y, x*y)