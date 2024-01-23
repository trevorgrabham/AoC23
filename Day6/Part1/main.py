import re

def main():
  try: 
    with open("input.txt") as inputFile:
      timeString, distanceString = inputFile.read().split('\n')
      times = list(map(lambda x: int(x), re.findall(r'(\d+)', timeString.split(':')[1])))
      distances = list(map(lambda x: int(x), re.findall(r'(\d+)', distanceString.split(':')[1])))
      numberWaysToWin = [0] * len(times)
      for index in range(len(times)):
        time = times[index]
        distance = distances[index]
        for i in range(1, time):
          if i*(time-i) > distance: 
            numberWaysToWin[index] += 1
      productOfWins = 1
      for n in numberWaysToWin:
        productOfWins *= n
      print(productOfWins)
              
  except FileNotFoundError: 
    print("Error: File 'input.txt' not found")
  except Exception as e:
    print(f"Error: {e}")

if __name__ == "__main__":
  main()