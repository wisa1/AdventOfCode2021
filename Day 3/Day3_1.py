import os

# get file name
dataPath = os.path.dirname(__file__)
dataFileName = "Data.txt"
absFileName = os.path.join(dataPath, dataFileName)

f = open(absFileName)
lines = f.readlines()

arrayLen = 12
occurences = [0 for i in range(arrayLen)]

for line in lines: 
    for i in range(0, len(line)): 
        char = line[i]
        match char:
            case("0"):
                occurences[i] -= 1
            case("1"):
                occurences[i] += 1

gammaRate = 0
epsilonRate = 0

for i in range(0, arrayLen):
    if(occurences[i] > 0):
        gammaRate += 2**(arrayLen -1  - i)
    else:
        epsilonRate += 2**(arrayLen -1 - i)

print(occurences)
print(gammaRate)
print(epsilonRate)
print(gammaRate * epsilonRate)

