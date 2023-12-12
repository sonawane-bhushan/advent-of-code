from pathlib import Path

p = Path(__file__).with_name('advent-9-data.txt')

with p.open("r") as f:
    input_array = f.read().splitlines()

def getLast(inputSequence: list):
    differenceSequence = []
    for i, num in enumerate(inputSequence):
        if i == 0:
            continue
        differenceSequence.append(num - inputSequence[i - 1])
    if all(v == 0 for v in differenceSequence):
        return inputSequence[0]
    return inputSequence[-1] + getLast(differenceSequence)

result = 0

for input in input_array:
    sequence = list(reversed([int(x) for x in input.split(" ")]))
    result += getLast(sequence)

print(result)