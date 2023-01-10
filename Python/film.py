#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      tang.doui
#
# Created:     16/09/2021
# Copyright:   (c) tang.doui 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------
heure = input ("debut du film ")
h = heure [0:2]
h = int (h)
d = heure [3:5]
d =int (d)
z = input ("duree du film")
m = z[0:2]
m = int (m)
s = z[3:5]
s= int(s)
c = h + m
t = d + s
if t == 60:
    print(c+1 ,":00")
elif t > 60:
    print(c+1 ,":", t-60)
elif c>24 and t>60:
 print(c-24,":",t-60)
elif c==24 and t>60:
     print(c-24 ,":", t-60)

else:
    print(c ,":", t)





