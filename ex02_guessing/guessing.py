from math import e
import random

tab = [1,2,3,4,5,6,7,8,9,10]

#On choisit un chiffre au hasard dans le tableau
def Number_random(tab):
    return random.choice(tab)

#On stock ce chiffre dans la variable "number_rand"
number_rand = Number_random(tab)

#On demande à l'utilisateur de rentrer un nombre et on le converti en un int
string_user = input("Entrée une valeur entre 1 et 10 pour trouver le nombre : ")
number_user = int(string_user)

while number_user != number_rand:
    #Si le nombre rentrer est différent du nombre aléatoire
    if number_user != number_rand :
        #On donne comme indice qu'il est plus grand et qu'il rentre un nouveau nombre
        if number_user < number_rand:
            number_user = int(input("La valeur est plus grande, réessayer : "))
        #On donne comme indice qu'il est plus petit et qu'il rentre un nouveau nombre
        elif number_user > number_rand:
            number_user = int(input("La valeur est plus petite, réesayer : "))
        #On vérifie que l'utilisateur à bien rentrer un nombre compris entre 1 et 10
        elif number_user < 1 and number_user > 10:
            number_user = int(input("La valeur rentrée n'est pas comprise entre 1 et 10 : "))
    #Si le nombre n'est pas un chiffre ou si il y a un probleme
    else :
        print("Erreur")
#Si le nombre que l'utilisateur rentre est égale au nombre alétoire c'est gagné
if number_user == number_rand :
    print("Bravo vous avez trouver la bonne réponse")