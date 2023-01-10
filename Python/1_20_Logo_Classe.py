# -*- coding: utf-8 *-*
#-------------------------------------------------------------------------------
# Créer une image avec logo 1°5
# 0 = Noir   255 = Blanc
#-------------------------------------------------------------------------------
#
# Pour lire et écrire des images dans un fichier
from PIL import Image
#
# Création de l'image "mon_image"
# image.mode = RGB ou L pour echelle de gris
#
largeur = 1000
longueur = 500
mon_image = Image.new('L',(largeur,longueur),"grey")
#
# Ecriture du premier chiffre
#
for y in range(100,400):
    for x in range(280,320):
        pixel = mon_image.getpixel((x, y))
        print(pixel)
        pixel = 0
        mon_image.putpixel((x,y),pixel)
#
# Ecriture du second chiffre
#
for y in range(100,140):
    for x in range(600,800):
        pixel = 255
        mon_image.putpixel((x,y),pixel)
#
# Ecriture des points
#
for y in range(100,250):
    for x in range(600,640):
        pixel = mon_image.getpixel((x,y))
        print(pixel)
        pixel=255
        mon_image.putpixel((x,y),pixel)
#
# Ecriture des points
#
for y in range (230,270):
    for x in range (600,800):
        pixel = 255
        mon_image.putpixel((x,y),pixel)

for y in range (250,400):
    for x in range (760,800):
        pixel=255
        mon_image.putpixel((x,y),pixel)

for y in range (360,400):
    for x in range (600,800):
        pixel=255
        mon_image.putpixel((x,y),pixel)

for y in range (100,140):
    for x in range (360,400):
        pixel=0
        mon_image.putpixel((x,y),pixel)

for y in range (360,400):
    for x in range (840,880):
        pixel=255
        mon_image.putpixel((x,y),pixel)

for x in range(180,280):
    for y in range(380-x,430+--x):
            pixel=0
            mon_image.putpixel((x,y),pixel)
# Affichage de l'image
#
mon_image.save('sortie.png')
mon_image.show()