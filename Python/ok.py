#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      tang.doui
#
# Created:     06/10/2021
# Copyright:   (c) tang.doui 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------

texte= input("texte?")
texte= str(texte)

voyelle = ["a","e","i","o","u","y"]

x=0


for lettre in texte:

    print (lettre)

    if lettre in voyelle:
        x=x+1
        print(" ",lettre,"est une voyelle")

print("il y a",x,"voyelles")
