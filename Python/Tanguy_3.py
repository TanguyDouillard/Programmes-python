# -*- coding: utf-8 *-*
# Chiffre de César, décalage de 3 rangs.
# Code ASCII de A = 65 à Z 90 et  a = 97 à z = 122

# Ouvrir un fichier
fichier = open('Texte_3.txt','r',encoding='utf8')
texte=fichier.read()

# Ecrire le texte chiffré avec un décalage de 3 rangs.
print("Texte clair : ")
print(texte)
print("")
print("Texte chiffré: ")

lettres = []

#x=max
#z=minimum
#j=compteur
#f=décalage
##### A Modifier #####
for y in range(97,123):
    j=0

    for i in range(len(texte)):
        lettre = texte[i]
        code = ord(lettre)

        if code == y:
            j=j+1
            lettres.append(j)

x=max(lettres)
z=lettres.index(x)

l=texte[0:x]
b=0
for a in range(l):
    if a == 1:
        b=b+1

print(lettres,end="")
print(x)
print(z)
print(p)

f=x-101

print(f,"= le décalage")



fichier.close()



