from pathlib import Path
import re

p = Path(__file__).with_name('advent-3-data.txt')

with p.open("r") as f:
        input_array = f.read().splitlines() 

symbolMap = {}

for line, lines in enumerate(input_array):
    symbolMap[line] = []
    for row, part in enumerate(lines):
        if(part == '*'):
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

finalResult = 0

for keys in symbolMap:
    row = keys
    rows = symbolMap[row]
    number = 1
    count = 0
    for gear in rows:
        # same line
        currentLineNumbers = numberDict[row]
        for keys in currentLineNumbers:
            currentNumber = keys
            locations = currentLineNumbers[keys]
            for location in locations:
                startLocation = location
                endLocation = location + len(currentNumber) - 1
                print('locations for number ' + str(currentNumber) + ' with locations ' + str(startLocation) + ' ' + str(endLocation) + ' ' + str(gear))
                if(gear == startLocation - 1 or gear == endLocation + 1):
                    print("adding " + currentNumber)
                    number *= int(currentNumber)
                    count += 1
        # above line
        if(row - 1 >= 0):
            aboveLineNumbers = numberDict[row - 1]
            for keys in aboveLineNumbers:
                currentNumber = keys
                locations = aboveLineNumbers[keys]
                for location in locations:
                    startLocation = location
                    endLocation = location + len(currentNumber)
                    numLocation = range(startLocation, endLocation)
                    if(gear in numLocation or gear - 1 in numLocation or gear + 1 in numLocation):
                        print("adding " + currentNumber)
                        number *= int(currentNumber)
                        count += 1
        # below line
        if(row + 1 < len(numberDict)):
            belowLineNumbers = numberDict[row + 1]
            for keys in belowLineNumbers:
                currentNumber = keys
                locations = belowLineNumbers[keys]
                for location in locations:
                    startLocation = location
                    endLocation = location + len(currentNumber)
                    numLocation = range(startLocation, endLocation)
                    if(gear in numLocation or gear - 1 in numLocation or gear + 1 in numLocation):
                        print("adding " + currentNumber)
                        number *= int(currentNumber)
                        count += 1
        if(count == 2):
            print('adding final number ' +  str(number))
            finalResult += number
        number = 1
        count = 0

print(finalResult)