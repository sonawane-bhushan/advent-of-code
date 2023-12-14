from pathlib import Path
import functools

p = Path(__file__).with_name('advent-12-data.txt')

with p.open("r") as f:
    input_array = f.read().splitlines()

#recursive_function(args):
    # check for exit condition
    # check for early cutoff (e.g. if it's possible to realize none of the children of this node matter to the final answer)
    # for each possible "move" (2 in this problem)
        # do move
        # call recursive_function with the new arguments
        # track something (best, worst, sum, whatever)
        # undo move
    # return something (best, worst, sum, whatever)

@functools.lru_cache(maxsize=None)
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

    record = ((record + '?') * 5) [:-1]

    groups = groups * 5 

    output += calculatePossibleCombinations(record, tuple(groups))

print(output)