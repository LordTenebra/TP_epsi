# -*- coding: utf-8 -*-
#!/usr/bin/python
nb_produit = int(input("Combiens de produit :"))
for i in range(1, nb_produit+1) :
    prix_HT = int(input("Entrer le prix : "))
    prix_TTC = prix_HT + ((prix_HT * 20) / 100)
    if (prix_TTC >= 200) :
        prix_TTC = prix_TTC - ((prix_TTC * 5) / 100)
    print ("le produit", i, "a por valeur", prix_TTC)
