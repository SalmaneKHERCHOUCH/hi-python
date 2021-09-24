import random

bot = ["pierre","papier","ciseau"]

#On choisit notre paire au hasard dans le tableau pour le bot
def Rps_random(bot):
    return random.choice(bot)

#On stock cette paire dans la variable "bot_rand"
bot_rand = Rps_random(bot)

#Si on veut tricher
#print(bot_rand)

#On demande à l'utilisateur de rentrer sa paire
user_rand = input("Entrée votre paire entre 'pierre/papier/ciseau' : ")


if user_rand == "pierre" or "ciseau" or "papier":
    
    if user_rand == "pierre" and bot_rand == "ciseau" or user_rand == "ciseau" and bot_rand == "papier" or user_rand == "papier" and bot_rand == "pierre":
        print("Vous avez gagné")
    elif user_rand == "pierre" and bot_rand == "papier" or user_rand == "papier" and bot_rand == "ciseau" or user_rand == "ciseau" and bot_rand == "pierre":
        print("Vous avez perdu")
    elif user_rand == bot_rand:
        print("C'est une égalité")   
elif user_rand != "pierre" or "ciseau" or "papier":
    user_paire = input("La synthaxe de la paire rentrée est incorrect, réessaye :")
else :
    print("Erreur")