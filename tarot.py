import random

class Card:
    def __init__(self,suit,val):
        self.suit = suit
        self.value = val
    
    def show(self):
        print("{} of {}".format(self.value,self.suit))

class Deck:
    def __init__(self):
        self.cards = []
        self.build()
    
    def build(self):
        for a in ["Cups","Pentacles","Swords","Wands","Major"]:
            if a=="Major":
                for b in range (1,23):
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
        return self.cards.pop()


