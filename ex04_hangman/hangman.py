import random
import words


#On choisit un mot au hasard dans le tableau tab
def string_random(tab):
    return random.choice(tab)

#On stock ce mot dans la variable "string_rand"
string_rand = string_random(tab)

#On créer notre compteur pour chaque coup de l'utilisateur
compteur = 20

#On demande à l'utilisateur de rentrer une lettre
letter = input("Entrée une lettre :")

#if len(letter)<= 1:
#    if letter 
