# -*- coding: utf-8 *-*
# Chiffre de César, décalage de 3 rangs.
# Code ASCII de A = 65 à Z 90 et  a = 97 à z = 122

# Ouvrir un fichier
fichier = open('Texte_1.txt','r',encoding='utf8')
texte=fichier.read()

# Ecrire le texte chiffré avec un décalage de 3 rangs.
print("Texte clair : ")
print(texte)
print("")
print("Texte chiffré: ")

##### A Modifier #####
for i in range(19):
    lettre = texte[0+i]
    code = ord(lettre)
    if 65<=code<=90 or 97<=code<=122:
##        if 88<=code<=90 or 119<=code<=122:
        if 88<=code<=90 or 120<=code<=122:

            code = code -23
            lettre_new=chr(code)
            print (lettre_new,end="")
        else:
            code = code +3
            lettre_new=chr(code)
            print (lettre_new,end="")

    elif code == 32 or code == 44:
        lettre_new=chr(code)
        print (lettre_new,end="")



fichier.close()



