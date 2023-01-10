#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      tang.doui
#
# Created:     23/09/2021
# Copyright:   (c) tang.doui 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------

n=input("n?")
n=int (n)

j=2

while n%j != 0:

    j=j+1

if j==n:

    print("premier")

else:

    print(n," n'est pas un nombre premier!")
