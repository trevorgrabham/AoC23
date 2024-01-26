import re
import traceback

def printPartOf(A):
  for row in range(len(A)):
    rowString = ''
    for col in range(len(A[0])):
      if A[row][col]:
        rowString += '#'
      else:
        rowString += '.'
    print(rowString)
  print()

def printPipes(partOfLoop, pipes):
  for row in range(len(pipes)):
    string = ''
    for col in range(len(pipes[0])):
      if partOfLoop[row][col]:
        string += pipes[row][col]
      else:
        string += '.'
    print(string)
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
  if (pipes[row][col] == 'S' or pipes[row][col] == '|' or pipes[row][col] == 'J' or pipes[row][col] == 'L') and row > 0 and partOfLoop[row-1][col] == False and (pipes[row-1][col] == '|' or pipes[row-1][col] == 'F' or pipes[row-1][col] == '7'):
    partOfLoop[row-1][col] = True
    queue.append((row-1, col))
  # down
  if (pipes[row][col] == 'S' or pipes[row][col] == '|' or pipes[row][col] == '7' or pipes[row][col] == 'F') and row < len(pipes)-1 and partOfLoop[row+1][col] == False and (pipes[row+1][col] == '|' or pipes[row+1][col] == 'L' or pipes[row+1][col] == 'J'):
    partOfLoop[row+1][col] = True
    queue.append((row+1, col))
  # left
  if (pipes[row][col] == 'S' or pipes[row][col] == '-' or pipes[row][col] == 'J' or pipes[row][col] == '7') and col > 0 and partOfLoop[row][col-1] == False and (pipes[row][col-1] == '-' or pipes[row][col-1] == 'L' or pipes[row][col-1] == 'F'):
    partOfLoop[row][col-1] = True
    queue.append((row, col-1))
  # right
  if (pipes[row][col] == 'S' or pipes[row][col] == '-' or pipes[row][col] == 'F' or pipes[row][col] == 'L') and col < len(pipes[0])-1 and partOfLoop[row][col+1] == False and (pipes[row][col+1] == '-' or pipes[row][col+1] == 'J' or pipes[row][col+1] == '7'):
    partOfLoop[row][col+1] = True
    queue.append((row, col+1))

def containedLeft(partOfLoop, pipes, row, col):
  numBoundries = 0
  foundF = False
  foundL = False
  for c in range(col):
    if partOfLoop[row][c] and pipes[row][c] == '|':
      numBoundries += 1
    elif partOfLoop[row][c] and pipes[row][c] == 'F':
      foundF = True
    elif partOfLoop[row][c] and pipes[row][c] == 'L':
      foundL = True
    elif partOfLoop[row][c] and pipes[row][c] == '7':
      if foundL: 
        numBoundries += 1
        foundL = False
      else:
        foundF = False
    elif partOfLoop[row][c] and pipes[row][c] == 'J':
      if foundL:
        foundL = False
      else:
        numBoundries += 1
        foundF = False
  return numBoundries%2 != 0

def containedRight(partOfLoop, pipes, row, col):
  numBoundries = 0
  foundF = False
  foundL = False
  for c in range(col + 1, len(pipes[0])):
    if partOfLoop[row][c] and pipes[row][c] == '|':
      numBoundries += 1
    elif partOfLoop[row][c] and pipes[row][c] == 'F':
      foundF = True
    elif partOfLoop[row][c] and pipes[row][c] == 'L':
      foundL = True
    elif partOfLoop[row][c] and pipes[row][c] == '7':
      if foundL: 
        numBoundries += 1
        foundL = False
      else:
        foundF = False
    elif partOfLoop[row][c] and pipes[row][c] == 'J':
      if foundF:
        numBoundries += 1
        foundF = False
      else:
        foundL = False
  return numBoundries%2 != 0

def containedUp(partOfLoop, pipes, row, col):
  numBoundries = 0
  foundF = False 
  found7 = False
  for r in range(row):
    if partOfLoop[r][col] and pipes[r][col] == '-':
      numBoundries += 1
    elif partOfLoop[r][col] and pipes[r][col] == 'F':
      foundF = True
    elif partOfLoop[r][col] and pipes[r][col] == '7':
      found7 = True 
    elif partOfLoop[r][col] and pipes[r][col] == 'J':
      if foundF:
        numBoundries += 1
        foundF = False
      else:
        found7 = False
    elif partOfLoop[r][col] and pipes[r][col] == 'L':
      if found7:
        numBoundries += 1 
        found7 = False 
      else:
        foundF = False
  return numBoundries%2 != 0

