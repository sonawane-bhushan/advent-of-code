from pathlib import Path

p = Path(__file__).with_name('advent-15-data.txt')

with p.open("r") as f:
    input_array = f.read().splitlines()

def calculateHash(input: str):
    currentValue = 0
    for i in input:
        currentValue += ord(i)
        currentValue *= 17
        currentValue %= 256
    return currentValue

lensArray =  [[] for _ in range(256)]

for i in input_array[0].split(','):
    if('=' in i):
        input = i.split('=')
        label = input[0]
        focalLength = input[1]
        hashedLabel = calculateHash(label)
        updated = False
        for j, lens in enumerate(lensArray[hashedLabel]):
            if label in lens:
                lensArray[hashedLabel][j] = i
                updated = True
                break
        if not updated:
            lensArray[hashedLabel].append(i)
    else:
        label = i[:-1]
        hashedLabel = calculateHash(label)
        for j, lens in enumerate(lensArray[hashedLabel]):
            if label in lens:
                lensArray[hashedLabel].pop(j)
                break

output = 0

for i, box in enumerate(lensArray):
    for j, lens in enumerate(box):
        output += (i + 1) * (j + 1) * int(lens.split('=')[1])

print(output)