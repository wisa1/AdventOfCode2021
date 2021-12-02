import os

# get file name
dataPath = os.path.dirname(__file__)
dataFileName = "Data.txt"
absFileName = os.path.join(dataPath, dataFileName)

f = open(absFileName)
lines = f.readlines()

higherCount = 0
for i in range(0, len(lines)-3):
    # no need to compare more than the difference between both sliding windows
    if  int(lines[i+3])> int(lines[i]):
        higherCount += 1

print(higherCount)