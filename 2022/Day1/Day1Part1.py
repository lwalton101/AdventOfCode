file = open("Day1.txt", "r")
lines = file.readlines()
prevCal = []
elfDict = {}

index = -1
for x in lines:
    if(x == "\n"):
        index += 1
        total = 0
        for y in prevCal:
            total += int(y)

        prevCal.clear()
        elfDict[index] = total
    else:
        prevCal.append(x)

highest = 0
highestIndex = 0
for x in elfDict:
    if elfDict[x] > highest:
        highest = elfDict[x]
        highestIndex = x
    
print(highest)