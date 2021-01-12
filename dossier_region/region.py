import csv
import os
with open('departements-france.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        #os.makedirs(row[0], exist_ok=True)
        print(row[0])
