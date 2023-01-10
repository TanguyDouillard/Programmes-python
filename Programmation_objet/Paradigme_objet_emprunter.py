

class emprunteur(object):
    def __init__ (self, nom, classe):
        self.nom=nom
        self.classe=classe
        self.liste=liste=[]

    def ajoute(self,livre):
        self.liste.append(livre)

    def nombre(self):
        nb=len(self.liste)
        print(self.nom, "a emprunté", nb, "livres")

    def rendre(self,n):
        if len(self.liste)>=n:
            for i in range(n):
                self.liste.pop(len(self.liste)-1)
        else:
            print(self.nom, "n'a pas assez de livres")




Tanguy=emprunteur("Tanguy","T°5")
Tanguy.ajoute("Gargantua")
Tanguy.ajoute("1984")
