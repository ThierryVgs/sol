from abc import ABC, abstractmethod
from Cartes import Card, Ranks, Suits
from Deck import Deck

######################
# CLASS : Sequence    #
######################
class Sequence(ABC):
    def __init__(self) -> Card:
        self.sequence = []

    def pop(self) -> Card:
        return self.sequence.pop() if not self.is_empty() else None

    def top_card(self) -> Card:
        return self.sequence[-1] if not self.is_empty() else None

    @abstractmethod
    def move(self, destination):
        pass

    @abstractmethod
    def is_valid_move(self, destination):
        pass

    @abstractmethod
    def append(self, card):
        pass

    @abstractmethod
    def is_empty(self):
        pass

#########################
# CLASS : Pile_Sequence #
#########################
class Pile_Sequence(Sequence):
    def __str__(self):
        if self.is_empty():
            return "Pile: "
        stack_str = ''
        for i, card in enumerate(self.sequence):
            if i < len(self.sequence) - 1:
                stack_str += 'X, '
            else:
                stack_str += f'{card}' if not card.mask else 'X'
        return f"Pile: {stack_str}


    def move(self, destination) -> bool:
        if not self.is_valid_move(destination):
            return False

        last_card = self.sequence.pop()
        destination.append(last_card)
        return True

    def is_valid_move(self, destination) -> bool:
        dest_card = destination.top_card()
        src_card = self.top_card()
        if dest_card is None:
            return src_card.rank == Ranks.K
        if src_card is None or src_card.mask:
            return False
        return src_card.color() != dest_card.color() and src_card.rank == dest_card.rank - 1

    def append(self, card: Card):
        self.sequence.append(card)

    def is_empty(self) -> bool:
        return len(self.sequence) == 0

###############################
# CLASS : Foundation_Sequence #
###############################
class Foundation_Sequence(Sequence):
    def __init__(self, suit, ):
        super().__init__()
        self.suit = suit

    def __str__(self):
        if self.is_empty():
            return f"Foundation {self.foundation_number}: "
        return f"Foundation {self.foundation_number}: {self.top_card()}"

    def is_valid_move(self, card: Card) -> bool:
        # Retourne True si la carte peut être ajoutée à la fondation
        return (self.is_empty() and card.rank == Ranks.A and card.suit == self.suit) or \
               (not self.is_empty() and card.suit == self.suit and
                card.rank == self.sequence[-1].rank + 1)
    
    def move(self, destination) -> bool:
        return False 
    
    def append(self, card: Card):
        if not self.is_valid_move(card):
            raise ValueError("Invalid Move")
        self.sequence.append(card)

    def is_empty(self) -> bool:
        return len(self.sequence) == 0


############################
# CLASS : Tableau_Sequence #
############################
class Tableau_Sequence(Sequence):
    def __init__(self, num_columns: int, num_rows: int):
        super().__init__()
        self.num_columns = num_columns

    def move(self, destination: Sequence) -> bool:
        #Tente de bouger la dernière carte de la colonne vers une destination donnée.
        if not self.is_valid_move(destination):
            return False
        
    def append(self, card: Card):
        pass
    def extend(self, card: Card):
        pass
    
####################
# CLASS : __main__ #
####################
if __name__ == "__main__":
    # Création d'un paquet de cartes et mélange
    deck = Deck(mask=True)
    deck.shuffle()

    # Création d'une pile de cartes
    pile = Pile_Sequence()
    for i in range(9):
        pile.append(deck.deal())

    # Affichage de la pile
    print(pile)

    #foundation = Foundation_Sequence()


#
# pile_sequence : est la pile de carte ou on tire carte par carte, et la carte affiché face visible est cele qui sera disponible
#                 les autres seront remplacer par " X ",  et non disponible pour des mouvements

# tableau_sequence : est le tableau de carte distribué, 7 colonnes de 0 à 6, 

# foundation_sequence : sont les 4 emplacements libres pour y mettre les AS donc les 4 paquets complets. donc 2 3 4 5 de la même famille
                        #on ne déplacera pas les cartes de la foundation_sequence vers le tableau_sequence

#Pile_sequence
#Cette classe représente une pile de cartes et 
# fournit des méthodes pour ajouter, enlever et 
# déplacer des cartes entre les piles.



#Foundation_sequence
#Cette classe représente une séquence de cartes de même couleur et de rang croissant. 
# Elle fournit des méthodes pour ajouter, enlever et déplacer des cartes 
# entre les séquences.



#Tableau_sequence
#Cette classe représente une séquence de cartes avec des cartes alternant les couleurs et les rangs décroissants. 
# Elle fournit des méthodes pour ajouter, enlever et déplacer des cartes entre les séquences.
# la dernière ou toute la liste visible ( vers foundation une par une, et )



# append : ajoute un élément à la fin
# extend recoit une liste de carte
# on doit aussi implémenter pour déplacer une liste du tableau vers ou la foundation_sequence, ou vers d'autre éléments du tableau_sequence

# top cart sert à afficher la carte du sommet de la pile  ( toujours la même )
# pop affiche à chaque fois une carte différente 
# si top_cart ne revoit rien c'est que la place est libre, ou alors on ajoute une méthode " is_empty "


# 