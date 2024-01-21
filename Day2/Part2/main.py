import re

def main():
  try:
    with open("input.txt") as inputFile:
      cubePowers = []
      redPattern = r'.*?(\d+) red.*?'
      greenPattern = r'.*?(\d+) green.*?'
      bluePattern = r'.*?(\d+) blue.*?'
      inputLines = inputFile.read().split('\n')
      for line in inputLines:
        bagSubsets = line.split(':')[1].split(';')
        maxRed = 0
        maxGreen = 0 
        maxBlue = 0
        for subset in bagSubsets:
          redMatch = re.match(redPattern, subset)
          greenMatch = re.match(greenPattern, subset)
          blueMatch = re.match(bluePattern, subset)
          if redMatch:
            if int(redMatch.group(1)) > maxRed:
              maxRed = int(redMatch.group(1))
          if greenMatch:
            if int(greenMatch.group(1)) > maxGreen:
              maxGreen = int(greenMatch.group(1))
          if blueMatch:
            if int(blueMatch.group(1)) > maxBlue:
              maxBlue = int(blueMatch.group(1))
        cubePowers.append(maxRed*maxGreen*maxBlue)
      print(sum(cubePowers))
  except FileNotFoundError: 
    print("Error: File 'input.txt' not found")
  except Exception as e:
    print(f"Error: {e}")

if __name__ == "__main__":
  main()