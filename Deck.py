import random
from Cartes import Card, Ranks, Suits

################
# CLASS : Deck #
################
class Deck:
    # Method : __init__
    # Type : Constructeur
    # Input : self
    # Return : None
    def __init__(self,mask=False):
        self.cards = []
        for suit in Suits:
            for rank in Ranks:
                self.cards.append(Card(suit, rank))

    # Method : shuffle
    # Type : Instance method
    # Input : self
    # Return : None
    def shuffle(self):
        random.shuffle(self.cards)

    # Method : is_empty
    # Type : Instance method
    # Input : self
    # Return : bool
    def is_empty(self) -> bool:
        return len(self.cards) == 0
    
    # Method : deal
    # Type : Instance method
    # Input : self
    # Return : Card
    # permet de prendre la carte du haut de la pile, la supprime de la pile de cartes et la renvoie en tant que résultat.
    def deal(self) -> Card:
        if self.is_empty():
            raise Exception("No more cards in the deck") # gestion de l'erreur de fin de paquet
        return self.cards.pop()
    
    # Method : deal_cards
    # Type : Instance method
    # Input : self
    # Return : None
    # affiche les 52 cartes de la pile de cartes sur quatre colonnes de 13 cartes chacune.
    def deal_cards(self):
        # Affichage des cartes avant le shuffle
        print("Avant le shuffle:")
        for i in range(0, 52, 4):
            print(f"{self.cards[i]}\t\t{self.cards[i+1]}\t\t{self.cards[i+2]}\t\t{self.cards[i+3]}\t") # 0 4 8 12 ...
        
        # Shuffle des cartes
        self.shuffle()
        
        # Affichage des cartes après le shuffle
        print("\nAprès le shuffle:")
        for i in range(0, 52, 4):
            print(f"{self.cards[i]}\t\t{self.cards[i+1]}\t\t{self.cards[i+2]}\t\t{self.cards[i+3]}\t")
    
if __name__ == '__main__':

    """
    deck = Deck()
    deck.shuffle()
    print("Mon Deck :")
    for i in range(13):
        print(f"{deck.deal()}\t\t{deck.deal()}\t\t{deck.deal()}\t\t{deck.deal()}\t")

    """

    while True:
        deck = Deck()
        deck.deal_cards()
        restart = input("\nVoulez-vous recommencer? (Oui/Non) ")
        if restart.lower() != 'oui':
            break



# deal doit retourner un objet de type Card
# comment on précise le type de retour Oo ? 
"""
 def deal(self) -> Card: 
 
"""