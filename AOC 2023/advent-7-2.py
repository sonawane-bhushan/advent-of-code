from pathlib import Path
from collections import Counter

p = Path(__file__).with_name('advent-7-data.txt')

with p.open("r") as f:
    input_array = f.read().splitlines()

power = {
    "A": 13,
    "K": 12,
    "Q": 11,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
    "J": 1
}

def handWithoutJoker(occurance: Counter):
    match occurance:
        # five of kind
        case [5]:
            return 6
        # four of kind
        case [4, 1]:
            return 5
        # full house
        case [3, 2]:
            return 4
        # Three of kind
        case [3, 1, 1]:
            return 3
        # Two pair
        case [2, 2, 1]:
            return 2
        # One Pair
        case [2, 1, 1, 1]:
            return 1
        # High card
        case [1, 1, 1, 1, 1]:
            return 0
        
def handWithJoker(occurance: Counter, countOfJokers: int):
    match occurance:
        # five of kind
        case [5]:
            return 6
        # four of kind
        case [4, 1]:
            return 6
        # full house
        case [3, 2]:
            return 6
        # Three of kind
        case [3, 1, 1]:
            return 5
        # Two pair
        case [2, 2, 1]:
            if(countOfJokers == 2):
                return 5
            else: 
                return 4
        # One Pair
        case [2, 1, 1, 1]:
            return 3
        # High card
        case [1, 1, 1, 1, 1]:
            return 1


class Hand:
    typeOfHand: int = None
    bid: int = None
    cards: list = None

    def __init__(self, cards, bid):
        self.bid = bid
        self.cards = list(cards)
        self.typeOfHand = self.getTypeOfHand()

    def getTypeOfHand(self):
        counter = Counter(self.cards)
        common = counter.most_common()

        occurance = [count for key, count in common]

        if(counter['J'] != 0):
            return handWithJoker(occurance, counter['J'])
        else:
            return handWithoutJoker(occurance)
            
    def __lt__(self, hand2: "Hand"):
        if(self.typeOfHand != hand2.typeOfHand):
            return self.typeOfHand < hand2.typeOfHand

        for i in range(5):
            if(self.cards[i] != hand2.cards[i]):
                return power[self.cards[i]] < power[hand2.cards[i]]

    def __str__(self):
        return f"{self.typeOfHand} @ C: {self.cards} B: {self.bid}"

hands = []

for input in input_array:
    cards = input.split(" ")[0]
    bid = input.split(" ")[1]
    hands.append(Hand(cards, bid))

hands.sort()

result = 0

for i, hand in enumerate(hands):
    result += (i + 1) * int(hand.bid)
    print(i+1, hand.cards)

print(result)