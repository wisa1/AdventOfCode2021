import os

# get file name
dataPath = os.path.dirname(__file__)
dataFileName = "Data.txt"
absFileName = os.path.join(dataPath, dataFileName)

f = open(absFileName)
lines = f.readlines()

xPos = 0
yPos = 0

for line in lines: 
    match line.split():
        case["up", value]: 
            yPos -= int(value)
        case["down", value]:
            yPos += int(value)
        case["forward", value]:
            xPos += int(value)

print(xPos * yPos)