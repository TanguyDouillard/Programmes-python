

class Etudiant(object):
    def __init__ (self, note_maths, note_physique, specialité):
        self.Nm=note_maths
        self.Np=note_physique
        self.spe=specialité

    def moyenne(self):
        if self.spe=="Maths" or self.spe=="maths":
            moy = (self.Nm*3+self.Np*2)/5
            print("La moyenne de l'étudiant vaut", moy)
        elif self.spe=="Physique" or self.spe=="physique":
            moy = (self.Nm*2+self.Np*3)/5
            print("La moyenne de l'étudiant vaut", moy)
        else:
            print("La spécialité est fausse")


