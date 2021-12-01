f = open("D:\private\git\AdventOfCode2021\Day 1\Data_2.txt")
lines = f.readlines()

higherCount = 0

for i in range(0, len(lines)-3):
    # no need to compare more than the difference between both sliding windows
    if  int(lines[i+3])> int(lines[i]):
        higherCount += 1

print(higherCount)