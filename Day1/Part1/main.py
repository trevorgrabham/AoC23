def main():
  try:
    with open("input.txt", 'r') as inputFile:
      inputLines = inputFile.read().split('\n')
      calibrationValues = []
      for line in inputLines:
        digits = [c for c in line if c.isdigit()]
        calibrationValues.append(int(f"{digits[0]}{digits[-1]}"))
      print(sum(calibrationValues))  
  except FileNotFoundError: 
    print("Error: File 'input.txt' not found")
  except Exception as e:
    print(f"Error: {e}")

if __name__ == "__main__":
  main()