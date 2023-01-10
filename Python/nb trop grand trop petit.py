#-------------------------------------------------------------------------------
# Name:        module1
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
        t=int(input("Redevine"))
        y=y+1

    elif t>n:
        print(t,"est trop grand")
        t=input("Redevine")
        t=int(t)
        y=y+1

print("Bravo tu as trouvé! Le bon nombre était bien",n,". Tu as mis",y,"essais!")