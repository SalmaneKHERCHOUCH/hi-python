import json
import csv

#On ouvre notre fichier json
with open('eleve.json') as eleve:
    data = json.load(eleve)

#On stock les données json dans eleves
eleves = data['eleve']

#On stock notre fichier csv pour l'ecriture dans eleve_csv
eleve_csv = open('eleve.csv', 'w')


csv_writer = csv.writer(eleve_csv)

count = 0
 
for el in eleves:
    if count == 0:
        #on selectionne les "cles" du json dans "eleve"
        titre = el.keys()
        #puis on ecrit une ligne pour les titres
        csv_writer.writerow(titre)
        count += 1
    #ensuite on écrit une autre ligne pour leur valeur    
    csv_writer.writerow(el.values())
 
eleve_csv.close()