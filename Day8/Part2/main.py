import re
import traceback
import threading
import queue

def task(startNode, nodeNetwork, instructions, messageQueue, lock, barrier, stopSignal):
  i = 0
  print(f'Thread {threading.current_thread().name} starting at {startNode}')
  while True:
    barrier.wait()
    if stopSignal.is_set():
      with lock:
        messageQueue.put(i)
      break
    left, right = re.findall(r'(\w+)', nodeNetwork[startNode])
    if instructions[i%len(instructions)] == 'R':
      startNode = right
    else:
      startNode = left
    with lock:
      messageQueue.put(startNode[-1] == 'Z') 
    i += 1
    barrier.wait()

class Node:
  def __init__(self, terminal):
    self.terminal = terminal
  
  def setLeft(self, left):
    self.left = left
  
  def setRight(self, right):
    self.right = right
  
  def update(self, instruction):
    if instruction == 'R':
      self.terminal = self.right.terminal
      self.left = self.right.left
      self.right = self.right.right
    elif instruction == 'L':
      self.terminal = self.left.terminal
      self.right = self.left.right
      self.left = self.left.left
    else:
      print('What the hell happened here')
  
  def isTerminal(self):
    return self.terminal
  
def main():
  try: 
    with open("input.txt") as inputFile:
      instructions, nodeNetworkString = inputFile.read().split('\n\n')
      instructions = re.match(r'(\w+)', instructions).group(1)
      nodeNetworkStrings = nodeNetworkString.split('\n')
      nodeNetwork = {}
      nodes = {}
      startNodes = []
      for nodeString in nodeNetworkStrings:
        currentNode, nextNodes = nodeString.split(' = ')
        nodeNetwork[currentNode] = nextNodes
        nodes[currentNode] = Node(currentNode[-1] == 'Z')
        if currentNode[-1] == 'A':
          startNodes.append(nodes[currentNode])
      for node, branches in nodeNetwork.items():
        left, right = re.findall(r'(\w+)', branches)
        nodes[node].setLeft(nodes[left])
        nodes[node].setRight(nodes[right])
      i = 0
      while True:
        allTerminal = True
        for node in startNodes:
          node.update(instructions[i%len(instructions)])
          allTerminal = allTerminal and node.isTerminal()
        i += 1
        if allTerminal:
          break
      print(i)

              
  except FileNotFoundError: 
    print("Error: File 'input.txt' not found")
  except Exception as e:
    print(f"Error: {e}")
    traceback.print_exc()

if __name__ == "__main__":
  main()