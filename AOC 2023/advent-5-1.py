from pathlib import Path
import sys

p = Path(__file__).with_name('advent-5-data.txt')

def getFiledArray(inputArray, index):
    result = []
    while(inputArray[index] != ''):
        result.append([int(x.strip()) for x in input_array[index].split(' ')])
        index += 1
    return result

def getInRange(inputArray, input):
    for rangeArray in inputArray:
        sourceRanges = [rangeArray[1], rangeArray[1] + rangeArray[2] + 1]
        if(input in range(sourceRanges[0], sourceRanges[1])):
            return rangeArray[0] + (input - sourceRanges[0])
    return input

with p.open("r") as f:
        input_array = f.read().splitlines() 

result = 0
seeds = []
seedToSoilMap = []
soilToFertilizerMap = []
fertilizerToWaterMap = []
waterToLightMap = []
lightToTemperatureMap = []
temperatureToHumidityMap = []


for i in range(len(input_array)):
    if(input_array[i].startswith('seeds: ')):
        seeds = [int(x.strip()) for x in input_array[i].split(': ')[1].split(' ') if x != '']
    if(input_array[i].startswith('seed-to-soil map:')):
        seedToSoilMap = getFiledArray(input_array, i+1)
    if(input_array[i].startswith('soil-to-fertilizer map:')):
        soilToFertilizerMap = getFiledArray(input_array, i+1)
    if(input_array[i].startswith('fertilizer-to-water map:')):
        fertilizerToWaterMap = getFiledArray(input_array, i+1)
    if(input_array[i].startswith('water-to-light map:')):
        waterToLightMap = getFiledArray(input_array, i+1)
    if(input_array[i].startswith('light-to-temperature map:')):
        lightToTemperatureMap = getFiledArray(input_array, i+1)
    if(input_array[i].startswith('temperature-to-humidity map:')):
        temperatureToHumidityMap = getFiledArray(input_array, i+1)
    if(input_array[i].startswith('humidity-to-location map:')):
        humidityToLocationMap = getFiledArray(input_array, i+1)
        
lowLocation = sys.maxsize

for seed in seeds:
    soil = getInRange(seedToSoilMap, seed)
    fertilizer = getInRange(soilToFertilizerMap, soil)
    water = getInRange(fertilizerToWaterMap, fertilizer)
    light = getInRange(waterToLightMap, water)
    temperature = getInRange(lightToTemperatureMap, light)
    humidity = getInRange(temperatureToHumidityMap, temperature)
    location = getInRange(humidityToLocationMap, humidity)
    if(location < lowLocation):
        lowLocation = location

print(lowLocation)  