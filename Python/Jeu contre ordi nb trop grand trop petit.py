#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      tang.doui
#
# Created:     07/10/2021
# Copyright:   (c) tang.doui 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from random import randint

n= randint(1,100)

t=input("Devine le nombre")
t=int(t)

y=0


while t!=n:
    if t<n:
        print(t,"est trop petit")
        x=t
        i= randint(x,)
        print(i)

        if i>n:
            print("Mon nombre est trop grand")
            t=input("A toi, redevine!")
            t=int(t)
            x=t
            i= randint(1,x)
        elif i<n:
            print("Mon nombre est trop petit")
            t=input("A toi, redevine!")
            t=int(t)
            x=t
            i= randint(x,100)

        elif i==n:
            print("J'ai trouvé!")



    elif t>n:
        print(t,"est trop grand")
        x=t
        i= randint(1,x)
        print(i)

        if i>n:
            print("Mon nombre est trop grand")
            t=input("A toi, redevine!")
            t=int(t)
            x=t
            i= randint(1,x)
        elif i<n:
            print("Mon nombre est trop petit")
            t=input("A toi, redevine!")
            t=int(t)
            x=t
            i= randint(x,100)

        elif i==n:
            print("J'aitruvé!")

print( "Tu as trouive*é! Le bon nombre était bien",n)