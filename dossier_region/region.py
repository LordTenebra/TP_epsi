import csv
import os
import shutil
cible = input("selectionner le fichier cible \n")
recup = ""
if cible != "":
    os.makedirs(cible, exist_ok=True)
    os.chdir(cible)
    recup = "../"
with open(recup + 'departements-france.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    count = 0
    region = []
    suppr = 0
    for row in spamreader:
        if count == 0:
            count = 1
        else:
            os.makedirs(row[3], exist_ok=True)
            for rec in region:
                if rec == row[3]:
                    suppr = 1
            if suppr == 0:
                vider = input("Voulez vous vider le dossier " + row[3] + " ? y / n \n")
                if vider == "y":
                    shutil.rmtree(row[3])
                    os.makedirs(row[3], exist_ok=True)
            region.append(row[3])
            suppr = 0
            os.chdir(row[3])
            os.makedirs(row[1], exist_ok=True)
            os.chdir('../')
