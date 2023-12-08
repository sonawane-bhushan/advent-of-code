from pathlib import Path

p = Path(__file__).with_name('advent-6-data.txt')

def getMinTime(time, distance):
    i = 1
    calculatedDistance = 0
    while(calculatedDistance <= distance):
        runDuration = time - i
        calculatedDistance = runDuration * i
        i += 1
    return i - 1

with p.open("r") as f:
    input_array = f.read().splitlines() 

times = None
distances = None

for input in (input_array):
    if(input.startswith('Time:')):
        times = int(input.split(':')[1].replace(' ', ''))
    if(input.startswith('Distance:')):
        distances = int(input.split(':')[1].replace(' ', ''))

minTime = getMinTime(times, distances)
maxTime = times - minTime
result = (maxTime - minTime + 1)
print(result)