from pathlib import Path
import re

p = Path(__file__).with_name('advent-8-data.txt')

with p.open("r") as f:
    input_array = f.read().splitlines()

nodes = dict()

path = input_array[0]

for input in input_array[2:]:
    regex = r'\w+'
    keys = re.findall(regex, input)
    nodes[keys[0]] = (keys[1], keys[2])

i = 0 
destinationNode = 'AAA'
steps = 0

while(destinationNode != 'ZZZ'):
    if(path[i] == 'R'):
        destinationNode = nodes[destinationNode][1]
    elif(path[i] == 'L'):
        destinationNode = nodes[destinationNode][0]
    if(i >= len(path) - 1):
        i = 0
    else:
        i += 1
    steps += 1

print(steps)