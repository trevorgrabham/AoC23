import re

def main():
  try:
    with open("input.txt", 'r') as inputFile:
      inputLines = inputFile.read().split('\n')
      calibrationValues = []
      digitPattern = r'^\D*(\d).*?(?:(\d)\D*)?$'
      for line in inputLines:
        digits = re.match(digitPattern, line)
        if digits.group(2) is None:
          calibrationValues.append(int(f"{digits.group(1)}{digits.group(1)}"))
        else:
          calibrationValues.append(int(f"{digits.group(1)}{digits.group(2)}"))
      print(sum(calibrationValues))  

  except FileNotFoundError: 
    print("Error: File 'input.txt' not found")
  except Exception as e:
    print(f"Error: {e}")

if __name__ == "__main__":
  main()