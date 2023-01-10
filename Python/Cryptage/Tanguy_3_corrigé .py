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

#lettres = []
lettres = 26 * [0]
alphabet = 'abcdefghijklmnopqrstuvwxyz'
#x=max
#z=minimum
#j=compteur
#f=décalage
##### A Modifier #####
##for y in range(97,123):
##    j=0
for k in range(26) :
    for i in range(len(texte)):
        lettre = texte[i]
    #    code = ord(lettre)

    #    if code == y:
        if lettre == alphabet[k] :
    #        j=j+1
    #        lettres.append(j)
            lettres[k] = lettres[k] + 1

x=max(lettres)
z=lettres.index(x)
# Tu as trouvé le décalage, il ne reste plus quà reprendre l'algoritthme de l'exercice 2

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



