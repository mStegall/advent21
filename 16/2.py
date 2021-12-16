from functools import reduce

with open('./data.txt') as f:
    lines = f.readlines()

def evalPacket(packet):
    version = int(packet[0:3],base=2)
    packetType = int(packet[3:6], base=2)
    
    vSum = version

    if packetType == 4:
        body = packet[6:]
        value = ""
        while body[0] == "1":
            value += body[1:5]
            body = body[5:]
        value += body[1:5]
        body = body[5:]
        return int(value, base=2), body
    
    lengthType = packet[6]
    subs = []

    if lengthType == "1":
        packetCount = int(packet[7:18], base=2)
        body = packet[18:]
        for i in range(packetCount):
            ver, body = evalPacket(body)
            subs.append(ver)
        
        
        
    else:

        packetBitCount = int(packet[7:22], base=2)
        body = packet[22: 22+packetBitCount]
        while len(body) > 0:
            ver, body = evalPacket(body)
            subs.append(ver)
        
        body = packet[22+packetBitCount:]

    if packetType == 0:
        return sum(subs), body
    elif packetType == 1:
        return reduce(lambda x,y: x*y, subs,1), body
    elif packetType == 2:
        return min(subs), body
    elif packetType == 3:
        return max(subs), body
    elif packetType == 5:
        return 1 if subs[0] > subs[1] else 0, body
    elif packetType == 6:
        return 1 if subs[0] < subs[1] else 0, body
    elif packetType == 7:
        return 1 if subs[0] == subs[1] else 0, body

chars = {
'0' : '0000',
'1' : '0001',
'2' : '0010',
'3' : '0011',
'4' : '0100',
'5' : '0101',
'6' : '0110',
'7' : '0111',
'8' : '1000',
'9' : '1001',
'A' : '1010',
'B' : '1011',
'C' : '1100',
'D' : '1101',
'E' : '1110',
'F' : '1111',
}


for line in lines:

    packetBin = ''.join([chars[x] for x in line.strip()])
    
    print(evalPacket(packetBin)[0])
