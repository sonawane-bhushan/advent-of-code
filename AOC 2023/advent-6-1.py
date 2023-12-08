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

times = []
distances = []

for input in (input_array):
    if(input.startswith('Time:')):
        times = [int(x.strip()) for x in input.split(':')[1].split(' ') if x != '']
    if(input.startswith('Distance:')):
        distances = [int(x.strip()) for x in input.split(':')[1].split(' ') if x != '']

result = 1

for i in range(len(times)):
    minTime = getMinTime(times[i], distances[i])
    maxTime = times[i] - minTime
    result *= (maxTime - minTime + 1)
print(result)