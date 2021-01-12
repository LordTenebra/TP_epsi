# -*- coding: utf-8 -*-
#!/usr/bin/python
import creation

class Labyrinthe:

    def __init__(self, longueur, largeur, hp):
        self.longueur = longueur
        self.largeur = largeur
        self.hp = hp


Laby = Labyrinthe(3,3,3)

def launch(Laby):
    structure = creation.structure(Laby.longueur, Laby.largeur)
    print(structure[5])

launch(Laby)
