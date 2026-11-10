import pygame
import constantes


class Deck:
    """Le deck : une liste."""
    def __init__(self, indice):
        """Construit le jeu.

        Entrées : indice — un entier (soit 1 soit 2)
        Sortie  : aucune, un attribut sont créé : deck, une liste de cinq cartes
                  vide au départ
        Précondition : aucune
        """
        self.deck = []
        self.image = pygame.image.load(f"Assets/deck_{indice}.png")
        self.rect = self.image.get_rect(
            x=constantes.POSITIONS_DECKS[indice][0], y=constantes.POSITIONS_DECKS[indice][1])

    def ajouter_carte(self, carte):
        """Ajoute une carte au deck.

        Entrées : carte — un objet Carte
        Sortie  : aucune, l'attribut deck est modifié
        Précondition : aucune
        """
        self.deck.append(carte)

    def remplir_deck(self, cartes):
        """Remplit le deck (ajoute 5 cartes).

        Entrées : cartes — une liste de cinq objets Carte
        Sortie  : aucune, l'attribut deck est modifié
        Précondition : cartes est une liste
                       cartes contient exactement le nombre de cartes maximum dans deck
        On utilise cette méthode uniquement au lancement du jeu.
        """
        assert isinstance(cartes, list), "pas une liste"
        assert len(cartes) == constantes.TAILLE_DECK, "nombre de cartes incorrect"
        for carte in cartes:
            self.ajouter_carte(carte)

    def trouver_carte(self, carte):
        """Retrouve une carte dans le deck.

        Entrées : carte — un objet Carte
        Sortie  : l'indice de la carte recherchée dans le deck
        Précondition : aucune
        """
        return self.deck.index(carte)

    def jouer_carte(self, carte):
        """Retire la carte du deck.

        Entrées : carte — un objet Carte
        Sortie  : aucune, l'attribut deck est modifié
        Précondition : aucune
        """
        return self.deck.pop(self.trouver_carte(carte))

    def dessiner(self, ecran):
        ecran.blit(self.image, self.rect)
