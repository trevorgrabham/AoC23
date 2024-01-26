import re
import traceback

class Galaxy:
  def __init__(self, x, y):
    self.x = x
    self.y = y
  
  def distanceBetween(self, other):
    return (abs(self.x - other.x) + abs(self.y - other.y))

  def __str__(self):
    return f'({self.x}, {self.y})'

def printArray(A):
  for line in A:
    print(line)
  print()

def expandEmptySpace(A):
  rowsToExpand = []
  colsToExpand = []
  for row in range(len(A)):
    if '#' not in A[row]:
      rowsToExpand.append(row)
  for col in range(len(A[0])):
    galaxyFound = False
    for r in range(len(A)):
      if A[r][col] == '#':
        galaxyFound = True
        break
    if galaxyFound == False:
      colsToExpand.append(col)
  for col in reversed(colsToExpand):
    for r in range(len(A)):
      A[r] = A[r][:col] + '.' + A[r][col:]
  for row in reversed(rowsToExpand):
    A.insert(row, '.'*len(A[0]))

def findGalaxies(A):
  galaxies = []
  for row in range(len(A)):
    for col in range(len(A[0])):
      if A[row][col] == '#':
        galaxies.append(Galaxy(col, row))
  return galaxies

def main():
  try: 
    with open("input.txt") as inputFile:
      inputArray = inputFile.read().split('\n')
      expandEmptySpace(inputArray)
      galaxies = findGalaxies(inputArray)
      shortestPaths = []
      for index in range(len(galaxies)-1):
        for nextIndex in range(index+1, len(galaxies)):
          shortestPaths.append(galaxies[index].distanceBetween(galaxies[nextIndex]))
      print(sum(shortestPaths))

          
  except FileNotFoundError: 
    print("Error: File 'input.txt' not found")
  except Exception as e:
    print(f"Error: {e}")
    traceback.print_exc()

if __name__ == "__main__":
  main()