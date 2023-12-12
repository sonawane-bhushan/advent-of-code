from pathlib import Path

p = Path(__file__).with_name('advent-11-data.txt')

with p.open("r") as f:
    input_array = f.read().splitlines()

universe = []

def isElementPresentInRow(universe, row_index, element):
    return element in universe[row_index]

def isElementPresentInColumn(universe, col_index, element):
    return element in [row[col_index] for row in universe]

def getCountOfEmptyRows(emptyRows, i, j):
    if (i > j):
        i, j = j, i
    return sum(emptyRows[i : j])

def getCountOfEmptyColumns(emptyColumns, i, j):
    if (i > j):
        i, j = j, i
    return sum(emptyColumns[i : j])

for input in input_array:
    universe.append(list(input))

galaxies = []

for i, rowValue in enumerate(universe):
    for j, colValue in enumerate(rowValue):
        if(colValue == '#'):
            galaxies.append((i, j))


emptyRows = []
emptyColumns = []

for i in range(len(universe)):
    if(isElementPresentInRow(universe, i, '#') == False):
        emptyRows.append(1)
    else:
        emptyRows.append(0)

for i in range(len(universe[0])):
    if(isElementPresentInColumn(universe, i, '#') == False):
        emptyColumns.append(1)
    else:
        emptyColumns.append(0)

totalDistance = 0

for i in range(len(galaxies)):
    j = i + 1
    while(j < len(galaxies)):
        countOfEmptyRows = getCountOfEmptyRows(emptyRows, galaxies[j][0], galaxies[i][0])
        countOfEmptyColumns = getCountOfEmptyColumns(emptyColumns, galaxies[j][1], galaxies[i][1])
        totalDistance += ((abs(galaxies[j][0] - galaxies[i][0])) + countOfEmptyRows * 999999) + (abs(galaxies[j][1] - galaxies[i][1]) + countOfEmptyColumns * 999999)
        j += 1
    
print(totalDistance)