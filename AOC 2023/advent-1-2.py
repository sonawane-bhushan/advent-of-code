from pathlib import Path

p = Path(__file__).with_name('advent-1-data.txt')

with p.open("r") as f:
        input_array = f.read().splitlines() 

sum = 0
validDigits = {"one": '1', "two": '2', "three": '3', "four": '4', "five": '5', "six": '6', "seven": '7', "eight": '8', "nine": '9'}

for data in input_array:
    i = -1
    val = ''
    for characters in data:
        for keys in validDigits:
            if(data[i:].startswith(keys)):
                data = data[:i] + validDigits[keys] + data[i+1:]
        i += 1
    calibrationValue = ""
    for character in data:
        if(character >= '0' and character <= '9'):
            if(len(calibrationValue) == 0):
                calibrationValue += character
            elif(len(calibrationValue) <= 2):
                calibrationValue = calibrationValue[:1] + character
        if(len(calibrationValue) == 1):
            calibrationValue += calibrationValue
    sum += int(calibrationValue)

print(sum)