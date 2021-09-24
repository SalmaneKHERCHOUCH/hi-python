import random
import words

words = open('words.py').read().strip().split('", "')
word = random.choice(words)
print(word)


#On créer notre compteur pour chaque coup de l'utilisateur
compteur = 20

#On demande à l'utilisateur de rentrer une lettre

while compteur != 0 :
    for i in word :
        letter = input('Entrer une lettre :')
        if len(letter)<= 1:
            print("Vous avez mis 2 lettres tricheur !")
            if i == letter :
                print("Cette lettre appartient au mot",i) 
            elif i != letter : #si la lettre n'est pas dans le mot
                print("_") #les lettres manquantes
                print("Cette lettre n'appartient pas au mot")
                compteur-=1
                print("Il vous reste " + str(compteur) + " coup")

            if i == word : #s'il devine le mot
                print(word)
                print("Vous avez gagnée") 

            if compteur == 0 :
                print("Vous avez perdu")
