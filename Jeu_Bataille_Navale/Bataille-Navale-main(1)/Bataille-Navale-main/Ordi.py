from tkinter import*
import tkinter as tk
from math import*
import random
import time


#Initialise toutes les variables
class GameState(object):
    def __init__(self) -> None:

        self.score = 0
        self.last = (0,0)
        self.bat1 = 0
        self.bat2 = 0
        self.bat3 = 0

        self.bateau1 = []
        self.bateau2 = []
        self.bateau3 = []

        self.temps1 = 0
        self.temps2 = 0
        self.temps = 0







#Fonction du jeu
def JeuO(diffi, user, gstate):

        game = True
        # gstate.print_temps()


        def scorepoints(gstate):
            gstate.score = gstate.score + 1


        while game == True:

            gstate.temps1 = time.time()
            global labelbat
            master = Tk()
            master.title('Jeu')
            master.geometry("1200x900")
            master.configure(background='lightgrey')
            canvas=Canvas(master, width=1200, height=900)
            canvas.pack()


            newWindow = Toplevel(master)
            newWindow.title("Tableau de Bord")
            newWindow.geometry("600x300")
            framenew = Frame(newWindow)
            framenew.pack()
            quitter = Button(framenew, text = "Quitter", bg = "red", font = "Helvtica 10 bold", command = master.destroy)
            quitter.pack(pady = 2)
            labelessai = Label ( framenew, text = '', font = "Helvetica 15 bold")
            labelessai.pack(pady = 2)
            labelbat = Label(newWindow, text = '', font = 'Helvetica 15 bold')
            labelbat.pack()


            #Détermine la direction du bateau et la colonne et ligne de départ de la créaion du bateau
            def creation(gstate):
                #direction hasard ------- 0 = vertical -- 1 = horizontal
                direction1 = random.randrange(0,2)
                direction2 = random.randrange(0,2)
                direction3 = random.randrange(0,2)
                #colonne hasard
                colonne1 = random.randrange(1,10)
                colonne2 = random.randrange(1,9)
                colonne3 = random.randrange(1,8)
                #ligne hasard
                ligne1 = random.randrange(2,11)
                ligne2 = random.randrange(3,11)
                ligne3 = random.randrange(4,11)

            #Création des bateaux (coordonnées)
                if direction1 == 0:
                    gstate.bateau1= [(colonne1,ligne1), (colonne1, ligne1-1)]
                    #print(gstate.bateau1)

                else :
                    gstate.bateau1 = [(colonne1,ligne1), (colonne1+1,ligne1)]
                    #print(gstate.bateau1)

                if direction2 == 0:
                    gstate.bateau2= [(colonne2,ligne2), (colonne2, ligne2-1), (colonne2, ligne2-2)]
                    #print(gstate.bateau2)

                else :
                    gstate.bateau2 = [(colonne2,ligne2), (colonne2+1,ligne2), (colonne2+2, ligne2)]
                    #print(gstate.bateau2)

                if direction3 == 0:
                    gstate.bateau3= [(colonne3,ligne3), (colonne3, ligne3-1), (colonne3, ligne3-2), (colonne3, ligne3-3)]
                    #print(gstate.bateau3)

                else :
                    gstate.bateau3 = [(colonne3,ligne3), (colonne3+1,ligne3), (colonne3+2,ligne3), (colonne3+3,ligne3)]
                    #print(gstate.bateau3)

        #Vérification que les bateaux ne se croisent pas
            def test(gstate):
                global jeu


                if gstate.bateau1[0] not in gstate.bateau2 and gstate.bateau1[0] not in  gstate.bateau3:
                    if gstate.bateau1[1] not in gstate.bateau2 and gstate.bateau1[1] not in gstate.bateau3:
                        if gstate.bateau2[0] not in gstate.bateau3:
                            if gstate.bateau2[1] not in gstate.bateau3:
                                if gstate.bateau2[2] not in gstate.bateau3:
                                    jeu = True
                                else:
                                    jeu = False
                            else:
                                jeu = False
                        else:
                            jeu = False
                    else:
                        jeu = False
                else:
                    jeu = False




            creation(gstate)
            test(gstate)


            if jeu == False:
                print('Erreur dans Creation, retentative en cours')

                while jeu == False:
                    creation(gstate)
                    test(gstate)


            #Croix si le bateau a été touché
            def reveal():
                for co in gstate.bateau1:
                    x = co[0]
                    y = co[1]
                    x = ((x+1)*100)-65
                    y = (y*75)+5
                    canvas.create_line(x,y,x+75,y+60, fill = 'red', width = 1.5)
                    canvas.create_line(x, y+60, x+75, y, fill = 'red', width = 1.5)

                for co2 in gstate.bateau2:
                    x = co2[0]
                    y = co2[1]
                    x = ((x+1)*100)-65
                    y = (y*75)+5
                    canvas.create_line(x,y,x+75,y+60, fill = 'red', width = 1.5)
                    canvas.create_line(x, y+60, x+75, y, fill = 'red', width = 1.5)

                for co3 in gstate.bateau3:
                    x = co3[0]
                    y = co3[1]
                    x = ((x+1)*100)-65
                    y = (y*75)+5
                    canvas.create_line(x,y,x+75,y+60, fill = 'red', width = 1.5)
                    canvas.create_line(x, y+60, x+75, y, fill = 'red', width = 1.5)


            #def pour le tir
            def tir(event):

                global labelbat
                x, y = event.x, event.y
                #coordonnes precises
                x = ((x-120)//100) + 1
                y = ((y-75)//75) + 1
                print('{}, {}'.format(x, y)) #Coordonnes Carre
                souris = (x,y)


                if x>=1 and x<=10 and y>=1 and y<=10 and souris != gstate.last:
                    if (souris in gstate.bateau1) or (souris in gstate.bateau2) or (souris in gstate.bateau3):

                        x = ((x+1)*100)-65
                        y = (y*75)+5
                        canvas.create_line(x,y,x+75,y+60, fill = 'red', width = 1.5)
                        canvas.create_line(x, y+60, x+75, y, fill = 'red', width = 1.5)

                        if souris in gstate.bateau1:
                            gstate.bat1 = gstate.bat1 + 1
                            labelbat['text'] = "Touche!"
                            if gstate.bat1 == 2:
                                labelbat['text'] = "Bateau 1 coule!"

                        elif souris in gstate.bateau2:
                            gstate.bat2 = gstate.bat2 + 1
                            labelbat['text'] = "Touche!"

                            if gstate.bat2 == 3:
                                labelbat['text'] = "Bateau 2 coule!"

                        elif souris in gstate.bateau3:
                            gstate.bat3 = gstate.bat3 + 1
                            labelbat['text'] = "Touche!"

                            if gstate.bat3 == 4:
                                labelbat['text'] = "Bateau 3 Coule!"

                    else:

                            x = ((x+1)*100) - 75
                            y = (y*75) + 5

                            canvas.create_rectangle(x, y, x+ 90, y+65, fill = 'lightblue', outline = 'lightblue')
                            labelbat['text'] = "Loupe!"
                            scorepoints(gstate)
                            labelessai['text'] = "essai numero: " + str(gstate.score)

                            if gstate.score>=diffi:

                                labelbat['text'] = "Tu as perdu, tu as depasse le nopmbre d'essais limite\n voici les bateaux : \n"+ "bateau 1: " + str(gstate.bateau1) + "\n" + "bateau 2: " + str(gstate.bateau2) + "\n" +"bateau 3: " + str(gstate.bateau3)

                                reveal()
                                gstate.temps2 = time.time()
                                gstate.temps = int(gstate.temps2 - gstate.temps1)
                                with open("Score.txt", "a") as s:
                                    s.write(user)
                                    s.write(" a perdu et a fait un score de: ")
                                    s.write(str(gstate.score))
                                    s.write(" pour un temps de: ")
                                    s.write(str(gstate.temps))
                                    s.write(" secondes \n")

                                if gstate.score == diffi+2:
                                    master.destroy()


                    if gstate.bat1 == 2 and gstate.bat2 == 3 and gstate.bat3 == 4:
                        gstate.temps2 = time.time()
                        gstate.temps = int(gstate.temps2 - gstate.temps1)
                        labelbat = Label(newWindow, text = 'Bravo! Tu as reussi a trouver tout les bateaux! Tu as fais : ', font = "Helvetica 15 bold")
                        labelbat.pack()
                        labelbat = Label(newWindow, text= gstate.score, font = "Helvetica 15 bold")
                        labelbat.pack()
                        labelbat['text'] = gstate.score
                        labelbat = Label(newWindow, text = 'essais\n pour un temps de: \n' + str(gstate.temps) + " secondes", font = "Helvetica 15 bold")
                        labelbat.pack()
                        with open("Score.txt", "a") as s:
                            s.write(user)
                            s.write(" a fait un score de: ")
                            s.write(str(gstate.score))
                            s.write(" pour un temps de: ")
                            s.write(str(gstate.temps))
                            s.write(" secondes \n")






                gstate.last = souris



            master.bind('<Button>', tir)



            # Taille des Rectangles : 100 px pour 75 px
            #creation de lignes verticals et horizontales

            for i in range (11):
                canvas.create_line(120,((i+1)*75),1120,((i+1)*75), fill="black", width=2.5)
                canvas.create_line((20+((i+1)*100)), 75, (20+((i+1)*100)) ,825, fill = 'black', width = 2.5)

            #nommentlature des carrees

            for j in range (1,11):
                canvas.create_text( 60 + (j*100), 40 , text= j, font=('Helvetica 15 bold'))
                canvas.create_text( 80, 45+(j*75) , text= j, font=('Helvetica 15 bold'))








            master.mainloop()

            game = False

