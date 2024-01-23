import re
from functools import total_ordering

class Hand:

  typeRankings = {'FiveOfAKind': 7, 'FourOfAKind': 6, 'FullHouse': 5, 'ThreeOfAKind': 4, 'TwoPair': 3, 'OnePair': 2, 'HighCard': 1}
  cardRankings = {'A': 13, 'K': 12, 'Q': 11, 'J': 10, 'T': 9, '9': 8, '8': 7, '7': 6, '6':5, '5': 4, '4': 3, '3': 2, '2': 1}

  def __eq__(self, other):
    for s, o in zip(self.cardOrdering, other.cardOrdering):
      if s != o:
        return False
    return True

  def __lt__(self, other):
    if self.type is not None and other.type is not None and Hand.typeRankings[self.type] == Hand.typeRankings[other.type]:
      if Hand.cardRankings[self.cards[0]] is not None and Hand.cardRankings[other.cards[0]] is not None and Hand.cardRankings[self.cards[0]] == Hand.cardRankings[other.cards[0]]:
        if Hand.cardRankings[self.cards[1]] is not None and Hand.cardRankings[other.cards[1]] is not None and Hand.cardRankings[self.cards[1]] == Hand.cardRankings[other.cards[1]]:
          if Hand.cardRankings[self.cards[2]] is not None and Hand.cardRankings[other.cards[2]] is not None and Hand.cardRankings[self.cards[2]] == Hand.cardRankings[other.cards[2]]:
            if Hand.cardRankings[self.cards[3]] is not None and Hand.cardRankings[other.cards[3]] is not None and Hand.cardRankings[self.cards[3]] == Hand.cardRankings[other.cards[3]]:
              if Hand.cardRankings[self.cards[4]] is not None and Hand.cardRankings[other.cards[4]] is not None and Hand.cardRankings[self.cards[4]] == Hand.cardRankings[other.cards[4]]:
                return False
              else:
                if self.cards[4] is None: 
                  return True
                elif other.cards[4] is None: 
                  return False
                else:
                  return Hand.cardRankings[self.cards[4]] < Hand.cardRankings[other.cards[4]]
            else:
              if self.cards[3] is None:
                return True
              elif other.cards[3] is None: 
                return False
              else:
                return Hand.cardRankings[self.cards[3]] < Hand.cardRankings[other.cards[3]]
          else:
            if self.cards[2] is None:
              return True
            elif other.cards[2] is None:
              return False
            else:
              return Hand.cardRankings[self.cards[2]] < Hand.cardRankings[other.cards[2]]
        else:
          if self.cards[1] is None:
            return True
          elif other.cards[1] is None: 
            return False 
          else: 
            return Hand.cardRankings[self.cards[1]] < Hand.cardRankings[other.cards[1]]
      else:
        if self.cards[0] is None:
          return True
        elif other.cards[0] is None:
          return False
        else: 
          return Hand.cardRankings[self.cards[0]] < Hand.cardRankings[other.cards[0]]
    else:
      if self.type is None:
        return True
      elif other.type is None: 
        return False 
      else:
        return Hand.typeRankings[self.type] < Hand.typeRankings[other.type]
  
  def __str__(self): 
    formattedString = f'Hand: {self.cards}\nBet: {self.bet}\nType: {self.type}\nHigh Card: {self.highCard}'
    if self.secondHigh is not None:
      formattedString += f'\nSecond High: {self.secondHigh}'
    if self.thirdHigh is not None:
      formattedString += f'\nThird High: {self.thirdHigh}'
    if self.fourthHigh is not None:
      formattedString += f'\nFourth High: {self.fourthHigh}'
    if self.type == 'HighCard':
      formattedString += f'\nFifth High: {self.cardOrdering[4]}'
    return formattedString

  def checkFiveOfAKind(self):
    if self.cardOrdering[0] == self.cardOrdering[4]:
      self.type = 'FiveOfAKind'
      self.highCard = self.cardOrdering[0]
      return
    self.checkFourOfAKind()
  
  def checkFourOfAKind(self):
    if self.cardOrdering[0] == self.cardOrdering[3]:
      self.type = 'FourOfAKind'
      self.highCard = self.cardOrdering[0]
      self.secondHigh = self.cardOrdering[4]
      return
    elif self.cardOrdering[1] == self.cardOrdering[4]:
      self.type = 'FourOfAKind'
      self.highCard = self.cardOrdering[1]
      self.secondHigh = self.cardOrdering[0]
      return
    self.checkFullHouse()

  def checkFullHouse(self):
    if self.cardOrdering[0] == self.cardOrdering[1] and self.cardOrdering[0] == self.cardOrdering[2]:
      if self.cardOrdering[3] == self.cardOrdering[4]:
        self.type = 'FullHouse'
        self.highCard = self.cardOrdering[0]
        self.secondHigh = self.cardOrdering[4]
      else:
        self.type = 'ThreeOfAKind'
        self.highCard = self.cardOrdering[0]
        self.secondHigh = self.cardOrdering[3]
        self.thirdHigh = self.cardOrdering[4]
    elif self.cardOrdering[2] == self.cardOrdering[3] and self.cardOrdering[2] == self.cardOrdering[4]:
      if self.cardOrdering[0] == self.cardOrdering[1]:
        self.type = 'FullHouse'
        self.highCard = self.cardOrdering[4]
        self.secondHigh = self.cardOrdering[0]
      else:
        self.type = 'ThreeOfAKind'
        self.highCard = self.cardOrdering[4]
        self.secondHigh = self.cardOrdering[0]
        self.thirdHigh = self.cardOrdering[1]
    else:
      self.checkThreeOfAKind()
  
  def checkThreeOfAKind(self):
    i = 0
    while i < 3:
      if self.cardOrdering[i] == self.cardOrdering[i+1] and self.cardOrdering[i] == self.cardOrdering[i+2]:
        self.type = 'ThreeOfAKind'
        self.highCard = self.cardOrdering[i]
        break
      i += 1
    if i == 0:
      self.secondHigh = self.cardOrdering[3]
      self.thirdHigh = self.cardOrdering[4]
    elif i == 1:
      self.secondHigh = self.cardOrdering[0]
      self.thirdHigh = self.cardOrdering[4]
    elif i == 2:
      self.secondHigh = self.cardOrdering[0]
      self.thirdHigh = self.cardOrdering[1]
    else:
      self.checkPairOrTwoPair()
  
  def checkPairOrTwoPair(self):
    i = 0
    while i < 4:
      if self.cardOrdering[i] == self.cardOrdering[i+1]:
        self.type = 'OnePair'
        self.highCard = self.cardOrdering[i]
        break
      i += 1
    j = i + 1
    while j < 4:
      if self.cardOrdering[j] == self.cardOrdering[j+1]:
        self.type = 'TwoPair'
        self.secondHigh = self.cardOrdering[j]
        break
      j += 1
    if j >= 4:
      if i == 0:
        self.secondHigh = self.cardOrdering[2]
        self.thirdHigh = self.cardOrdering[3]
        self.fourthHigh = self.cardOrdering[4]
      elif i == 1:
        self.secondHigh = self.cardOrdering[0]
        self.thirdHigh = self.cardOrdering[3]
        self.fourthHigh = self.cardOrdering[4]
      elif i == 2:
        self.secondHigh = self.cardOrdering[0]
        self.thirdHigh = self.cardOrdering[1]
        self.fourthHigh = self.cardOrdering[4]
      elif i == 3:
        self.secondHigh = self.cardOrdering[0]
        self.thirdHigh = self.cardOrdering[1]
        self.fourthHigh = self.cardOrdering[2]
      else: 
        self.type = 'HighCard'
        self.highCard = self.cardOrdering[0]
        self.secondHigh = self.cardOrdering[1]
        self.thirdHigh = self.cardOrdering[2]
        self.fourthHigh = self.cardOrdering[3]
        self.fifthHigh = self.cardOrdering[4]
    else: 
      if i == 0: 
        if j == 2:
          self.thirdHigh = self.cardOrdering[4]
        else:
          self.thirdHigh = self.cardOrdering[2]
      elif i == 1:
        self.thirdHigh = self.cardOrdering[0]

  def __init__(self, cardString, bet):
    self.type = None 
    self.highCard = None 
    self.secondHigh = None
    self.thirdHigh = None
    self.fourthHigh = None 
    self.fifthHigh= None 
    self.bet = bet
    self.cards = [card for card in cardString]
    self.cardOrdering = [Hand.cardRankings[card] for card in cardString]
    self.cardOrdering.sort(reverse = True)

    self.checkFiveOfAKind()

def main():
  try: 
    with open("input.txt") as inputFile:
      inputLines = inputFile.read().split('\n')
      hands = []
      total = 0
      for line in inputLines: 
        handString, betString = line.split(' ')
        hands.append(Hand(handString, int(betString)))
      hands.sort()
      for index,hand in enumerate(hands):
        print(f'{hand.type}\t\t\t{hand.cards}\t\t\t{hand.bet}\t\t\t{index+1}\t\t\t\t\t\t{total}')
        total += (index+1)*hand.bet
      print(total)

              
  except FileNotFoundError: 
    print("Error: File 'input.txt' not found")
  except Exception as e:
    print(f"Error: {e}")

if __name__ == "__main__":
  main()