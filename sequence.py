from abc import ABC, abstractmethod
from Cartes import Card, Ranks, Suits
from Deck import Deck

####################
# CLASS : Sequence #
####################
class Sequence(ABC):
    def __init__(self):
        self.sequence = []

    # Méthode pour retourner la carte du dessus de la séquence
    def top_card(self):
        if self.is_empty():
            return None
        return self.sequence[-1]

    # Méthode pour retirer la carte du dessus de la séquence
    def pop(self):
        return self.sequence.pop()

    # Méthode abstraite pour déplacer une carte vers une autre séquence
    @abstractmethod
    def move(self, destination):
        pass

    # Méthode abstraite pour vérifier si le déplacement d'une carte vers une autre séquence est valide
    @abstractmethod
    def is_valid_move(self, destination):
        pass

    # Méthode pour ajouter une carte à la séquence
    @abstractmethod
    def append(self, card):
        pass

    # Méthode pour vérifier si la séquence est vide
    def is_empty(self):
        return not bool(self.sequence)

#########################
# CLASS : Pile_Sequence #
#########################
class Pile_Sequence(Sequence):
    def move(self, destination):
        # On ne peut déplacer une carte de la pile que vers une séquence tableau
        if isinstance(destination, Tableau_Sequence):
            destination.append(self.pop())

    def is_valid_move(self, destination):
        # On peut déplacer une carte de la pile vers une séquence tableau si la dernière carte de la séquence tableau est de la même couleur et de rang inférieur à la carte de la pile
        if isinstance(destination, Tableau_Sequence):
            if destination.is_empty():
                return self.top_card().rank == Ranks.KING
            else:
                return destination.top_card().is_opposite_color(self.top_card()) and destination.top_card().rank == self.top_card().rank + 1
        return False

    def append(self, card):
        self.sequence.append(card)

    # Redéfinition de la méthode top_card pour renvoyer "None" si la pile est vide
    def top_card(self):
        if self.is_empty():
            return None
        return self.sequence[-1]

###############################
# CLASS : Foundation_Sequence #
###############################
class Foundation_Sequence(Sequence):
    def move(self, destination):
        # On ne peut pas déplacer de carte depuis la séquence foundation
        pass

    def is_valid_move(self, destination):
        # On ne peut pas déplacer de carte vers la séquence foundation depuis une autre séquence
        return False

    def append(self, card):
        # On ne peut ajouter une carte à la séquence foundation que si elle est un AS de la même famille que la séquence
        if card.rank == Ranks.ACE:
            self.sequence.append(card)

    # Redéfinition de la méthode top_card pour renvoyer "None" si la séquence foundation est vide
    def top_card(self):
        if self.is_empty():
            return None
        return self.sequence[-1]

    # Redéfinition de la méthode pop pour empêcher la suppression d'une carte dans la séquence foundation
    def pop(self):
        return None

    def is_empty(self):
        return not bool(self.sequence)

    def __str__(self):
        if self.is_empty():
            return "[]"
        return f"[{self.top_card()}]"

class Tableau_Sequence(Sequence):
    def move(self, destination):
        pass

    def is_valid_move(self, destination):
        return False

    def append(self, card):
        self.sequence.append(card)

    def top_card(self):
        if self.is_empty():
            return None
        return self.sequence[-1]

    def pop(self):
        return self.sequence.pop()

    def is_empty(self):
        return not bool(self.sequence)

    def extend(self, card):
        self.sequence.extend(card)

    def __str__(self):
        if self.is_empty():
            return "[]"
        s = ""
        for card in self.sequence:
            s += str(card) + ", "
        return "[" + s[:-2] + "]"

if __name__ == '__main__':
    deck = Deck(mask=False)
    deck.shuffle()
    pile = Pile_Sequence()
    for _ in range(10):
        c = deck.deal()
        pile.append(c)
    print('pile:', pile)
    foundation = Foundation_Sequence()
    valid = pile.is_valid_move(foundation)
    print('move -> foundation ? ' , valid)
    if valid:
        card = pile.pop()
        foundation.append(card)
        print('pile:', pile)
        print('foundation:', foundation)



"""
# pile_sequence : est la pile de carte ou on tire carte par carte, et la carte affiché face visible est cele qui sera disponible
#                 les autres seront remplacer par " X ",  et non disponible pour des mouvements

# tableau_sequence : est le tableau de carte distribué, 7 colonnes de 0 à 6, 

# foundation_sequence : sont les 4 emplacements libres pour y mettre les AS donc les 4 paquets complets. donc 2 3 4 5 de la même famille
                        on ne déplacera pas les cartes de la foundation_sequence vers le tableau_sequence
"""



# append : ajoute un élément à la fin
# extend recoit une liste de carte
# on doit aussi implémenter pour déplacer une liste du tableau vers ou la foundation_sequence, ou vers d'autre éléments du tableau_sequence

# top cart sert à afficher la carte du sommet de la pile  ( toujours la même )
# pop affiche à chaque fois une carte différente 
# si top_cart ne revoit rien c'est que la place est libre, ou alors on ajoute une méthode " is_empty "
