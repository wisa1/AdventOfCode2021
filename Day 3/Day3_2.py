import os

# get file name
dataPath = os.path.dirname(__file__)
dataFileName = "Data.txt"
absFileName = os.path.join(dataPath, dataFileName)

f = open(absFileName)
lines = f.readlines()

def GetDay3_2Rating(lines, type): 
    countZeroBit = 0
    countOneBit = 0
    mostCommonBit = 0
    leastCommonBit = 0
    lineLength = len(lines[0])-1

    for i in range(0,lineLength):
        # count bits
        countZeroBit = 0
        countOneBit = 0
        for line in lines:
            match line[i]:
                case("0"):
                    countZeroBit += 1
                case("1"):
                    countOneBit += 1

        # determine most common bit
        if countZeroBit > countOneBit: 
            mostCommonBit = 0 
            leastCommonBit = 1
        else: 
            if countZeroBit < countOneBit:
                mostCommonBit = 1
                leastCommonBit = 0
            else:
                mostCommonBit = 1
                leastCommonBit = 0

        # remove lines accordingly
        if type == "oxygen":
            lines = [l for l in lines if l[i] == str(mostCommonBit)]
        if type == "co2":
            lines = [l for l in lines if l[i] == str(leastCommonBit)]

        # check exit condition
        if len(lines) <= 1: 
            return lines[0]

    
oxyRating = GetDay3_2Rating(lines, "oxygen")
co2Rating = GetDay3_2Rating(lines, "co2")

print(oxyRating)
print(co2Rating)

oxyDecimal = int(oxyRating, 2)
co2Decimal = int(co2Rating, 2)

print(oxyDecimal)
print(co2Decimal)
print(oxyDecimal * co2Decimal)


