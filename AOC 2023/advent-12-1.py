from pathlib import Path

p = Path(__file__).with_name('advent-12-data.txt')

with p.open("r") as f:
    input_array = f.read().splitlines()

def calculatePossibleCombinations(record: str, groups: tuple):

    if not groups:
        if '#' not in record:
            return 1
        else: 
            return 0
        
    if not record:
        return 0
    
    nextRecord = record[0]
    nextGroup = groups[0]

    def dot():
        return calculatePossibleCombinations(record[1:], groups)

    def pound():
        thisGroup = record[:nextGroup]
        thisGroup = thisGroup.replace("?", "#")

        if thisGroup != nextGroup * "#":
            return 0

        if len(record) == nextGroup:
            if len(groups) == 1:
                return 1
            else:
                return 0
        
        if record[nextGroup] in "?.":
            return calculatePossibleCombinations(record[nextGroup+1:], groups[1:])
        
        return 0
    
    if nextRecord == '#':
        out = pound()

    elif nextRecord == '.':
        out = dot()

    elif nextRecord == '?':
        out = dot() + pound()
            
    return out

output = 0

for input in input_array:
    record, rawGroup = input.split(' ')

    groups = [int(x) for x in rawGroup.split(',')]

    output += calculatePossibleCombinations(record, tuple(groups))

print(output)