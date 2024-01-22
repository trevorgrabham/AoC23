import re

def useMap(input, map):
  for line in map:
    if input >= line[1] and input < line[1] + line[2]:
      return line[0] + (input - line[1])
  return input

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
      initialSeeds = list(map(lambda x: int(x), re.findall(r'(\d+)', initialSeedsString)))
      soilMapping = []
      fertilizerMapping = []
      waterMapping = []
      lightMapping = []
      temperatureMapping = []
      humidityMapping = []
      locationMapping = []
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
      for seed in initialSeeds:
        soilMapping.append(useMap(seed, seedToSoilMap))
      for soil in soilMapping:
        fertilizerMapping.append(useMap(soil, soilToFertilizerMap))
      for fertilizer in fertilizerMapping:
        waterMapping.append(useMap(fertilizer, fertilizerToWaterMap))
      for water in waterMapping:
        lightMapping.append(useMap(water, waterToLightMap))
      for light in lightMapping:
        temperatureMapping.append(useMap(light, lightToTemperatureMap))
      for temperature in temperatureMapping:
        humidityMapping.append(useMap(temperature, temperatureToHumidityMap))
      for humidity in humidityMapping:
        locationMapping.append(useMap(humidity, humidityToLocationMap))

      print(min(locationMapping))
      
      
  except FileNotFoundError: 
    print("Error: File 'input.txt' not found")
  except Exception as e:
    print(f"Error: {e}")

if __name__ == "__main__":
  main()