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
def move(self, destination):
        """Déplace la carte du dessus de la pile vers la destination"""
        if self.is_valid_move(destination):
            destination.append(self.pop())

    def is_valid_move(self, card):
        """Vérifie si le déplacement de la carte vers la fondation est valide"""
        if not self.sequence:
            return card.rank == Ranks.Ace
        top_card = self.top_card()
        if top_card.suit != card.suit:
            return False
        return top_card.rank.value + 1 == card.rank.value

    def append(self, card):
        """Ajoute une carte à la pile"""
        if self.is_valid_move(card):
            self.sequence.append(card)

    def top_card(self):
        """Retourne la carte du dessus de la pile"""
        if self.is_empty():
            return None
        return self.sequence[-1]

    def is_empty(self):
        """Vérifie si la pile est vide"""
        return not bool(self.sequence)

    def __str__(self):
        """Affiche la pile sous forme de chaîne de caractères"""
        return ", ".join(str(card) for card in self.sequence)

##############################
# CLASS : Tableau_Sequence #
##############################
class Tableau_Sequence(Sequence):
    def move(self, destination):
        """Déplace la carte du dessus de la pile vers la destination"""
        if self.is_valid_move(destination):
            destination.append(self.pop())

    def is_valid_move(self, destination):
        """Vérifie si le déplacement de la carte du dessus de la pile vers la destination est valide"""
        if not self.sequence:
            return False
        if isinstance(destination, Foundation_Sequence):
            return False
        top_card = self.top_card()
        if isinstance(destination, Tableau_Sequence):
            return destination.is_valid_move(top_card)
        elif isinstance(destination, Pile_Sequence):
            return not destination.is_empty() and destination.top_card().rank.value - 1 == top_card.rank.value and not top_card.same_color(destination.top_card())
        else:
            return False

    def append(self, card):
        """Ajoute une carte à la pile"""
        self.sequence.append(card)

    def top_card(self):
        """Retourne la carte du dessus de la pile"""
        if self.is_empty():
            return None
        return self.sequence[-1]

    def pop(self):
        """Retire la carte du dessus de la pile"""
        return self.sequence.pop()

    def is_empty(self):
        """Vérifie si la pile est vide"""
        return not bool(self.sequence)

    def __str__(self):
        """Affiche la pile sous forme de chaîne de caractères"""
        return ", ".join(str(card) for card in self.sequence)

##########
# TESTS #
##########
if __name__ == '__main__':
    deck = Deck(mask=False)
    deck.shuffle()

    # Tableau test
    tableau = Tableau_Sequence()
    for i in range(7):
        for j in range(i + 1):
            tableau.append(deck.deal())
        tableau.top_card().flip()
        print(tableau)

    # Foundation test
    foundation = Foundation_Sequence()
    print(foundation.is_valid_move(Card(Ranks.Ace, Suits.Spades)))
    foundation.append(Card(Ranks.Ace, Suits.Spades))
    print(foundation)
    print(foundation.is_valid_move(Card(Ranks.Two, Suits.Spades)))
    foundation.append(Card(Ranks.Two, Suits.Spades))


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
