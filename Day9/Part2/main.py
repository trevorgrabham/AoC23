import re
import traceback

def differences(inputList):
  diffs = []
  for i in range(1,len(inputList)):
    diffs.append(inputList[i]-inputList[i-1])
  return diffs


def main():
  try: 
    with open("input.txt") as inputFile:
      inputLines = inputFile.read().split('\n')
      extrapolatedValues = []
      for line in inputLines:
        differenceLists = []
        lineNumbers = list(map(lambda x: int(x), re.findall(r'(-?\d+)', line)))
        diffs = lineNumbers
        differenceLists.append(diffs)
        while True:
          diffs = differences(diffs)
          differenceLists.append(diffs)
          if all([t==0 for t in diffs]):
            break
        length = len(differenceLists)
        for i in range(len(differenceLists)-1):
          differenceLists[length - 2 - i].insert(0, differenceLists[length - 2 - i][0] - differenceLists[length - 1 - i][0])
        extrapolatedValues.append(differenceLists[0][0])
      print(sum(extrapolatedValues))
          
  except FileNotFoundError: 
    print("Error: File 'input.txt' not found")
  except Exception as e:
    print(f"Error: {e}")
    traceback.print_exc()

if __name__ == "__main__":
  main()