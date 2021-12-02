import os

# get file name
dataPath = os.path.dirname(__file__)
dataFileName = "Data.txt"
absFileName = os.path.join(dataPath, dataFileName)

f = open(absFileName)
lines = f.readlines()

aim = 0
horizontalPos = 0
depth = 0

for line in lines: 
    match line.split():
        case["up", value]: 
            aim -= int(value)
        case["down", value]:
            aim += int(value)
        case["forward", value]:
            horizontalPos += int(value)
            depth += int(value) * aim

print("aim = " + str(aim) + "\nhorizontalPosition = " + str(horizontalPos) + "\ndepth = " + str(depth))
print(depth * horizontalPos)
