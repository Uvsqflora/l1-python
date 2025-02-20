###########################
# Auteur: Pierre Coucheney 
###########################

#######################
# import des librairies

import tkinter as tk
import random as rd


############################
# Définition des constantes

# hauteur du canevas
HAUTEUR = 600
# largeur du canevas
LARGEUR = 600
# taille de la grille
N = 4

# choix des couleurs
COUL_MUR = "grey"
COUL_VIDE = "white"

# paramètres de l'automate
# probabilité d'avoir un mur à l'initialisation
P = 0.5


######################
# variables globales

terrain = []
grille = []

#######################
# fonctions

def init_terrain():
    """ Initilise le terrain de la manière suivante:
    * met à 0 la liste à 2D appelée terrain qui contient pour chaque case la 
    valeur 1 si il y a un mur, et 0 sinon
    * initialise la liste à 2D grille qui contient l'identifiant
    de chaque carré dessiné sur le canevas 
    """
    global grille, terrain
    for i in range(N):
        terrain.append([0]*N)
        grille.append([0]*N)

    for i in range(N):
        for j in range(N):
            if rd.uniform(0, 1) < P:
                terrain[i][j] = 1
                couleur = COUL_MUR
            else:
                couleur = COUL_VIDE
            largeur = LARGEUR // N
            hauteur = HAUTEUR // N
            x0, y0 = i * largeur, j * hauteur
            x1, y1 = (i + 1) * largeur, (j + 1) * hauteur
            canvas.create_rectangle((x0, y0), (x1, y1), fill=couleur)



#######################
# programme principal

# définition des widgets
racine = tk.Tk()
racine.title("Génération de terrain")
canvas = tk.Canvas(racine, width=LARGEUR, height=HAUTEUR, bg="blue")

# placement des widgets
canvas.grid(column=0, row=0)

init_terrain()

# boucle principale
racine.mainloop()