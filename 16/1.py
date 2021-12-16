with open('./test.txt') as f:
    lines = f.readlines()

def versionSum(packet):
    version = int(packet[0:3],base=2)
    packetType = int(packet[3:6], base=2)
    print(version,packetType)
    
    vSum = version

    if packetType == 4:
        body = packet[6:]
        while body[0] == "1":
            body = body[5:]

        body = body[5:]
        return version, body
    
    lengthType = packet[6]
    if lengthType == "1":
        packetCount = int(packet[7:18], base=2)
        print("packets", packetCount)
        body = packet[18:]
        for i in range(packetCount):
            ver, body = versionSum(body)
            vSum += ver
        
    else:

        packetBitCount = int(packet[7:22], base=2)
        print("bits", packetBitCount)
        body = packet[22: 22+packetBitCount]
        while len(body) > 0:
            ver, body = versionSum(body)
            vSum += ver
        
        body = packet[22+packetBitCount:]
        
    return vSum, body


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
    
    print(versionSum(packetBin)[0])

