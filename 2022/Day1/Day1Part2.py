file = open("Day1.txt", "r")
lines = file.readlines()
prevCal = []
elfDict = []

index = -1
for x in lines:
    if(x == "\n"):
        index += 1
        total = 0
        for y in prevCal:
            total += int(y)

        prevCal.clear()
        elfDict.append(total)
    else:
        prevCal.append(x)


elfDict.sort()
elfDict.reverse()
    
print(elfDict[0] + elfDict[1] + elfDict[2])