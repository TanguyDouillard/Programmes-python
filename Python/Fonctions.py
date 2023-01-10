import math

def cercle(r):
    aire= math.pi*r**2
    aire = round(aire,2)
    longueur = 2*math.pi*r
    longueur = round(longueur,2)

    return "L'aire est " +str(aire) + " et la longueur est " +str(longueur)


def nb_case(R):
    case = 1
    u = 1
    somme = u
    while somme <= R:
        u = u*2
        somme = somme + u
        case = case + 1
    return case

def degre(F):
    x=F-32
    x=x*(5/9)
    return x

def multiple(X,Y):
    if X%Y==0 or Y%X==0:
        return True
    return False

def operation(A,B):
    plus=A+B
    fois=A*B
    return "La somme est " + str(plus) + ", le produit est " + str(fois)


def carre(N):
    if N%math.sqrt(N)==0:return True
    return False

#mention = "Pas de mention"

#def Trimestre(note):
    #if note>=14:
        #return "Bon trimestre"
    #elif note>=10:
       # return "Trimestre correct"
    #else :
        #return "Attention"

#mention = Trimestre(17)
#print(mention)


#mention = "Pas de mention"

#def Trimestre2(note):
    #global mention
    #if note>=14:
        #mention = "Bon trimestre"
    #elif note>=10:
        #mention = "Trimestre correct"
    #else :
        #mention = "Attention"

#Trimestre2(17)
#print(mention)


#k=10
#def f():
    #global k
    #k=k+3

#print("k vaut",k)
#f()
#[print ("k vaut", k)
#f()
#print ("k vaut", k)



def moyenne(liste):
    s=0
    for elt in liste:
        s=s+elt
    return s/len(liste)

def trie(l):
    for i in range(len(l)-1):
        if l[i]>l[i+1]:
            return False
    return True


def inverse(l):
    liste=[]
    for i in range(len(l)-1,-1,-1):
        liste.append(l[i])
    return liste

def insere(l,valeur,position):
    liste=[]
    for i in l:
            liste.append(i)
            if i==position:
                liste.append(valeur)
    return liste

def extrema(l):
    max = l[0]
    min = l[0]
    for i in l:
        if i>max:
            max=i
        elif i<min:
            min=i
    return max, min


def position(l):
    z=1
    max = l[0]
    min = l[0]
    for i in l:
        if i>max:
            posmax = z
            max=i
        z=z+1
    return max, posmax


def cinq(phrase):
        for i in range (len(phrase)):
            if len(phrase[i]) == 5:
                 return i, phrase[i]


        #if len(elt) == 5:
           #return elt
    #return 'pas de mot de cinq lettres'


def voyelle(mot):
    voyelles = "aeiouy"
    rep = ""
    for elt in mot:
        if elt not in voyelles:
            rep = rep + elt
    return rep

def voyelle2(mot):
    voyelles = "aeiouy"
    voy = 0
    cons = 0
    for elt in mot:
        if elt in voyelles:
            voy = voy + 1
        else :
            cons = cons + 1
    return voy, cons

def scrabble(mot):
    l1 = "aeilnorstu"
    l2 = "dgm"
    l3 = "bcp"
    l4 = "fhv"
    l8 = "jq"
    l10 = "kwxyz"
    score = 0
    for elt in mot:
        if elt in l1:
            score = score + 1
        elif elt in l2:
            score = score + 2
        elif elt in l3:
            score = score + 3
        elif elt in l4:
            score = score + 4
        elif elt in l8:
            score = score + 8
        elif elt in l10:
            score = score + 10
    return score

