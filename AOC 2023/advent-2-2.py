from pathlib import Path

p = Path(__file__).with_name('advent-2-data.txt')

with p.open("r") as f:
        input_array = f.read().splitlines() 

maxRed = 12
maxBlue = 14
maxGreen = 13
wholePowerSet = 0

for data in input_array:
    currentColourMax = {
        'red': 0,
        'blue': 0,
        'green': 0 
    }
    game = int(data.split(':')[0].replace('Game ',''))
    chances = data.split(': ')[1].split('; ')
    for chance in chances:
        chance = chance.split(', ')
        for dices in chance:
            for keys in currentColourMax:
                if keys in dices:
                    if(currentColourMax[keys] < int(dices.split(' ')[0])):
                        currentColourMax[keys] = int(dices.split(' ')[0])
    powerSet = currentColourMax['red'] * currentColourMax['green'] * currentColourMax['blue']
    wholePowerSet += powerSet

print(wholePowerSet)