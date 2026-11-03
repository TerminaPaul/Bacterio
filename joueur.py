import pygame
from deck import Deck


class Joueur:
    def __init__(self, x, y, indice):
        self.image = pygame.image.load(f"Assets/joueur_{indice}.png")
        self.rect = self.image.get_rect(x=x, y=y)
        self.barre_de_vie = 200
        self.deck = Deck(indice)

    def dessiner(self, ecran):
        ecran.blit(self.image, self.rect)
