from card import Card
from deck import Deck
import sequence

from sequence import Pile_Sequence, Foundation_Sequence, Tableau_Sequence

#####################
# CLASS Solitaire : #
#####################
class Solitaire:
    def __init__(self):
        self.deck = Deck()
        self.tableau = [Tableau_Sequence() for _ in range(7)]
        self.pile = Pile_Sequence()
        self.foundation = [Foundation_Sequence() for _ in range(4)]

    def play(self):
        while True:
            self.display()
            source = self.get_source()
            if source == 'd':
                if not self.deck.is_empty():
                    self.pile.add_card(self.deck.draw())
                else:
                    break
            elif source == 'p':
                if not self.pile.is_empty():
                    self.move(self.pile, self.get_destination())
                else:
                    break
            else:
                self.move(self.tableau[int(source)], self.get_destination())

    def display(self):
        print('Pile:', end=' ')
        print(self.pile)
        print('Tableau:')
        for i, t in enumerate(self.tableau):
            print(i, ':', t)
        print('Foundation:')
        for i, f in enumerate(self.foundation):
            print(i, ':', f)

    def get_source(self):
        while True:
            source = input('Enter the source pile (0-6 for tableau, p for pile or d for Draw) ').strip()
            if source in ['0', '1', '2', '3', '4', '5', '6', 'p', 'd']:
                return source
            print('Invalid source')

    def get_destination(self):
        while True:
            destination = input('Enter the destination pile (0-6 for tableau, 8-11 for foundation) ').strip()
            if destination in [str(i) for i in range(7)] + [str(i) for i in range(8, 12)]:
                return int(destination)
            print('Invalid destination')

    def move(self, source, destination):
            if destination in range(7):
                if self.tableau[destination].can_add_card(source.get_top_card()):
                    self.tableau[destination].add(source.pop())
                else:
                    print('Invalid move')
            else:
                destination -= 7
                if self.foundation[destination].can_add(source.get_top_card()):
                    self.foundation[destination].add(source.pop())
                else:
                    print('Invalid move')

-
    s = Solitaire()
    s.play()
    # Output:
    # Pile: X, X, 6 of spades
    # Tableau:
    # 0: K of hearts, Q of clubs
    # 1: K of clubs, Q of diamonds
    # 2: X, 7 of spades, 6 of hearts
    # 3: 
    # 4: X, X, X, X, 5 of hearts, 4 of clubs, 3 of diamonds
    # 5: X, X, X, X, X, 8 of clubs, 7 of hearts
    # 6: X, X, 9
