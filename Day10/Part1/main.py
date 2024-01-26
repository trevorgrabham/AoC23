import re
import traceback

def printPipes(A):
  for line in A:
    print(line)
  print()

def printContained(partOfLoop, contained):
  for row in range(len(contained)):
    lineString = ''
    for col in range(len(contained[0])):
      if partOfLoop[row][col]:
        lineString += '#'
      elif contained[row][col]:
        lineString += '@'
      else:
        lineString += '.'
    print(lineString)
  print()

def checkSurrounding(pipes, partOfLoop, row, col, queue):
  # up
  if row > 0 and partOfLoop[row-1][col] == False and (pipes[row-1][col] == '|' or pipes[row-1][col] == 'F' or pipes[row-1][col] == '7'):
    partOfLoop[row-1][col] = True
    queue.append((row-1, col))
  # down
  if row < len(pipes)-1 and partOfLoop[row+1][col] == False and (pipes[row+1][col] == '|' or pipes[row+1][col] == 'L' or pipes[row+1][col] == 'J'):
    partOfLoop[row+1][col] = True
    queue.append((row+1, col))
  # left
  if col > 0 and partOfLoop[row][col-1] == False and (pipes[row][col-1] == '-' or pipes[row][col-1] == 'L' or pipes[row][col-1] == 'F'):
    partOfLoop[row][col-1] = True
    queue.append((row, col-1))
  # right
  if col < len(pipes[0])-1 and partOfLoop[row][col+1] == False and (pipes[row][col+1] == '-' or pipes[row][col+1] == 'J' or pipes[row][col+1] == '7'):
    partOfLoop[row][col+1] = True
    queue.append((row, col+1))

def containedLeft(partOfLoop, pipes, row, col):
  numBoundries = 0
  for c in range(col):
    if partOfLoop[row][c] and (pipes[row][c] == '|' or pipes[row][c] == 'L' or pipes[row][c] == 'F' or pipes[row][c] == 'J' or pipes[row][c] == '7'):
      numBoundries += 1
  return numBoundries%2 != 0

def containedRight(partOfLoop, pipes, row, col):
  numBoundries = 0
  for c in range(col + 1, len(pipes[0])):
    if partOfLoop[row][c] and (pipes[row][c] == '|' or pipes[row][c] == 'L' or pipes[row][c] == 'F' or pipes[row][c] == 'J' or pipes[row][c] == '7'):
      numBoundries += 1
  return numBoundries%2 != 0

def containedDown(partOfLoop, pipes, row, col):
  numBoundries = 0
  for r in range(row):
    if partOfLoop[r][col] and (pipes[r][col] == '-' or pipes[r][col] == 'L' or pipes[r][col] == 'F' or pipes[r][col] == 'J' or pipes[r][col] == '7'):
      numBoundries += 1
  return numBoundries%2 != 0

def containedDown(partOfLoop, pipes, row, col):
  numBoundries = 0
  for r in range(row+1, len(pipes)):
    if partOfLoop[r][col] and (pipes[r][col] == '-' or pipes[r][col] == 'L' or pipes[r][col] == 'F' or pipes[r][col] == 'J' or pipes[r][col] == '7'):
      numBoundries += 1
  return numBoundries%2 != 0

def countContained(partOfLoop, pipes):
  contained = [[False] * len(pipes[0]) for _ in range(len(pipes))]
  for row in range(len(pipes)):
    for col in range(len(pipes[0])):
      contained[row][col] = containedLeft(partOfLoop, pipes, row, col) and containedRight(partOfLoop, pipes, row, col) and containedDown(partOfLoop, pipes, row, col) and containedUp(partOfLoop, pipes, row, col)
  return contained

def main():
  try: 
    with open("input.txt") as inputFile:
      pipeArray = inputFile.read().split('\n')
      partOfLoop = [[False] * len(pipeArray[0]) for _ in range(len(pipeArray))]
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
      partOfLoop[startingRow][startingCol] = True
      queue = [(startingRow, startingCol)]
      while len(queue) > 0:
        row, col = queue.pop(0)
        checkSurrounding(pipeArray, partOfLoop, row, col, queue)
      contained = countContained(partOfLoop, pipeArray)
      printContained(partOfLoop, contained)

          
  except FileNotFoundError: 
    print("Error: File 'input.txt' not found")
  except Exception as e:
    print(f"Error: {e}")
    traceback.print_exc()

if __name__ == "__main__":
  main()