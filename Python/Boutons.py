#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      tang.doui
#
# Created:     10/11/2021
# Copyright:   (c) tang.doui 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from tkinter import*

fen=Tk()
fen.minsize(100,100)
fen.title("Moula presque gratuit ici")

texte=Label(fen, text="Appuye sur ce bouton après avoir écrit qqchose",font=(20))

def fonction():
    print("Hello", saisie.get())


bouton= Button(fen, text="Ce bouton",font=(20), command=fonction, bg="red")

nom=StringVar()

saisie = Entry(fen, textvariable=nom)

texte.pack(side=LEFT,padx=10,pady=10)
bouton.pack(side=RIGHT,padx=10,pady=10)
saisie.pack(side=BOTTOM)

fen.mainloop()