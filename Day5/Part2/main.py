import re
from multiprocessing import Pool

def useMap(input, map):
  for line in map:
    if input >= line[1] and input < line[1] + line[2]:
      return line[0] + (input - line[1])
  return input
      
def task(start, length, seedToSoilMap, soilToFertilizerMap, fertilizerToWaterMap, waterToLightMap, lightToTemperatureMap, temperatureToHumidityMap, humidityToLocationMap):
  initialSeeds = []
  minimum = None
  for i in range(length):
    seed = start+i
    soilMapping = []
    fertilizerMapping = []
    waterMapping = []
    lightMapping = []
    temperatureMapping = []
    humidityMapping = []
    locationMapping = []
    soil = useMap(seed, seedToSoilMap)
    fertilizer = useMap(soil, soilToFertilizerMap)
    water = useMap(fertilizer, fertilizerToWaterMap)
    light = useMap(water, waterToLightMap)
    temperature = useMap(light, lightToTemperatureMap)
    humidity = useMap(temperature, temperatureToHumidityMap)
    location = useMap(humidity, humidityToLocationMap)
    if minimum is None or location < minimum:
      minimum = location
  return minimum

def main():
  try: 
    with open("input.txt") as inputFile:
      inputGroups = inputFile.read().split('\n\n')
      initialSeedsString = inputGroups[0]
      seedToSoilString = inputGroups[1]
      soilToFertilizerString = inputGroups[2]
      fertilizerToWaterString = inputGroups[3]
      waterToLightString = inputGroups[4]
      lightToTemperatureString = inputGroups[5]
      temperatureToHumidityString = inputGroups[6]
      humidityToLocationString = inputGroups[7]
      incorrectInitialSeeds = list(map(lambda x: (int(x[0]), int(x[1])), re.findall(r'(\d+) (\d+)', initialSeedsString)))
      seedToSoilMap = []
      soilToFertilizerMap = []
      fertilizerToWaterMap = []
      waterToLightMap = []
      lightToTemperatureMap = []
      temperatureToHumidityMap = []
      humidityToLocationMap = []
      for row in seedToSoilString.split('\n')[1:]:
        seedToSoilMap.append(list(map(lambda x: int(x), re.findall(r'(\d+)', row))))
      for row in soilToFertilizerString.split('\n')[1:]:
        soilToFertilizerMap.append(list(map(lambda x: int(x), re.findall(r'(\d+)', row))))
      for row in fertilizerToWaterString.split('\n')[1:]:
        fertilizerToWaterMap.append(list(map(lambda x: int(x), re.findall(r'(\d+)', row))))
      for row in waterToLightString.split('\n')[1:]:
        waterToLightMap.append(list(map(lambda x: int(x), re.findall(r'(\d+)', row))))
      for row in lightToTemperatureString.split('\n')[1:]:
        lightToTemperatureMap.append(list(map(lambda x: int(x), re.findall(r'(\d+)', row))))
      for row in temperatureToHumidityString.split('\n')[1:]:
        temperatureToHumidityMap.append(list(map(lambda x: int(x), re.findall(r'(\d+)', row))))
      for row in humidityToLocationString.split('\n')[1:]:
        humidityToLocationMap.append(list(map(lambda x: int(x), re.findall(r'(\d+)', row))))
      minimum = None

# Great candidate for parallelization if i get bored in the future

      with Pool() as pool:
        localMins = pool.starmap(task, 
        [(start, length, seedToSoilMap, soilToFertilizerMap, fertilizerToWaterMap, waterToLightMap, 
          lightToTemperatureMap, temperatureToHumidityMap, humidityToLocationMap) 
         for start, length in incorrectInitialSeeds])
        
      print(min(localMins))

      
      
  except FileNotFoundError: 
    print("Error: File 'input.txt' not found")
  except Exception as e:
    print(f"Error: {e}")

if __name__ == "__main__":
  main()