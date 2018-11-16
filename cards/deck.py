from card import Card
class Deck:
    def __init__(self):
        self._cards = []
        self.populate()
        print(self._cards)
        
    def populate(self):
        suits = ["hearts","clubs","diamonds","spades"]
        numbers = [str(n) for n in range(2,11)] + ["J", "D", "K", "A"]
        cards = []
        for suit in suits: 
            for number in numbers:
                #create a new Card obejct and add it to the list
                cards.append(Card(suit,number))
        self._cards = cards   
        
my_deck = Deck()        
print(my_deck)