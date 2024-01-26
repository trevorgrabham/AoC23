import re
import traceback

expansionFactor =1000000 

class Galaxy:
  def __init__(self, x, y):
    self.x = x
    self.y = y
  
  def distanceBetween(self, other, expandedRows, expandedCols):
    minRow = min(self.y, other.y)
    maxRow = max(self.y, other.y)
    minCol = min(self.x, other.x)
    maxCol = max(self.x, other.x)
    expandedRowsBetween = len([row for row in expandedRows if row > minRow and row < maxRow])
    expandedColsBetween = len([col for col in expandedCols if col > minCol and col < maxCol])
    nonExpandedRowsBetween = abs(self.y - other.y) - expandedRowsBetween
    nonExpandedColsBetween = abs(self.x - other.x) - expandedColsBetween
    return (expandedColsBetween + expandedRowsBetween)*expansionFactor + (nonExpandedColsBetween + nonExpandedRowsBetween)

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
  return (rowsToExpand, colsToExpand)

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
      expandedRows, expandedCols = expandEmptySpace(inputArray)
      galaxies = findGalaxies(inputArray)
      shortestPaths = []
      for index in range(len(galaxies)-1):
        for nextIndex in range(index+1, len(galaxies)):
          shortestPaths.append(galaxies[index].distanceBetween(galaxies[nextIndex], expandedRows, expandedCols))
      print(sum(shortestPaths))

          
  except FileNotFoundError: 
    print("Error: File 'input.txt' not found")
  except Exception as e:
    print(f"Error: {e}")
    traceback.print_exc()

if __name__ == "__main__":
  main()