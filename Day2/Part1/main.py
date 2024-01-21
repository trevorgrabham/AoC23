import re

def main():
  maxRed = 12
  maxGreen = 13
  maxBlue = 14
  try:
    with open("input.txt") as inputFile:
      possibleGameIds = []
      redPattern = r'.*?(\d+) red.*?'
      greenPattern = r'.*?(\d+) green.*?'
      bluePattern = r'.*?(\d+) blue.*?'
      gameIdPattern = r'Game (\d+)'
      inputLines = inputFile.read().split('\n')
      for line in inputLines:
        possibleGame = True
        gameIdString = line.split(':')[0]
        gameId = re.match(gameIdPattern, gameIdString).group(1)
        bagSubsets = line.split(':')[1].split(';')
        print(bagSubsets)
        for subset in bagSubsets:
          redMatch = re.match(redPattern, subset)
          greenMatch = re.match(greenPattern, subset)
          blueMatch = re.match(bluePattern, subset)
          if redMatch and int(redMatch.group(1)) > maxRed:
            possibleGame = False
            break
          if greenMatch and int(greenMatch.group(1)) > maxGreen:
            possibleGame = False
            break
          if blueMatch and int(blueMatch.group(1)) > maxBlue:
            possibleGame = False
            break
        if possibleGame:
          possibleGameIds.append(int(gameId))
      print(sum(possibleGameIds))
  except FileNotFoundError: 
    print("Error: File 'input.txt' not found")
  except Exception as e:
    print(f"Error: {e}")

if __name__ == "__main__":
  main()