from pathlib import Path

p = Path(__file__).with_name('advent-4-data.txt')

with p.open("r") as f:
        input_array = f.read().splitlines() 

result = 0
for data in input_array:
    input = data.split(': ')
    game = int(input[0].replace('Card ',''))
    numbers = input[1].split(' | ')
    winningNumbers = [x.strip() for x in numbers[0].split(' ') if x != '']
    drawnNumbers = [x.strip() for x in numbers[1].split(' ') if x != '']
    n = 0
    ticketResult = 0
    for digit in winningNumbers:
        if(digit in drawnNumbers):
            if(n == 0):
                ticketResult = 1
            else:
                ticketResult *= 2
            n += 1
    result += ticketResult

print(result)