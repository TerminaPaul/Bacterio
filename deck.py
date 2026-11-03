import pygame
import constantes


class Deck:
    def __init__(self, indice):
        self.deck = []
        self.image = pygame.image.load(f"Assets/deck_{indice}.png")
        self.rect = self.image.get_rect(
            x=constantes.POSITIONS_DECKS[indice][0], y=constantes.POSITIONS_DECKS[indice][1])

    def ajouter_carte(self, carte):
        self.deck.append(carte)

    def remplir_deck(self, cartes):
        assert isinstance(cartes, list), "pas une liste"
        assert len(cartes) == constantes.TAILLE_DECK, "nombre de cartes incorrect"
        for carte in cartes:
            self.ajouter_carte(carte)

    def trouver_carte(self, carte):
        return self.deck.index(carte)

    def jouer_carte(self, carte):
        return self.deck.pop(self.trouver_carte(carte))

    def dessiner(self, ecran):
        ecran.blit(self.image, self.rect)
