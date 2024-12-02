from pathlib import Path

p = Path(__file__).with_name('advent-2-data.txt')

l1, l2 = [], []

with p.open("r") as f:
    input_array = f.read().splitlines()

unsafeLevels = 0

for i in input_array:
    data = [int(x.strip()) for x in i.split(' ')]
    
    isAscending = True if data[0] < data[1] else False
    
    if isAscending:
        for j in range(len(data) - 1):
            if(data[j] > data[j+1] or (data[j+1] - data[j] < 1 or data[j+1] - data[j] > 3)):
                unsafeLevels += 1
                break
    else:
        for j in range(len(data) - 1):
            if(data[j] < data[j+1] or (data[j] - data[j+1] < 1 or data[j] - data[j+1] > 3)):
                unsafeLevels += 1
                break

print(len(input_array) - unsafeLevels)