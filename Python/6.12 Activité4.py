#6.12 : Activité 4

def Moyenne_Eleve(note):
    for eleve in note:
        print(eleve[0]," a un moyenne de ", eleve[1])

def Moyenne_Eleve_2(note):
    for i in range (len(note)):
        print(note[i][0]," a une moyenne de ", note [i][1])

def Oral(liste):
    nsi = []
    for eleve in liste:
        if eleve[1] == "NSI":
            nsi.append(eleve[0])
        else:
            pass
    return nsi



#6.11 : Activité 3

#Exercice 1

##l=[]
##for i in range(15):
##    nb = (i**2)
##    if nb%2==0:
##        l.append(nb)
##print(l)
##
##l2=[(i**2) for i in range(15) if i%2==0]

#Exercice 2

##l3=[]
##for i in range(180):
##    if i%5==0 and i%3==0:
##        l3.append(i)
##print(l3)
##
##l3=[i for i in range(180) if i%5==0 and i%3==0]

#Exercice 3

##liste=["Anna","Ben","Chloe","Ali"]
##la=[]
##l3=[]
##for i in range (len(liste)):
##    if liste[i][0]=="A":
##        la.append(liste[i])
##    if len(liste[i])==3:
##        l3.append(liste[i])
##print(liste, la, l3)
##
##la=[liste[i] for i in range (len(liste)) if liste[i][0]=="A"]
##l3=[liste[i] for i in range (len(liste)) if len(liste[i])==3]

#Exercice 4

##liste=[["Anna",18],["Ben",14],["Chloe",11],["Don",15]]
##bien = []
##for i in range(len(liste)):
##    if liste[i][1]>14:
##        bien.append(liste[i][0])
##print (bien)
##
##bien2=[liste[i][0] for i in range(len(liste)) if liste[i][1]>14]

#Exercice 5

##e2 = {i for i in range(24) if i%2==0}
##e3 = {i for i in range(24) if i%3==0}
##
#Exercice 6
##
##epair = {i for i in range(21) if i%2==0}
##e5 = {i for i in range(11) if i%5==0}

##dico = {"Pomme":"fruit","Kiwi":"fruit","Chou":"legume"}
##a=[]
##b=[]
##x=0
##for achat in dico.keys():
##    a.append(achat)
##for achat,type in dico.items():
##    if type == "fruit":
##        x=x+1
##        b.append(achat)
##print("Tu as acheté ", a," il y a", x," fruits qui sont", b )
##
##



def Note(dico):
    max=0
    a=[]
    for maximum in dico.values():
        if maximum>max:
            max=maximum
    for personne,maximum in dico.items():
        if maximum == max:
            a.append(personne)
    return a, max
















