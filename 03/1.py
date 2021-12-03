with open("./data.txt") as f:
    lines = f.readlines()

length = len(lines[0]) - 1
counts = [0] * length

for line in lines:
    for i in range(0,length):
        if line[i] == "1":
            counts[i] += 1

gammab = ""
epsilonb = ""

for i in range(0, length):
    if counts[i] > 500:
        gammab += "1"
        epsilonb += "0"
    else:
        gammab += "0"
        epsilonb += "1"

print(int(gammab, 2) * int(epsilonb,2))
