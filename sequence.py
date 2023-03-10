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
        # Retourne True si la carte peut ??tre ajout??e ?? la fondation
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
        #Tente de bouger la derni??re carte de la colonne vers une destination donn??e.
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
    # Cr??ation d'un paquet de cartes et m??lange
    deck = Deck(mask=True)
    deck.shuffle()

    # Cr??ation d'une pile de cartes
    pile = Pile_Sequence()
    for i in range(9):
        pile.append(deck.deal())

    # Affichage de la pile
    print(pile)

    #foundation = Foundation_Sequence()


#
# pile_sequence : est la pile de carte ou on tire carte par carte, et la carte affich?? face visible est cele qui sera disponible
#                 les autres seront remplacer par " X ",  et non disponible pour des mouvements

# tableau_sequence : est le tableau de carte distribu??, 7 colonnes de 0 ?? 6, 

# foundation_sequence : sont les 4 emplacements libres pour y mettre les AS donc les 4 paquets complets. donc 2 3 4 5 de la m??me famille
                        #on ne d??placera pas les cartes de la foundation_sequence vers le tableau_sequence

#Pile_sequence
#Cette classe repr??sente une pile de cartes et 
# fournit des m??thodes pour ajouter, enlever et 
# d??placer des cartes entre les piles.



#Foundation_sequence
#Cette classe repr??sente une s??quence de cartes de m??me couleur et de rang croissant. 
# Elle fournit des m??thodes pour ajouter, enlever et d??placer des cartes 
# entre les s??quences.



#Tableau_sequence
#Cette classe repr??sente une s??quence de cartes avec des cartes alternant les couleurs et les rangs d??croissants. 
# Elle fournit des m??thodes pour ajouter, enlever et d??placer des cartes entre les s??quences.
# la derni??re ou toute la liste visible ( vers foundation une par une, et )



# append : ajoute un ??l??ment ?? la fin
# extend recoit une liste de carte
# on doit aussi impl??menter pour d??placer une liste du tableau vers ou la foundation_sequence, ou vers d'autre ??l??ments du tableau_sequence

# top cart sert ?? afficher la carte du sommet de la pile  ( toujours la m??me )
# pop affiche ?? chaque fois une carte diff??rente 
# si top_cart ne revoit rien c'est que la place est libre, ou alors on ajoute une m??thode " is_empty "


# 