# -*- coding: utf-8 *-*
#---------------------------------------------------------------------
# Décryptage image 400 * 300 pixels
#---------------------------------------------------------------------
from PIL import Image # Pour lire et écrire des images dans un fichier

def poids_faible(n):
    ecriture_binaire = [0 for i in range(0,8)] # Initialisation Ecriture binaire
    for i in range(8):
       ecriture_binaire[i] =  n%2
       n=n//2
# Renvoie les 4 bits de poids faible
    return ecriture_binaire[0:4]

longueur = 400
hauteur  = 300

l=[]

# Image à décrypter
img_ini = Image.open('Indice_3.png')

# Création d'une image vide
img_fin = Image.new('L',(longueur,hauteur),"grey")

# Boucle sur les pixels **** A compléter ***
for y in range(0,300):
    for x in range(0,400):
        pixel = img_ini.getpixel((x,y))
        l=poids_faible(pixel)
        pixel=l[0]*16+l[1]*32+l[2]*64+l[3]*128
        img_fin.putpixel((x,y),pixel)

#
img_fin.show()





