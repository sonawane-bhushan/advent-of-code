from pathlib import Path

p = Path(__file__).with_name('advent-10-data.txt')

with p.open("r") as f:
    input_array = f.read().splitlines()

upValid = ['|', '7', 'F']
downValid = ['|', 'L', 'J']
leftValid = ['-', 'L', 'F']
rightValid = ['-', 'J', 'T']

pipeDict = {
    '|D': [1, 0, 'D'],
    '|U': [-1, 0, 'U'],
    '-R': [0, 1, 'R'],
    '-L': [0, -1, 'L'],
    '7R': [1, 0, 'D'],
    '7U': [0, -1, 'L'],
    'FU': [0, 1, 'R'],
    'FL': [1, 0, 'D'],
    'LD': [0, 1, 'R'],
    'LL': [-1, 0, 'U'],
    'JD': [0, -1, 'L'],
    'JR': [-1, 0, 'U']
}

def getStartPoint():
    for i, input in enumerate(input_array):
        startPoint = input.find('S')
        if(startPoint != -1):
            return(i, startPoint)
        
def getDirections(location: tuple):
    directions = []
    if(location[0] > 0):
        if(input_array[location[0] - 1][location[1]] in upValid):
            directions.append([location[0] - 1, location[1], 'U'])
    if(location[0] < len(input_array)):
        if(input_array[location[0] + 1][location[1]] in downValid):
            directions.append([location[0] + 1, location[1], 'D'])
    if(location[1] > 0):
        if(input_array[location[0]][location[1] - 1] in leftValid):
            directions.append([location[0], location[1] - 1, 'L'])
    if(location[1] < len(input_array[0])):
        if(input_array[location[0]][location[1] + 1] in rightValid):
            directions.append([location[0], location[1] + 1, 'R'])
    return directions

def getNextLocation(location: list):
    points = pipeDict[input_array[location[0]][location[1]] + location[2]]
    return [location[0] + points[0], location[1] + points[1], points[2]]

startPoint = getStartPoint()

directions = getDirections(startPoint)

steps = 1
while(directions[0][0] != startPoint[0] or directions[0][1] != startPoint[1]):
    directions[0] = getNextLocation(directions[0])
    steps += 1

print(steps//2)