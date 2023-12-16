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

output = 0

for i in input_array[0].split(','):
    output += calculateHash(i)

print(output)