with open("./data.txt") as f:
    lines = f.readlines()

oxNums = lines
co2Nums = lines

oi = 0 
while len(oxNums) > 1:
    count = 0 
    for line in oxNums:
        if line[oi] == "1":
            count += 1
    
    if count >= len(oxNums)/2:
        char = "1"
    else:
        char = "0"
    
    oxNums = [ x for x in oxNums if x[oi] == char]

    oi += 1

ci = 0 
while len(co2Nums) > 1:
    count = 0 
    for line in co2Nums:
        if line[ci] == "1":
            count += 1
    
    if count < len(co2Nums)/2:
        char = "1"
    else:
        char = "0"
    
    co2Nums = [ x for x in co2Nums if x[ci] == char]
    ci += 1

print(oxNums,co2Nums, int(oxNums[0], 2)* int(co2Nums[0],2))
