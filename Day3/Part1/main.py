import re

def main():
  try: 
    with open("input.txt") as inputFile:
      inputArray = inputFile.read().split('\n')
      validPartNumbers = []
      for rowIndex, line in enumerate(inputArray):
        validColumns = [index for match in re.finditer(r'[^0-9.]', line) for index in (match.start()-1, match.start(), match.start()+1) if index >= 0 and index < len(inputArray)]
        if rowIndex > 0:
          validColumns = validColumns + [index for match in re.finditer(r'[^0-9.]', inputArray[rowIndex-1]) for index in (match.start()-1, match.start(), match.start()+1) if index >= 0 and index < len(inputArray)]
        if rowIndex < len(inputArray)-1:
          validColumns = validColumns + [index for match in re.finditer(r'[^0-9.]', inputArray[rowIndex+1]) for index in (match.start()-1, match.start(), match.start()+1) if index >= 0 and index < len(inputArray)]
        validColumns = list(set(validColumns))

        partNumbers = list(re.finditer(r'(\d+)', line))
        for part in partNumbers:
          start, end = part.span()
          for i in range(start, end):
            if i in validColumns:
              validPartNumbers.append(int(part.group(1)))
              break
      
      print(sum(validPartNumbers))


  except FileNotFoundError: 
    print("Error: File 'input.txt' not found")
  except Exception as e:
    print(f"Error: {e}")

if __name__ == "__main__":
  main()