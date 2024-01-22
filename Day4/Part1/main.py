import re

def main():
  try: 
    with open("input.txt") as inputFile:
      points = []
      cards = inputFile.read().split('\n')
      for index, card in enumerate(cards):
        numbers = card.split(':')[1]
        winningNumbersString, myNumbersString = numbers.split('|')
        winningNumbers = list(map(lambda x: int(x), re.findall(r'(\d+)', winningNumbersString)))
        myNumbers = list(map(lambda x: int(x), re.findall(r'(\d+)', myNumbersString)))
        cardPoints = 0
        for number in myNumbers:
          if number in winningNumbers:
            if cardPoints == 0:
              cardPoints = 1
            else: 
              cardPoints *= 2
        points.append(cardPoints)
      print(sum(points))

  except FileNotFoundError: 
    print("Error: File 'input.txt' not found")
  except Exception as e:
    print(f"Error: {e}")

if __name__ == "__main__":
  main()