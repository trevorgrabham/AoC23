import re

# symmetrical: if we hold it for one second, or if we hold it for time-1 seconds, we will go the same distance.
# 
# use this fact to instead of calculating all the possible ways that we can win, since we know that we will continue to lose 
# until we hold for long enough, calculate how long it is until we start to win, and then realize that if we lose the first n, 
# then with the symmetry we will also lost the last n, and duduct this 2n from the total number of possibilities, [0, time], = time + 1 ways

def main():
  try: 
    with open("input.txt") as inputFile:
      timeString, distanceString = inputFile.read().split('\n')
      time= int(re.sub(r'\s', '', timeString.split(':')[1]))
      distance = int(re.sub(r'\s', '', distanceString.split(':')[1]))
      numberOfWaysToLose = 0
      for i in range(time):
        if i*(time-i) > distance:
          break
        numberOfWaysToLose += 1
      print(time+1 - 2*numberOfWaysToLose)
              
  except FileNotFoundError: 
    print("Error: File 'input.txt' not found")
  except Exception as e:
    print(f"Error: {e}")

if __name__ == "__main__":
  main()