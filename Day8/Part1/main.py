import re
import traceback

def main():
  try: 
    with open("input.txt") as inputFile:
      instructions, nodeNetworkString = inputFile.read().split('\n\n')
      instructions = re.match(r'(\w+)', instructions).group(1)
      nodeNetworkStrings = nodeNetworkString.split('\n')
      nodeNetwork = {}
      for nodeString in nodeNetworkStrings:
        currentNode, nextNodes = nodeString.split(' = ')
        nodeNetwork[currentNode] = nextNodes
      
      i = 0
      currentNode = 'AAA'
      while True:
        options = re.findall(r'(\w+)', nodeNetwork[currentNode])
        left = options[0]
        right = options[1]
        if instructions[i%len(instructions)] == 'R':
          currentNode = right
        else:
          currentNode = left
        if currentNode == 'ZZZ':
          break
        i += 1
      
      print(i+1)
      
              
  except FileNotFoundError: 
    print("Error: File 'input.txt' not found")
  except Exception as e:
    print(f"Error: {e}")
    traceback.print_exc()

if __name__ == "__main__":
  main()