from pathlib import Path
import re
import math

p = Path(__file__).with_name('advent-8-data.txt')

with p.open("r") as f:
    input_array = f.read().splitlines()

nodes = dict()

path = input_array[0]

for input in input_array[2:]:
    regex = r'\w+'
    keys = re.findall(regex, input)
    nodes[keys[0]] = (keys[1], keys[2])

startingPoints = []

for keys in nodes:
    if keys.endswith('A'):
        startingPoints.append(keys)

print(startingPoints)

distances = []

for points in startingPoints:

    i = 0 
    steps = 0
    destinationNode = points

    while(destinationNode.endswith('Z') == False):
        if(path[i] == 'R'):
            destinationNode = nodes[destinationNode][1]
        elif(path[i] == 'L'):
            destinationNode = nodes[destinationNode][0]
        if(i >= len(path) - 1):
            i = 0
        else:
            i += 1
        steps += 1
    
    distances.append(steps)

result = 1 

for distance in distances:
    result = math.lcm(result, distance)

print(result)