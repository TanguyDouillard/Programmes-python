##from time import time
##from math import *
##debut = time()
##for i in range(100000):
##    a = 1.001**i
##fin=time()
##duree=fin-time()
##print(duree)
##print(a)


##debut=time()
##for i in range(100000):
##    a=2**i
##fin = time()
##duree=fin-debut
##print(duree)
##print(a)

##tab=[2,5,4,7,1,8]
##tab2= sorted(tab)
##print(tab)
##print(tab2)
##tab.sort()
##print(tab)

def tri(a,b,c):
    tab=[]
    if a<=b and a<=c:
        tab.append(a)
        if b<=c:
            tab.append(b)
            tab.append(c)
        else:
            tab.append(c)
            tab.append(b)
    elif b<=a and b<=c:
        tab.append(b)
        if a<=c:
            tab.append(a)
            tab.append(c)
        else:
            tab.append(c)
            tab.append(a)
    elif c<=a and c<=b:
        tab.append(c)
        if a<=b:
            tab.append(a)
            tab.append(b)
        else:
            tab.append(b)
            tab.append(a)

    return tab



def echange(l):
    a=l[0]
    b=l[1]
    l[0]=b
    l[1]=a
    return l

def Tri_2(tab):
    debut=0
    fin=len(tab)-1
    while debut != fin:
        if tab[debut] == 1:
            tab[debut],tab[fin]=tab[fin],tab[debut]
            fin = fin - 1
        else:
            debut = debut + 1
    return tab

def Tri_3(tab):
    for i in range(len(tab)):
        m=min(tab[i:])
        a=tab.index(m)
        tab[i],tab[a]=tab[a],tab[i]
    return tab

def Tri_4(tab):
    debut=0
    while debut != (len(tab)-1):
        m=min(tab[debut:])
        a=tab.index(m)
        tab[debut],tab[a]=tab[a],tab[debut]
        debut=debut+1
    return tab

def Syracuse(N):
    #i=0
    vol = []
    while N!=1:
        if N%2==0:
            N=N/2
            #i = i + 1
            vol.append(N)
        else:
            N=N*3
            N=N+1
            #i=i+1
            vol.append(N)
    i = len(vol)
    return i, ":", vol


def dichotomie(x,tab):
    if tab == []:
        return False
    elif (x<tab[0]) or (x>tab[len(tab)-1]):
        return False


    debut = 0
    fin = len(tab)-1
    while debut <= fin:
        m = (debut+fin)//2
        if x == tab[m]:
            return True
        if x > tab[m] :
            debut = m+1
        else:
            fin = m-1
    return False









