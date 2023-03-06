from abc import ABC, abstractmethod
from Cartes import Card, Ranks, Suits
from Deck import Deck

####################
# CLASS : Sequence #
####################

class Sequence(ABC):
    def __init__(self):
        self.sequence = []

    @abstractmethod
    def top_card(self):
        pass

    @abstractmethod
    def pop(self):
        pass

    @abstractmethod
    def move(self, destination):
        pass

    @abstractmethod
    def is_valid_move(self, destination):
        pass

    @abstractmethod
    def append(self, card):
        pass

#########################
# CLASS : PileSequence #
#########################

class Pile_Sequence(Sequence):
    def move(self, destination):
        destination.append(self.pop())

    def is_valid_move(self, destination):
        if not destination.is_empty():
            top_card = destination.top_card()
            return top_card.rank == Ranks.K and len(destination) == 1
        else:
            return self.top_card().rank == Ranks.K

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

    def __len__(self):
        return len(self.sequence)

    def __str__(self):
        if self.is_empty():
            return '[]'
        else:
            return str([str(c) for c in self.sequence[:-1]] + [str(self.top_card())])

###############################
# CLASS : FoundationSequence #
###############################

class Foundation_Sequence(Sequence):
    def __init__(self, suit):
        super().__init__()
        self.suit = suit

    def move(self, destination):
        destination.append(self.pop())

    def is_valid_move(self, destination):
        if self.is_empty():
            return False
        elif destination.is_empty():
            return self.top_card().rank == Ranks.A
        else:
            top_card = destination.top_card()
            return self.top_card().rank == top_card.rank + 1 and self.top_card().suit == top_card.suit

    def append(self, card):
        if card.rank == Ranks.A and card.suit == self.suit:
            self.sequence.append(card)
        elif not self.is_empty() and self.is_valid_move(TableauSequence(card.color)):
            self.sequence.append(card)
        else:
            raise ValueError(f"Cannot add card {card} to foundation sequence.")

    def top_card(self):
        if self.is_empty():
            return None
        return self.sequence[-1]

    def pop(self):
        return self.sequence.pop()

    def is_empty(self):
        return not bool(self.sequence)

    def __len__(self):
        return len(self.sequence)

    def __str__(self):
        if self.is_empty():
            return '[]'
        return f'[{self.top_card()}]'
    
class Tableau_Sequence(Sequence):
    def __init__(self):
        super().__init__()
        self.visible_cards = []  # cartes visibles dans la séquence
        self.hidden_cards = []  # cartes cachées dans la séquence

    def move(self, destination):
        # Vérifier si le mouvement est valide
        if not self.is_valid_move(destination):
            print("Ce mouvement n'est pas valide.")
            return

        # Retirer la carte du sommet de la pile visible
        card = self.visible_cards.pop()

        # Si la pile visible est vide et qu'il y a des cartes cachées,
        # la dernière carte cachée devient visible
        if not self.visible_cards and self.hidden_cards:
            self.visible_cards.append(self.hidden_cards.pop())

        # Ajouter la carte à la destination
        destination.append(card)

    def is_valid_move(self, destination):
        # Vérifier si la destination est une pile de fondation
        if isinstance(destination, Foundation_Sequence):
            return False

        # Vérifier si la destination est vide
        if destination.is_empty():
            return True

        # Récupérer la carte au sommet de la destination
        top_card = destination.top_card()

        # Vérifier si la couleur est opposée et le rang est inférieur de 1
        return (not card.color == top_card.color) and (card.rank == top_card.rank - 1)

    def append(self, card):
        # Ajouter la carte à la pile visible si elle est la première carte ajoutée
        if not self.visible_cards:
            self.visible_cards.append(card)
        else:
            # Ajouter la carte à la pile cachée
            self.hidden_cards.append(card)

    def top_card(self):
        # Retourner la carte du sommet de la pile visible
        if self.visible_cards:
            return self.visible_cards[-1]
        else:
            return None

    def pop(self):
        # Retirer la carte du sommet de la pile visible
        if self.visible_cards:
            return self.visible_cards.pop()
        else:
            return None

    def is_empty(self):
        # Vérifier si la pile visible et la pile cachée sont vides
        return not bool(self.visible_cards or self.hidden_cards)

    def extend(self, card):
        # Ajouter la carte à la pile visible
        self.visible_cards.append(card)

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
        tableau.top_card()
        print(tableau)

    # Foundation test
    foundation = Foundation_Sequence(suit='hearts')
    print(foundation.is_valid_move(Card(Ranks.A, Suits.Spades)))
    foundation.append(Card(Ranks.A, Suits.Spades))
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