def containedDown(partOfLoop, pipes, row, col):
  numBoundries = 0
  foundF = False 
  found7 = False
  for r in range(row+1, len(pipes)):
    if partOfLoop[r][col] and pipes[r][col] == '-':
      numBoundries += 1
    elif partOfLoop[r][col] and pipes[r][col] == 'F':
      foundF = True
    elif partOfLoop[r][col] and pipes[r][col] == '7':
      found7 = True 
    elif partOfLoop[r][col] and pipes[r][col] == 'J':
      if foundF:
        numBoundries += 1
        foundF = False
      else:
        found7 = False
    elif partOfLoop[r][col] and pipes[r][col] == 'L':
      if found7:
        numBoundries += 1 
        found7 = False 
      else:
        foundF = False
  return numBoundries%2 != 0

def countContained(partOfLoop, pipes):
  contained = [[False] * len(pipes[0]) for _ in range(len(pipes))]
  for row in range(len(pipes)):
    for col in range(len(pipes[0])):
      if partOfLoop[row][col]:
        continue
      contained[row][col] = containedLeft(partOfLoop, pipes, row, col) and containedRight(partOfLoop, pipes, row, col) and containedDown(partOfLoop, pipes, row, col) and containedUp(partOfLoop, pipes, row, col)
  return contained

def changeS(pipes, row, col):
  # |
  if row > 0 and row < len(pipes) - 1 and (pipes[row-1][col] == '|' or pipes[row-1][col] == 'F' or pipes[row-1][col] == '7') and (pipes[row+1][col] == '|' or pipes[row+1][col] == 'J' or pipes[row+1][col] == 'L'):
    pipes[row] = pipes[row][:col] + '|' + pipes[row][col+1:]
  # -
  elif col > 0 and col < len(pipes[0]) - 1 and (pipes[row][col-1] == '-' or pipes[row][col-1] == 'F' or pipes[row][col-1] == 'L') and (pipes[row][col+1] == '-' or pipes[row][col+1] == '7' or pipes[row][col+1] == 'J'):
    pipes[row] = pipes[row][:col] + '-' + pipes[row][col+1:]
  # L
  elif col < len(pipes[0]) - 1 and row > 0 and (pipes[row-1][col] == '|' or pipes[row-1][col] == 'F' or pipes[row-1][col] == '7') and (pipes[row][col+1] == '-' or pipes[row][col+1] == '7' or pipes[row][col+1] == 'J'):
    pipes[row] = pipes[row][:col] + 'L' + pipes[row][col+1:]
  # F 
  elif col < len(pipes[0]) - 1 and row < len(pipes) and (pipes[row+1][col] == '|' or pipes[row+1][col] == 'J' or pipes[row+1][col] == 'L') and (pipes[row][col+1] == '-' or pipes[row][col+1] == '7' or pipes[row][col+1] == 'J'):
    pipes[row] = pipes[row][:col] + 'F' + pipes[row][col+1:]
  # 7
  elif col > 0 and row < len(pipes) and (pipes[row+1][col] == '|' or pipes[row+1][col] == 'J' or pipes[row+1][col] == 'L') and (pipes[row][col-1] == '-' or pipes[row][col-1] == 'L' or pipes[row][col-1] == 'F'):
    pipes[row] = pipes[row][:col] + '7' + pipes[row][col+1:]
  # J
  elif col > 0 and row > 0 and (pipes[row-1][col] == '|' or pipes[row-1][col] == 'F' or pipes[row-1][col] == '7') and (pipes[row][col-1] == '-' or pipes[row][col-1] == 'L' or pipes[row][col-1] == 'F'):
    pipes[row] = pipes[row][:col] + 'J' + pipes[row][col+1:]

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
      changeS(pipeArray, startingRow, startingCol)
      queue = [(startingRow, startingCol)]
      while len(queue) > 0:
        row, col = queue.pop(0)
        checkSurrounding(pipeArray, partOfLoop, row, col, queue)
      contained = countContained(partOfLoop, pipeArray)
      numContained = 0
      for row in range(len(contained)):
        for col in range(len(contained[0])):
          if contained[row][col]:
            numContained += 1
      print(numContained)

          
  except FileNotFoundError: 
    print("Error: File 'input.txt' not found")
  except Exception as e:
    print(f"Error: {e}")
    traceback.print_exc()

if __name__ == "__main__":
  main()