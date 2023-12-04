from pathlib import Path
import re

p = Path(__file__).with_name('advent-3-data.txt')

with p.open("r") as f:
        input_array = f.read().splitlines() 

symbolMap = {}

for line, lines in enumerate(input_array):
    symbolMap[line] = []
    for row, part in enumerate(lines):
        if(part != '.' and (part < '0' or part > '9')):
            symbolMap[line].append(row)

print(symbolMap)

numberDict = {}

for line, lines in enumerate(input_array):
    number = ''
    numberDict[line] = {}
    lineLength = len(lines)
    for j, data in enumerate(lines):
        if(data >= '0' and data <= '9'):
            number += data
            if(j == lineLength - 1):
                if(number in numberDict[line]):
                    numberDict[line][number].append(j - len(number) + 1)
                else:
                    numberDict[line][number] = [j - len(number) + 1]
        else:
            if(number != ''): 
                if(number in numberDict[line]):
                    numberDict[line][number].append(j - len(number))
                else:
                    numberDict[line][number] = [j - len(number)]
            number = ''

print(numberDict)

finalArray = 0

for keys in numberDict:
    lineNumber = keys
    for keys in numberDict[lineNumber]:
        number = keys
        location = numberDict[lineNumber][number]
        for index in location:
            for i in range(index, index + len(str(number))):
                if(lineNumber > 0):
                    if(i - 1 in symbolMap[lineNumber - 1] or i + 1 in symbolMap[lineNumber - 1] or i in symbolMap[lineNumber - 1]):
                        print('adding ' + str(number))
                        finalArray += int(number)
                        break
                if(lineNumber < len(numberDict) - 1):
                    if(i - 1 in symbolMap[lineNumber + 1] or i + 1 in symbolMap[lineNumber + 1] or i in symbolMap[lineNumber + 1]):
                        print('adding ' + str(number))
                        finalArray += int(number)
                        break
                if(i - 1 in symbolMap[lineNumber] or i + 1 in symbolMap[lineNumber]):
                    print('adding ' + str(number))
                    finalArray += int(number)
                    break
print(finalArray)