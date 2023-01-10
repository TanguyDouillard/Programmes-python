

class Enfant(object):
    def __init__ (self, nom, argent=0):
        self.nom=nom
        self.argent=argent

class Parent(object):

    def donne(self, enfant, somme):
        if somme<0:
            print("Il y a une erreur, la somme est inferieure à 0. Veux-tu enlever de l'argent ? Si oui, utilise la fonction prend")
        else:
            enfant.argent=somme+enfant.argent
            print(enfant.nom, " a ", enfant.argent, "€")

    def prend(self, enfant, somme):
        enfant.argent=enfant.argent-somme
        if enfant.argent<0:
            print(enfant.nom, "est dans le négatif !")
        else:
            print(enfant.nom, 'a', enfant.argent,'€')





dad=Parent()
mom=Parent()
e1=Enfant("Bob")
e2=Enfant("Kevin")
