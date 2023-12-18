from pathlib import Path
import sys

sys.setrecursionlimit(2500)

p = Path(__file__).with_name('advent-16-data.txt')

with p.open("r") as f:
    input_array = f.read().splitlines()

mirrors = {
    '.': {'R': ['R'], 'L': ['L'], 'U': ['U'], 'D': ['D']},
    '-': {'R': ['R'], 'L': ['L'], 'U': ['R', 'L'], 'D': ['R', 'L']},
    '|': {'R': ['U', 'D'], 'L': ['U', 'D'], 'U': ['U'], 'D': ['D']},
    '/': {'R': ['U'], 'L': ['D'], 'U': ['R'], 'D': ['L']},
    '\\': {'R': ['D'], 'L': ['U'], 'U': ['L'], 'D': ['R']}
}

directions = {
    'R': [0, 1],
    'L': [0, -1],
    'U': [-1, 0],
    'D': [1, 0]
}


def count(start):
    visitedList = set()

    def illuminate(x: int, y: int, direction: str):
        if (x, y, direction) in visitedList:
            return
        visitedList.add((x, y, direction))

        mirror = input_array[x][y]
        for nextDirection in mirrors[mirror][direction]:
            nextPoint = directions[nextDirection]
            nextX = x + nextPoint[0]
            nextY = y + nextPoint[1]
            if nextX in range(len(input_array)) and nextY in range(len(input_array[0])):
                illuminate(nextX, nextY, nextDirection)
        
    illuminate(start[0], start[1], start[2])
    return len(set([(x, y) for x, y, _ in visitedList]))
    
print(count((0, 0, 'R')))