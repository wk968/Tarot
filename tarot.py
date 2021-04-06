import random
import json

class Card:
    def __init__(self,suit,val):
        self.suit = suit
        self.value = val
    
    def show(self):
        return ("{} of {}".format(self.value,self.suit))

class Deck:
    def __init__(self):
        self.cards = []
        self.build()
    
    def build(self):
        for a in ["Cups","Pentacles","Swords","Wands","Major"]:
            if a=="Major":
                for b in range (0,22):
                    self.cards.append(Card(a,b))
            else:
                for b in range (1,15):
                    self.cards.append(Card(a,b))
        
    def show(self):
        for c in self.cards:
            c.show()

    def shuffle(self):
        for i in range(len(self.cards)-1, 0, -1):
            r = random.randint(0,i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def draw(self):
        card = self.cards.pop()
        return card.show()

f = open('cards.json')
x = json.load(f)
t1 = "Major"
test = x[t1][0]['name']
print(test)

        