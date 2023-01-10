# -*- coding: utf-8 *-*
# Chiffre de César, décalage de 3 rangs.
# Code ASCII de A = 65 à Z 90 et  a = 97 à z = 122

# Ouvrir un fichier
fichier = open('Texte_2.txt','r',encoding='utf8')
texte=fichier.read()

# Ecrire le texte chiffré avec un décalage de 3 rangs.
print("Texte clair : ")
print(texte)
print("")
print("Texte chiffré: ")

##### A Modifier #####

n = input("Décalage?")
n=int(n)


#n=décalage

for i in range(len(texte)):
    lettre = texte[0+i]
    code = ord(lettre)

    if 65<=code<=90 or 97<=code<=122:
        if 65<=code<=(65+n-1) or 97<=code<=(97+n-1):

            code = code + 26 - n
            lettre_new=chr(code)
            print (lettre_new,end="")

        else:

            code = code - n
            lettre_new=chr(code)
            print (lettre_new,end="")

    else:
        lettre_new=chr(code)
        print (lettre_new,end="")



fichier.close()

