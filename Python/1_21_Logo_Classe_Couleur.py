# -*- coding: utf-8 *-*
#-------------------------------------------------------------------------------
# Créer une image avec logo 1°5 en couleur
#-------------------------------------------------------------------------------
#
# Pour lire et écrire des images dans un fichier
from PIL import Image
#
# Création de l'image mon_image
# image.mode = RGB  couleur
#            ou L pour echelle de gris
#
largeur = 1000
longueur = 500
mon_image = Image.new('RGB',(largeur,longueur),"red")
#
# Ecriture du premier chiffre
#
for y in range(100,140):
    for x in range(100,400):
        p_rouge = 0
        p_vert = 255
        p_bleu = 0
        mon_image.putpixel((x,y),(p_rouge,p_vert,p_bleu))
#
# Ecriture du second chiffre
#
for y in range(100,140):
    for x in range(600,800):
        p_rouge = 0
        p_vert = 0
        p_bleu = 255
        mon_image.putpixel((x,y),(p_rouge,p_vert,p_bleu))
#
# Ecriture des points
#
for y in range (100,400):
    for x in range(600,640):
        p_rouge = 0
        p_vert = 25
        p_bleu = 255
        mon_image.putpixel((x,y),(p_rouge,p_vert,p_bleu))

for y in range (360,400):
    for x in range(600,800):
        p_rouge=0
        p_vert=75
        p_bleu=255
        mon_image.putpixel((x,y),(p_rouge,p_vert,p_bleu))

for y in range (160,360):
    for x in range (760,800):
        p_rouge=0
        p_vert=125
        p_bleu=255
        mon_image.putpixel((x,y),(p_rouge,p_vert,p_bleu))


for y in range (160,200):
    for x in range(660,760):
        p_rouge=0
        p_vert=200
        p_bleu=255
        mon_image.putpixel((x,y),(p_rouge,p_vert,p_bleu))

for y in range (200,340):
    for x in range(660,700):
        p_rouge=0
        p_vert=255
        p_bleu=255
        mon_image.putpixel((x,y),(p_rouge,p_vert,p_bleu))

for y in range (320,340):
    for x in range (700,740):
        p_rouge=0
        p_vert=255
        p_bleu=200
        mon_image.putpixel((x,y),(p_rouge,p_vert,p_bleu))

for y in range (140,300):
    for x in range(100,140):
        p_rouge=255
        p_vert=0
        p_bleu=200
        mon_image.putpixel((x,y),(p_rouge,p_vert,p_bleu))

#
# Affichage de l'image
#
mon_image.save('sortie.png')
mon_image.show()