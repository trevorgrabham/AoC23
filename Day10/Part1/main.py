import re
import traceback

def printPipes(A):
  for line in A:
    print(line)
  print()

def printDistances(A):
  for line in A:
    string = ''
    for char in line:
      if char == -1:
        string += '.'
      else:
        string += str(char)
    print(string)
  print()

def checkSurrounding(pipes, distances, row, col, queue):
  # up
  if row > 0 and distances[row-1][col] == -1 and (pipes[row-1][col] == '|' or pipes[row-1][col] == 'F' or pipes[row-1][col] == '7'):
    distances[row-1][col] = distances[row][col] + 1
    queue.append((row-1, col))
  # down
  if row < len(pipes)-1 and distances[row+1][col] == -1 and (pipes[row+1][col] == '|' or pipes[row+1][col] == 'L' or pipes[row+1][col] == 'J'):
    distances[row+1][col] = distances[row][col] + 1
    queue.append((row+1, col))
  # left
  if col > 0 and distances[row][col-1] == -1 and (pipes[row][col-1] == '-' or pipes[row][col-1] == 'L' or pipes[row][col-1] == 'F'):
    distances[row][col-1] = distances[row][col] + 1
    queue.append((row, col-1))
  # right
  if col < len(pipes[0])-1 and distances[row][col+1] == -1 and (pipes[row][col+1] == '-' or pipes[row][col+1] == 'J' or pipes[row][col+1] == '7'):
    distances[row][col+1] = distances[row][col] + 1
    queue.append((row, col+1))

def main():
  try: 
    with open("input.txt") as inputFile:
      pipeArray = inputFile.read().split('\n')
      distanceArray = [[-1] * len(pipeArray[0]) for _ in range(len(pipeArray))]
      startingRow = -1
      startingCol = -1
      for row in range(len(pipeArray)):
        if 'S' in pipeArray[row]:
          for col in range(len(pipeArray[row])):
            if pipeArray[row][col] == 'S':
              startingRow = row
              startingCol = col
              break
          break
      distanceArray[startingRow][startingCol] = 0
      queue = [(startingRow, startingCol)]
      while len(queue) > 0:
        row, col = queue.pop(0)
        checkSurrounding(pipeArray, distanceArray, row, col, queue)
      maximum = 0
      for line in distanceArray:
        for num in line:
          if num > maximum:
            maximum = num
      print(maximum)
          
  except FileNotFoundError: 
    print("Error: File 'input.txt' not found")
  except Exception as e:
    print(f"Error: {e}")
    traceback.print_exc()

if __name__ == "__main__":
  main()