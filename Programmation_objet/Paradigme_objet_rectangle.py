


class rectangle(object):
    def __init__ (self, longueur, largeur):
        self.longueur=longueur
        self.largeur=largeur

    def Aire(self):
        self.aire=self.largeur*self.longueur
        print(self.aire)

    def Perimetre(self):
        self.per=self.largeur*2+self.longueur*2
        print(self.per)

    def iscarre(self):
        if self.largeur==self.longueur:
            print("C'est un carré !")
        else:
            print("Ce n'est pas un carré, mais bien un rectangle !")

