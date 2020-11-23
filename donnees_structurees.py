# -*- coding: utf-8 -*-
#!/usr/bin/python
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
                            prix_fin_HT = float(select['prix']) * quant
                            prix_tot += prix_fin_HT
                        else:
                            print("erreur : nombre inférieur à 1")
                    except ValueError:
                        print("veuillez entrer un entier")
            except ValueError:
                print("entrer un nombre entre 1 et 4")
        if prix_tot > 200:
            print("Votre facture Hors taxes est de ", prix_tot, " euros")
            print("Votre remise de 5% est de ", round((prix_tot * 5) / 100), " euros")
            prix_remise = round(prix_tot - (prix_tot * 5) / 100)
            print ("Votre facture final HT est de " , prix_remise, "euros")
            print("Votre facture TTC est de ", round(prix_remise + ((prix_remise * 20) / 100), 2), " euros")
        else :
            print("Votre facture Hors taxes est de ", prix_tot, " euros")
            print("Votre facture TTC est de ", round(prix_tot + ((prix_tot * 20) / 100), 2), " euros")
        break
    except ValueError:
        print("entrer un nombre")
