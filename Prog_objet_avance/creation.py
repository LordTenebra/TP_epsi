# -*- coding: utf-8 -*-
#!/usr/bin/python

def structure(long, larg):
    colonne = []
    for i in range(long):
        ligne = largeur(larg);
        colonne += ligne
    return colonne

def largeur(larg):
    ligne = [];
    for i in range(larg):
        ligne += "a";
    return ligne
