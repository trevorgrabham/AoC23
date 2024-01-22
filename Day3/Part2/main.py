import re

def main():
  try: 
    with open("input.txt") as inputFile:
      inputArray = inputFile.read().split('\n')
      gearRatios = []
      for rowIndex, line in enumerate(inputArray):
        potentialGears = re.finditer(r'(\*)', line)
        surroundingNumbers = list(re.finditer(r'(\d+)', line))
        if rowIndex > 0: 
          surroundingNumbers += list(re.finditer(r'(\d+)', inputArray[rowIndex-1]))
        if rowIndex < len(inputArray)-1: 
          surroundingNumbers += list(re.finditer(r'(\d+)', inputArray[rowIndex+1]))
        for gearCandidate in potentialGears:
          surroundingNumbersCount = 0
          potentialGearRatio = 1
          for number in surroundingNumbers:
            start, end = number.span()
            end -= 1
            if gearCandidate.start() >= start-1 and gearCandidate.start() <= end+1:
              surroundingNumbersCount += 1
              potentialGearRatio *= int(number.group(1))
          if surroundingNumbersCount == 2:
            gearRatios.append(potentialGearRatio)
      print(sum(gearRatios))


  except FileNotFoundError: 
    print("Error: File 'input.txt' not found")
  except Exception as e:
    print(f"Error: {e}")

if __name__ == "__main__":
  main()