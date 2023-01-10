# -*- coding: utf-8 *-*
#-----------------------------------------------------
# Cours 2_24 : Calcul mental
#-----------------------------------------------------
#
# On importe la bibliothèque graphique Tkinter
from tkinter import *
from random import randrange

def Jouer():
    global nombre_1,nombre_2
    nombre_1 = randrange(1,10)  # Nombre aléatoire entre 3 et 10 non inclus
    nombre_2 = randrange(11,19)
    label_nb_1["text"] = "Nombre 1 : " + str(nombre_1)
    label_nb_2["text"] = "Nombre 2 : " + str(nombre_2)
    label_resultat["text"] = "Le Produit est : "


score=0
total=0

def Valider():
    global score,total

    label_score["text"] = "Score : "
    rep=var_resultat.get()
    if rep == nombre_1 * nombre_2:
        label_resultat["text"] = " Bravo "
        score=score+1
        total=total+1
        label_score["text"] = "Score : " + str(score) +"/"+ str(total)
    else :
        label_resultat["text"] = " Erreur, la bonne reponse était " + str(nombre_1 * nombre_2)
        total=total+1
        label_score["text"] = "Score : " + str(score) +"/"+ str(total)

#**********************************************
# Programme Principal
#**********************************************

# objet fenetre à partir de la classe Tk() fenetre principale
fenetre = Tk()
fenetre.title("Calcul Mental")

# Titre de la fenetre principale en jaune
label_fenetre = Label(fenetre,text="Ma fenetre graphique",fg='blue', bg="yellow",font="Arial 15 italic")
label_fenetre.pack()

# Champ Texte
label_nb_1 = Label(fenetre, text="Nombre 1 : ", font="Arial 15 italic")
label_nb_2 = Label(fenetre, text="Nombre 2 : ", font="Arial 15 italic")

label_nb_1.pack(padx = 5,pady=5) # Methode pack() --> positionne l'objet
label_nb_2.pack(padx = 5,pady=10)

# Bouton fenetre du haut
bouton_jouer = Button(fenetre,text = " Jouer ",bg='yellow',command = Jouer )
bouton_jouer.pack(padx=5,pady=10)

# Champ Affichage du résultat
label_resultat = Label(fenetre, text="Le Produit est : ",fg='white',bg="blue", font="Arial 15 italic")
label_resultat.pack(padx=5,pady=5)

# Champ affichage score
label_score = Label(fenetre, text="Ton score est : " , fg='black', bg="yellow", font="Arial 15 italic")
label_score.pack(side=BOTTOM,padx=10,pady=10)

# Zone de saisie
# On crée une variable Tkinter associée au champ de texte.
# var_resultat.get() pour récupérer la valeur
var_resultat = IntVar()
saisie_resultat = Entry(fenetre,textvariable = var_resultat , width =10)
saisie_resultat.pack(padx=5,pady=5)

#Boutons Valider et Quitter
bouton_valider = Button(fenetre,text = " Valider ",fg='white',bg='blue',command = Valider )
bouton_quitter = Button(fenetre,text = " Quitter ",bg='red' ,command = fenetre.destroy )

bouton_valider.pack(side=LEFT,padx=10,pady=10)
bouton_quitter.pack(side=RIGHT,padx=10,pady=10)

# Représentation géométrique interne mais pas visible
# Methode mainloop tourne en boucle
# gestionnaire d'événement + affichage fenetre
fenetre.mainloop()

