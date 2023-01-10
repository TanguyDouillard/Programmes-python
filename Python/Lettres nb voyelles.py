#-------------------------------------------------------------------------------
# Name:        module2
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
lettre = True
texte=[texte]
j=(len(texte))

while lettre :
    x=x+1
    print(j)
    j=j+1

    if texte in voyelle:
        print ("voyelle a la",x,"place")
        lettre = False


