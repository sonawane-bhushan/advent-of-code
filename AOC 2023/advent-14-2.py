from pathlib import Path

p = Path(__file__).with_name('advent-14-data.txt')

with p.open("r") as f:
    input_array = f.read().splitlines()

def rotateClockwise(arr):
    rows = len(arr)
    cols = len(arr[0])

    rotated_arr = [[0] * rows for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            rotated_arr[j][rows - 1 - i] = arr[i][j]

    return rotated_arr

def tiltTable(table):
    for i in range(len(table)):
        for j in reversed(range(len(table[0]))):
            if table[i][j] == 'O':
                if(j != len(table[0]) - 1):
                    k = j
                    while(k != len(table[0]) - 1):
                        if(table[i][k+1] != 'O' and table[i][k+1] != '#'):
                            table[i][k], table[i][k+1] = table[i][k+1], table[i][k]
                            k += 1
                        else:
                            break
    return table

def cycle(table):
    for i in range(4):
        table = rotateClockwise(table)
        table = tiltTable(table)
    return table

cycles = 1000000000
seen = []
i = 0
grid = input_array

while True:
    grid = cycle(grid)
    if grid in seen:
        n = seen.index(grid)
        break
    seen.append(grid)
    i += 1

cycleLength = i - n
seenIndex = n + (cycles - n) % cycleLength - 1

total = 0

grid = rotateClockwise(seen[seenIndex])

for row in grid:
    for i, element in enumerate(row):
        if(element == 'O'):
            total += i + 1

print(total)