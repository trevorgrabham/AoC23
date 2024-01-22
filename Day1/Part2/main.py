import re 

def main():
  try:
    with open("input.txt", 'r') as inputFile:
      inputLines = inputFile.read().split("\n")
      calibrationValues = []
      wordToDigit = {'one': '1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}

      for lineNum, line in enumerate(inputLines):
        # need to use a positive lookahead assertion to find the overlapping matches, not just the non-overlapping matches
        digits = list(re.finditer(r'(?=(one|two|three|four|five|six|seven|eight|nine|[0-9]))', line))
        firstDigit = digits[0].group(1)
        if wordToDigit.get(firstDigit, None) is not None:
          firstDigit = wordToDigit[firstDigit]
        lastDigit = digits[-1].group(1)
        if wordToDigit.get(lastDigit, None) is not None:
          lastDigit = wordToDigit[lastDigit]
        calibrationValues.append(int(f"{firstDigit}{lastDigit}"))
      print(sum(calibrationValues))

  except FileNotFoundError: 
    print("Error: File 'input.txt' not found")
  except Exception as e:
    print(f"Error: {e}")

if __name__ == "__main__":
  main()