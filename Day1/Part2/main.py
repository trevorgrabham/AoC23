def main():
  try:
    with open("input.txt", 'r') as inputFile:
      inputLines = inputFile.read().split("\n")
      calibrationValues = []
      spellings = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
      # the last entries for replacements and lengths are the default values for when we do not have a spelt digit, or when there exists only one
      replacements = ["1", "2", "3", "4", "5", "6", "7", "8", "9", ""]
      lengths = [3, 3, 5, 4, 4, 3, 5, 5, 4, 0]

      for line in inputLines:
        first = len(spellings)
        last = -1
        firstIndex = len(line)
        lastIndex = -1
        for i in range(len(spellings)):
          index = line.find(spellings[i])
          if(index != -1 and index < firstIndex):
            first = i
            firstIndex = index
          index = line.rfind(spellings[i])
          if(index > lastIndex):
            last = i
            lastIndex = index

        # for the cases when we have < 2 spelt digits
        if firstIndex == len(line):
          firstIndex = 0
        if last == -1 or lastIndex == firstIndex:
          last = len(spellings)
          lastIndex = len(line)

        # replacing the first and last spelt digits with their numeric counterparts (still works for when there are < 2 of them)
        line = f"{line[:firstIndex]}{replacements[first]}{line[firstIndex+lengths[first]:lastIndex]}{replacements[last]}{line[lastIndex+lengths[last]:]}"

        digits = [c for c in line if c.isdigit()]
        calibrationValues.append(int(f"{digits[0]}{digits[-1]}"))
      print(sum(calibrationValues))  
  except FileNotFoundError: 
    print("Error: File 'input.txt' not found")
  except Exception as e:
    print(f"Error: {e}")

if __name__ == "__main__":
  main()