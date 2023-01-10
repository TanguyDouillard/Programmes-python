

#ESSAYER DE FAIRE AVEC DE NOUVELLES IMAGES !

from PIL import Image

image_Ronaldo = Image.open("Ronaldo.jpg")

image_Messi = Image.open("Messi.jpg")

def morphing(image_Messi,image_Ronaldo,etapes):

    #taille des images

    largeurMessi, hauteurMessi = image_Messi.size
    largeurRonaldo, hauteurRonaldo = image_Ronaldo.size
    print (largeurMessi, hauteurMessi)
    print (largeurRonaldo, hauteurRonaldo)


    #modification des tailles
    facteurlargeur = largeurRonaldo/largeurMessi
    facteurhauteur = hauteurRonaldo/hauteurMessi

    largeur_Messi = int(largeurMessi*facteurlargeur)+2
    hauteur_Messi = int(hauteurMessi*facteurhauteur)
    image_Messi = image_Messi.resize((largeur_Messi, hauteur_Messi), Image.ANTIALIAS)

    #image_Messi.show()
    #image_Ronaldo.show()
    #print(largeur_Messi)

    # Les deux images sont de la même taille

    image_new = Image.new("RGB", (400*etapes, 1000))

    #On prend les piexels de l'image Ronaldo
    for n in range(1,etapes+1):
        for x in range(largeur_Messi) :
            for y in range(hauteur_Messi) :
                pronaldo = image_Ronaldo.getpixel((x, y))
                pmessi = image_Messi.getpixel((x, y))

                pr = pronaldo[0]+int(n/etapes*(pmessi[0]-pronaldo[0]))
                pv = pronaldo[1]+int(n/etapes*(pmessi[1]-pronaldo[1]))
                pb = pronaldo[2]+int(n/etapes*(pmessi[2]-pronaldo[2]))
                image_new.putpixel((x+40*(n-1),y),(pr,pv,pb))
    image_new.show()










