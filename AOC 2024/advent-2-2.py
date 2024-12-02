from pathlib import Path

p = Path(__file__).with_name('advent-2-data.txt')

l1, l2 = [], []

with p.open("r") as f:
    input_array = f.read().splitlines()

def isLevelUnsafe(levels):
    isAscending = True if levels[0] < levels[1] else False
    if isAscending:
        for j in range(len(levels) - 1):
            if(levels[j] > levels[j+1] or (levels[j+1] - levels[j] < 1 or levels[j+1] - levels[j] > 3)):
                return j
        return -1
    else:
        for j in range(len(levels) - 1):
            if(levels[j] < levels[j+1] or (levels[j] - levels[j+1] < 1 or levels[j] - levels[j+1] > 3)):
                return j
        return -1
    
def deleteElementByIndex(list, index):
    return list[:index] + list[index+1:]

safeLevels = 0

for i in input_array:
    data = [int(x.strip()) for x in i.split(' ')]
    unsafeLevel = isLevelUnsafe(data)
    if(unsafeLevel == -1):
        safeLevels += 1
    else:
        for i in range(len(data)):
            levels = deleteElementByIndex(data, i)
            if(isLevelUnsafe(levels) == -1):
                safeLevels += 1
                break

print(safeLevels)