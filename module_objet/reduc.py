# -*- coding: utf-8 -*-
#!/usr/bin/python
import affiche

def prix(prix_tot):
    remise = round((prix_tot * 5) / 100)
    prix_remise = round(prix_tot - remise)
    prix_ttc = round(prix_remise + ((prix_remise * 20) / 100), 2)
    affiche.reduc(prix_tot,remise, prix_remise, prix_ttc)
