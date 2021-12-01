f = open("D:\private\git\AdventOfCode2021\Day 1\Data_1.txt", "r")
lines = f.readlines()

higherCount = 0

for i in range(1,len(lines)-1):
    if int(lines[i]) > int(lines[i-1]):
        higherCount += 1

print(higherCount)
