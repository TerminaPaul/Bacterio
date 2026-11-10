import pygame
from deck import Deck


class Joueur:
    """Le joueur : un nom, des points de vie, un deck."""
    def __init__(self, x, y, indice):
        """Construit le joueur.

        Entrées : indice - un entier (soit 1, soit 2)
        Sortie  : aucune, deux attributs sont créés : barre_de_vie, deck
        Précondition : aucune
        """
        self.image = pygame.image.load(f"Assets/joueur_{indice}.png")
        self.rect = self.image.get_rect(x=x, y=y)
        self.barre_de_vie = 200
        self.deck = Deck(indice)

    def dessiner(self, ecran):
        ecran.blit(self.image, self.rect)
