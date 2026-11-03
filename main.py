import pygame
from joueur import Joueur
from deck import Deck
import constantes


class Jeu:
    def __init__(self, screen):
        self.screen = screen
        self.running = True
        self.clock = pygame.time.Clock()
        self.joueur_1 = Joueur(0, 0, 1)
        self.joueur_2 = Joueur(650, 0, 2)

    def gestion_des_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def actualisation(self):
        pass

    def affichage(self):
        self.screen.fill("White")
        self.joueur_1.dessiner(self.screen)
        self.joueur_2.dessiner(self.screen)
        self.joueur_1.deck.dessiner(self.screen)
        self.joueur_2.deck.dessiner(self.screen)
        pygame.display.flip()

    def run(self):
        while self.running:
            self.gestion_des_events()
            self.actualisation()
            self.affichage()
            self.clock.tick(60)


if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption("Jeu")
    ratio = constantes.RATIOS[1]
    longueur = ratio[0] * constantes.REFERENCE_PX
    hauteur = ratio[1] * constantes.REFERENCE_PX
    ecran = pygame.display.set_mode((longueur, hauteur))
    jeu = Jeu(ecran)
    jeu.run()
    pygame.quit()