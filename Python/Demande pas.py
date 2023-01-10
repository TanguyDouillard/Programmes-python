#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      tang.doui
#
# Created:     23/09/2021
# Copyright:   (c) tang.doui 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------
a = True

while a:



    for i in range (1,31):

        j=i+1

        if j%3==0 and j%4==0:
            j='POUM'

        elif j%3==0:
            j='pim'

        elif j%4==0:
            j='pam'

        x = input ("continue la suite")
        if x != j:
            a = False

        if i%3==0 and i%4==0:
            i='POUM'

        elif i%3==0:
            i='pim'

        elif i%4==0:
            i='pam'

        print(i)












