from pathlib import Path

p = Path(__file__).with_name('advent-13-data.txt')

with p.open("r") as f:
    input_array = f.read().splitlines()

patterns = []
rawPattern = []

def columnVaryBySingleChar(matrix, col1, col2):
    diffCount = 0
    for row in matrix:
        if row[col1] != row[col2]:
            diffCount += 1
        if diffCount > 1:
            return False
    return diffCount == 1

def areColumnsEqual(matrix, col1, col2):
    for row in matrix:
        if row[col1] != row[col2]:
            return False
    return True

def rowVaryBySingleChar(str1, str2):
    diffCount = 0
    for char1, char2 in zip(str1, str2):
        if char1 != char2:
            diffCount += 1
        if diffCount > 1:
            return False
    return diffCount == 1

def getRowSymmetry(pattern: list):
    for i in range(1, len(pattern)):
        j = 0
        noMatches = 0
        while True:
            if(rowVaryBySingleChar(pattern[i - j - 1], pattern[i + j])):
                noMatches += 1
            elif(pattern[i - j - 1] != pattern[i + j]):
                break
            j += 1
            if((i - j - 1) == -1 or (i + j) == len(pattern)):
                if(noMatches == 1):
                    return i
                else: 
                    break
    return 0

def getColumnSymmetry(pattern: list):
    for i in range(1, len(pattern[0])):
        j = 0
        noMatches = 0
        while True:
            if columnVaryBySingleChar(pattern, i - j - 1, i + j):
                noMatches += 1
            elif not areColumnsEqual(pattern, i - j - 1, i + j):
                break
            j += 1
            if((i - j - 1) == -1 or (i + j) == len(pattern[0])):
                if(noMatches == 1):
                    return i
                else:
                    break
    return 0
        

for i, input in enumerate(input_array):
    if(input == ''):
        patterns.append(rawPattern)
        rawPattern = []
    else:
        if(i == len(input_array) - 1):
            patterns.append(rawPattern)
        rawPattern.append(input)

output = 0

for pattern in patterns:

    rowSymmetry = getRowSymmetry(pattern)

    columnSymmetry = getColumnSymmetry(pattern)

    output += rowSymmetry * 100 + columnSymmetry

print(output)