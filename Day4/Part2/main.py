import re

def main():
  try: 
    with open("input.txt") as inputFile:
      cards = inputFile.read().split('\n')
      numberOfCardCopies = [1] * len(cards)
      for index, card in enumerate(cards): 
        winningNumbersString, myNumbersString = card.split(':')[1].split('|')
        winningNumbers = list(map(lambda x: int(x), re.findall(r'(\d+)', winningNumbersString)))
        myNumbers = list(map(lambda x: int(x), re.findall(r'(\d+)', myNumbersString)))
        numberMatchingNumbers = 0
        for number in myNumbers:
          if number in winningNumbers:
            numberMatchingNumbers += 1
        for i in range(1,numberMatchingNumbers+1):
          numberOfCardCopies[index+i] += numberOfCardCopies[index]
      print(sum(numberOfCardCopies))


  except FileNotFoundError: 
    print("Error: File 'input.txt' not found")
  except Exception as e:
    print(f"Error: {e}")

if __name__ == "__main__":
  main()