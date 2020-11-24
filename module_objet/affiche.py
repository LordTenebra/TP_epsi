# -*- coding: utf-8 -*-
#!/usr/bin/python
import calc

def noreduc(prix_tot):
    print("Votre facture Hors taxes est de ", prix_tot, " euros")
    print("Votre facture TTC est de ", calc.ttc(prix_tot), " euros")

def reduc(prix_tot, remise, prix_remise, prix_ttc):
    print("Votre facture Hors taxes est de ", prix_tot, " euros")
    print("Votre remise de 5% est de ", remise, " euros")
    print ("Votre facture final HT est de " , prix_remise, "euros")
    print("Votre facture TTC est de ", prix_ttc, " euros")
