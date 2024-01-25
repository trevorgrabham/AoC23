import re
import traceback
from functools import total_ordering

class Hand:

  typeRankings = {'FiveOfAKind': 7, 'FourOfAKind': 6, 'FullHouse': 5, 'ThreeOfAKind': 4, 'TwoPair': 3, 'OnePair': 2, 'HighCard': 1}
  cardRankings = {'A': 13, 'K': 12, 'Q': 11, 'J': 1, 'T': 10, '9': 9, '8': 8, '7': 7, '6':6, '5': 5, '4': 4, '3': 3, '2': 2}

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
    return f'Hand: {self.cards}\nBet: {self.bet}\nType: {self.type}'

  def checkFiveOfAKind(self):
    if self.numberOfJacks == 5:
      self.type = 'FiveOfAKind'
      return
    if self.cardOrdering[0] == self.cardOrdering[4-self.numberOfJacks]:
      self.type = 'FiveOfAKind'
      return
    self.checkFourOfAKind()
  
  def checkFourOfAKind(self):
    if self.cardOrdering[0] == self.cardOrdering[4-self.numberOfJacks-1] or self.cardOrdering[1] == self.cardOrdering[4-self.numberOfJacks]:
      self.type = 'FourOfAKind'
      return
    self.checkFullHouse()

  def checkFullHouse(self):
    if self.numberOfJacks == 0:
      if self.cardOrdering[0] == self.cardOrdering[1] and self.cardOrdering[0] == self.cardOrdering[2]:
        if self.cardOrdering[3] == self.cardOrdering[4]:
          self.type = 'FullHouse'
        else:
          self.type = 'ThreeOfAKind'
      elif self.cardOrdering[2] == self.cardOrdering[3] and self.cardOrdering[2] == self.cardOrdering[4]:
        if self.cardOrdering[0] == self.cardOrdering[1]:
          self.type = 'FullHouse'
        else:
          self.type = 'ThreeOfAKind'
      else:
        self.checkThreeOfAKind()
    elif self.numberOfJacks == 1:
      if self.cardOrdering[0] == self.cardOrdering[1] and self.cardOrdering[2] == self.cardOrdering[3]:
        self.type = 'FullHouse'
      else: 
        self.checkThreeOfAKind()
    else: # must be two 'J' cards, otherwise if there were 3 or more, we would be guaranteed a four or five of a kind
      self.type = 'ThreeOfAKind'
  
  def checkThreeOfAKind(self):
    if self.numberOfJacks == 1:
      if self.cardOrdering[0] == self.cardOrdering[1] or self.cardOrdering[1] == self.cardOrdering[2] or self.cardOrdering[2] == self.cardOrdering[3]:
        self.type = 'ThreeOfAKind'
        return
      else:
        self.type = 'OnePair'
        return
    i = 0
    while i < 3:
      if self.cardOrdering[i] == self.cardOrdering[i+1] and self.cardOrdering[i] == self.cardOrdering[i+2]:
        self.type = 'ThreeOfAKind'
        return
      i += 1
    else:
      self.checkPairOrTwoPair()
  
  def checkPairOrTwoPair(self):
    i = 0
    while i < 4:
      if self.cardOrdering[i] == self.cardOrdering[i+1]:
        self.type = 'OnePair'
        break
      i += 1
    if i == 4:
      self.type = 'HighCard'
      return
    j = i + 1
    while j < 4:
      if self.cardOrdering[j] == self.cardOrdering[j+1]:
        self.type = 'TwoPair'
        return
      j += 1

  def __init__(self, cardString, bet):
    self.type = None 
    self.bet = bet
    self.cards = [card for card in cardString]
    self.numberOfJacks = len([card for card in cardString if card == 'J'])
    self.cardOrdering = [Hand.cardRankings[card] for card in cardString if card != 'J']
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
        total += (index+1)*hand.bet
      print(total)

              
  except FileNotFoundError: 
    print("Error: File 'input.txt' not found")
  except Exception as e:
    print(f"Error: {e}")
    traceback.print_exc()

if __name__ == "__main__":
  main()