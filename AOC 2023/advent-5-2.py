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

def getReverseInRange(inputArray, input):
    for rangeArray in inputArray:
        sourceRanges = [rangeArray[0], rangeArray[0] + rangeArray[2] + 1]
        if(input in range(sourceRanges[0], sourceRanges[1])):
            return rangeArray[1] + (input - sourceRanges[0])
    return input

def getLocation(seed):
    soil = getInRange(seedToSoilMap, seed)
    fertilizer = getInRange(soilToFertilizerMap, soil)
    water = getInRange(fertilizerToWaterMap, fertilizer)
    light = getInRange(waterToLightMap, water)
    temperature = getInRange(lightToTemperatureMap, light)
    humidity = getInRange(temperatureToHumidityMap, temperature)
    return getInRange(humidityToLocationMap, humidity)

def getSeed(location):
    humidity = getReverseInRange(humidityToLocationMap, location)
    temperature = getReverseInRange(temperatureToHumidityMap, humidity)
    light = getReverseInRange(lightToTemperatureMap, temperature)
    water = getReverseInRange(waterToLightMap, light)
    fertilizer = getReverseInRange(fertilizerToWaterMap, water)
    soil = getReverseInRange(soilToFertilizerMap, fertilizer)
    return getReverseInRange(seedToSoilMap, soil)

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

i = 0
location = 0
while(location == 0):
    calculatedSeed = getSeed(i)
    for j in range(0, len(seeds), 2):
        if(calculatedSeed >= seeds[j] and calculatedSeed <= seeds[j] + seeds[j+1]):
            print("found seed " + str(calculatedSeed) + " at location " + str(i))
            location = i
            break
    i += 1

print(location)