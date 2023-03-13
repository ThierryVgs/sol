from enum import Enum
import random
import colorama

colorama.init()
#########
# ENUM  #
#########
#################
# CLASS : Suits #
#################
class Suits(Enum):
    Hearts = 1
    Diamonds = 2
    Spades = 3
    Clubs = 4
    
#################
# CLASS : Ranks #
#################
class Ranks(Enum):
    A = 1
    Two = 2
    Three = 3
    Four = 4
    Five = 5
    Six = 6
    Seven = 7
    Eight = 8
    Nine = 9
    Ten = 10
    J = 11
    Q = 12
    K = 13

################
# CLASS : Card #
################
class Card:
    # Method : __init__
    # Type : Constructeur
    # Input : self, suit, rank, mask=False
    # Returns : None
    def __init__(self, suit, rank, mask=True): 
        self.suit = suit
        self.rank = rank
        self.mask = mask

    # Method : same_color
    # Type : Instance Method
    # Input : self, card
    # Returns : bool
    # si elles sont de couleurs différentes, la méthode retourne False.
    def same_color(self, card):
        return (self.suit in [Suits.Hearts, Suits.Diamonds] and
                card.suit in [Suits.Hearts, Suits.Diamonds]) or \
               (self.suit in [Suits.Spades, Suits.Clubs] and
                card.suit in [Suits.Spades, Suits.Clubs])

    # Method : rankDiffrence
    # Type : Instance Method
    # Input : self, card
    # Returns : bool
    def rankDiffrence(self, card):
        return self.rank == card.rank
    
    # Method : show
    # Type : Instance Method
    # Input : self
    # Returns : None
    def show(self):
        print(self.__str__())

    # Methode : __str__ 
    # Type : Instantiation Method
    # Input : self
    # return : str
    def __str__(self):
        if self.mask:    # Si la carte est masquée
            return "X, "
        if self.rank.value == 1:        # vérifie si la valeur de la carte est égale à 1, ce qui correspond à l'As.
            rank_str = 'A'
        elif self.rank.value <= 10:     # vérifie si la valeur de la carte est comprise entre 2 et 10 inclus.
            rank_str = str(self.rank.value)
        elif self.rank.value == 11:     # vérifie si la valeur de la carte est égale à 11, ce qui correspond au 'J'
            rank_str = 'J'
        elif self.rank.value == 12:     # vérifie si la valeur de la carte est égale à 11, ce qui correspond au 'Q'
            rank_str = 'Q'
        elif self.rank.value == 13:     # vérifie si la valeur de la carte est égale à 11, ce qui correspond au 'KJ'
            rank_str = 'K'

        suit_str = self.suit.name       # on prend le nom de la couleur 
        if self.suit in [Suits.Hearts, Suits.Diamonds]: # on vérifie si c'est rouge ( si oui bam ! rouge ( merci colorama ))
            return f"{colorama.Fore.RED}{rank_str} of {suit_str}{colorama.Style.RESET_ALL}"
        else:
            return f"{rank_str} of {suit_str}"  # si non, ben valeur par défaut (noir)

if __name__ == '__main__':
    card1 = Card(Suits.Hearts, Ranks.A, True)
    card2 = Card(Suits.Diamonds, Ranks.K, False)
    card3 = Card(Suits.Spades, Ranks.Q, True)
    card4 = Card(Suits.Clubs, Ranks.Five, False)

    cards = [card1, card2, card3, card4]

    # Afficher toutes les cartes
    print("Toutes les Cartes :")
    for card in cards:
        print(card)

    # Afficher toutes les cartes rouges
    print("\nCartes Rouges :")
    for card in cards:
        if card.suit in [Suits.Hearts, Suits.Diamonds]:
            print(card)

    # Vérifier si une carte est de la même couleur qu'une autre
    print(f"\n{card1} - {card2} same color : {card1.same_color(card2)}")
    print(f"{card1} - {card3} same color : {card1.same_color(card3)}")

    # Vérifier si une carte a le même rang qu'une autre
    print(f"\n{card1} - {card2} same rank : {card1.rankDiffrence(card2)}")
    print(f"{card1} - {card3} same rank : {card1.rankDiffrence(card3)}")

    # Afficher une carte
    two_of_spades = Card(Suits.Spades, Ranks.Two)
    as_of_hearts = Card(Suits.Hearts, Ranks.A)

    # Afficher la carte "two of spades"
    print(two_of_spades)

    # Afficher la carte "as of hearts"
    print(as_of_hearts)
    


    """  
    différence entre __repr__ et __str__ ? 
    apparemment la "lisibilité" de l'objet à la fin ... 
    recommandé d'implémenter les deux ...
    __str__ est appelé par " printf() ou str()
    __repr__ est appelé par "print() ou repr()

        def __str__(self):
            return f"{self.rank.name} of {self.suit.name}"

        def __repr__(self):
            return f"{self.rank.name} of {self.suit.name}" # rang de la carte + ' of ' + nom de la suite 

        c = Card(suit=Suits.Hearts, rank=Rank.A)
        print(c) #devrait afficher " A of Hearts "
        print(repr(c)) # devrait afficher "Card(suit=Hearts, Rank=A, mask=False)" si tout va bien :'( bordel

    # Methode : __repr__ 
    # Type : Instantiation Method
    # Input : self
    # return : str     
    def __repr__(self):
        if self.rank.value == 1:
            rank_str = 'A'
        elif self.rank.value <= 10:
            rank_str = str(self.rank.value)
        elif self.rank.value == 11:
            rank_str = 'J'
        elif self.rank.value == 12:
            rank_str = 'Q'
        elif self.rank.value == 13:
            rank_str = 'K'

        suit_str = self.suit.name
        if self.suit in [Suits.Hearts, Suits.Diamonds]:
            return f"{colorama.Fore.RED}{rank_str} of {suit_str}{colorama.Style.RESET_ALL}"
        else:
            return f"{rank_str} of {suit_str}" 
    """

    """
        def hide(self):
        #Cache la carte en la marquant comme cachée.
        self._is_hidden = True

    def expose(self):
        #Expose la carte en la marquant comme non cachée.
        self._is_hidden = False

    def is_hidden(self) -> bool:
        #Retourne si la carte est cachée ou non.
        return self._is_hidden
    """