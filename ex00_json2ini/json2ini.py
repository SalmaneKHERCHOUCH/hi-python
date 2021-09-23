import os,json

#import os controler si le fichier existe ou pas

file = "eleve.json"
string = ""

#Permet de verifier si le fichier existe
if os.path.exists(file):

    #"r" signifie reading
    with open(file,"r") as file : 
        data = json.load(file) # as a dicto

    #keys() pour les documents json clé/valeur
    for section in data.keys():
        string += f"[ {section} ] \n" 
        sectionElement = data[section]
        for key in sectionElement.keys():
            string +=  key + " = " + sectionElement[key] + "\n"
        string += "\n"

    with open('eleve.ini', 'w') as file:
        file.write(string)
        print("Job done !")

else:
    print("File doesn't exist .. ")