import os

# get file name
dataPath = os.path.dirname(__file__)
dataFileName = "Data.txt"
absFileName = os.path.join(dataPath, dataFileName)

f = open(absFileName)
lines = f.readlines()

higherCount = 0

for i in range(1,len(lines)-1):
    if int(lines[i]) > int(lines[i-1]):
        higherCount += 1

print(higherCount)
