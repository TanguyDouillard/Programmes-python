#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      tang.doui
#
# Created:     22/09/2021
# Copyright:   (c) tang.doui 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------

n=input("binaire")

x=n[-1]
x=int(x)
x=x*(2**0)

y=n[-2]
y=int(y)
y=y*(2**1)

z=n[-3]
z=int(z)
z=z*(2**2)

a=n[-4]
a=int(a)
a=a*(2**3)

d=x+y+z+a

print(d)