from pathlib import Path

p = Path(__file__).with_name('advent-1-data.txt')

with p.open("r") as f:
        input_array = f.read().splitlines() 

sum = 0

for data in input_array:
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