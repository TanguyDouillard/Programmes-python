

class Eleve(object):
    def __init__(self,nom):
        self.nom=nom
        self.liste1 =[]
        self.liste2 =[]
        self.moyenne=0

    def Calcul_moyenne(self):
        note1=0
        note2=0

        for i in range(len(self.liste1)):
            note1=note1+self.liste1[i]
        note1=note1/len(self.liste1)

        for i in range(len(self.liste2)):
            note2=note2+self.liste2[i]
        note2=note2/len(self.liste2)

        print("Maths :", note1 , "NSI:" ,note2)



class Prof(object):
    def __init__ (self,matiere):
        self.matiere=matiere

    def Note(self, eleve, note):
        if self.matiere=="Maths":
            eleve.liste1.append(note)
            print (eleve.liste1)
        if self.matiere=="NSI":
            eleve.liste2.append(note)
            print (eleve.liste2)

pmaths=Prof("Maths")
pnsi=Prof("NSI")
e1=Eleve("Bob")