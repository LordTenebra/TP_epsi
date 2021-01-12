# -*- coding: utf-8 -*-
#!/usr/bin/python
import calc
import affiche
import reduc

class Main:

    def select():
        produit = {
        1:{"nom":"banane", "prix":4},
        2:{"nom":"Pomme","prix":2},
        3:{"nom":"Orange", "prix":1.5},
        4:{"nom":"Poire","prix":3}
        }
        prix_tot = int(0)
        while True:
            try:
                nb_produit = int(input("Combiens de produit :"))
                for i in range(1, nb_produit+1) :
                    try:
                        ref = int(input("selectionner le produit : "))
                        if ref > 0 and ref < len(produit)+1:
                            select = produit[ref]
                            try:
                                quant = int(input("combiens en voulez vous : "))
                                if quant > 0:
                                    prix_tot += calc.prix(float(select['prix']), quant)
                                else:
                                    print("erreur : nombre inférieur à 1")
                            except ValueError:
                                print("veuillez entrer un entier")
                    except ValueError:
                            print("entrer un nombre entre 1 et 4")

                if prix_tot > 200:
                    reduc.prix(prix_tot)
                else:
                    affiche.noreduc(prix_tot)
                break
            except ValueError:
                print("entrer un nombre")

    select()
