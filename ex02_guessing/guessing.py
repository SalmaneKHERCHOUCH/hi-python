from math import e
import random

tab = [1,2,3,4,5,6,7,8,9,10]

def Number_random(tab):
    return random.choice(tab)

number_rand = Number_random(tab)

string_user = input("Entrée une valeur entre 1 et 10 pour trouver le nombre : ")
number_user = int(string_user)

while number_user != number_rand:

    if number_user != number_rand :
        if number_user < number_rand:
            number_user = int(input("La valeur est plus grande, réessayer : "))

        elif number_user > number_rand:
            number_user = int(input("La valeur est plus petite, réesayer : "))

        elif number_user < 1 and number_user > 10:
            number_user = int(input("La valeur rentrée n'est pas comprise entre 1 et 10 : "))
    
    else :
        print("Erreur")
if number_user == number_rand :
    print("Bravo vous avez trouver la bonne réponse")