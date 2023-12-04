from pathlib import Path

p = Path(__file__).with_name('advent-4-data.txt')

with p.open("r") as f:
        input_array = f.read().splitlines() 

result = [1] * len(input_array)
for i, data in enumerate(input_array):
    input = data.split(': ')
    game = int(input[0].replace('Card ',''))
    numbers = input[1].split(' | ')
    winningNumbers = [x.strip() for x in numbers[0].split(' ') if x != '']
    drawnNumbers = [x.strip() for x in numbers[1].split(' ') if x != '']
    ticketResult = 0
    for digit in winningNumbers:
        if(digit in drawnNumbers):           
            ticketResult += 1
    for k in range(i + 1, i + 1 + ticketResult):
        if(k < len(input_array)):
            result[k] += result[i]

print(sum(result))