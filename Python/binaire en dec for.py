#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      tang.doui
#
# Created:     22/09/2021
# Copyright:   (c) tang.doui 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------

n=input("binaire")

##x=n[-1]
##x=int(x)
##x=x*(2**0)

x=0
j=0

for i in range(1,len(n)):


    y=n[-1*i]
    y=int(y)
    y=y*(2**j)

    j=j+1




    x=y+x


print(x)