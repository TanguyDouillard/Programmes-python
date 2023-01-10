from tkinter import*
import tkinter as tk
from PIL import Image,ImageTk
import time

class GameStateD(object):
    def __init__(self) -> None:


        self.bateau1 = []

        self.bateau2 = []

        self.bateau3 = []

        self.bat1 = 0
        self.bat2 = 0
        self.bat3 = 0

        self.last = (0,0)
        self.score = 0

        self.temps1 = 0
        self.temps2 = 0
        self.temps = 0


def JeuD(diffi, user, gstate):


        master = Tk()
        master.title('Jeu')
        master.geometry("1200x900")
        master.configure(background='lightgrey')
        canvas=Canvas(master, width=1200, height=900)
        canvas.pack()

        # Taille des Rectangles : 100 px pour 75 px
        #creation de lignes verticals et horizontales
        def board():
            for i in range (11):
                canvas.create_line(120,((i+1)*75),1120,((i+1)*75), fill="black", width=2.5)
                canvas.create_line((20+((i+1)*100)), 75, (20+((i+1)*100)) ,825, fill = 'black', width = 2.5)

        #nommentlature des carrees

            for j in range (1,11):
                canvas.create_text( 60 + (j*100), 40 , text= j, font=('Helvetica 15 bold'))
                canvas.create_text( 80, 45+(j*75) , text= j, font=('Helvetica 15 bold'))

        game = True





        def selection(event):
            global game
            x, y = event.x , event.y
            print('{}, {}'.format(x, y)) #coordonnes precises
            x = ((x-120)//100) + 1
            y = ((y-75)//75) + 1
            souris = (x,y)
            print('{}, {}'.format(x, y)) #Coordonnes Carre



            count = 0
            if x>=1 and x<=10 and y>=1 and y<=10 and gstate.last!=souris:
                if len(gstate.bateau1) <=1 and count <=1:
                    gstate.bateau1.append(souris)
                    x = ((x+1)*100)-65
                    y = (y*75)+5
                    canvas.create_line(x,y,x+75,y+60, fill = 'red', width = 1.5)
                    canvas.create_line(x, y+60, x+75, y, fill = 'red', width = 1.5)
                    count = count +1
                elif len(gstate.bateau2) <=2 and count <=4:
                    gstate.bateau2.append(souris)
                    x = ((x+1)*100)-65
                    y = (y*75)+5
                    canvas.create_line(x,y,x+75,y+60, fill = 'red', width = 1.5)
                    canvas.create_line(x, y+60, x+75, y, fill = 'red', width = 1.5)
                    count = count + 1
                elif len(gstate.bateau3) <=3 and count <=8:
                    gstate.bateau3.append(souris)
                    x = ((x+1)*100)-65
                    y = (y*75)+5
                    canvas.create_line(x,y,x+75,y+60, fill = 'red', width = 1.5)
                    canvas.create_line(x, y+60, x+75, y, fill = 'red', width = 1.5)
                    count = count + 1
                else:
                    game = False
                    canvas.delete("all")
                    board()
                    master.bind('<Button>', tir)
                    gstate.temps1 = time.time()
                gstate.last = souris


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

        def tir(event):
            global game
            global labelbat



            x, y = event.x, event.y
            #coordonnes precises
            x = ((x-120)//100) + 1
            y = ((y-75)//75) + 1
            print('{}, {}'.format(x, y)) #Coordonnes Carre
            souris = (x,y)



            if x>=1 and x<=10 and y>=1 and y<=10 and gstate.last != souris:

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



                    if gstate.bat1 == 2 and gstate.bat2 == 3 and gstate.bat3 == 4:
                        gstate.temps2 = time.time()
                        gstate.temps = int(gstate.temps2 - gstate.temps1)
                        labelbat = Label(newWindow, text = 'Bravo! \n Tu as reussi a trouver tout les bateaux!\nTu as fais : ', font = "Helvetica 15 bold")
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






                else:
                    x = ((x+1)*100) - 75
                    y = (y*75) + 5

                    canvas.create_rectangle(x, y, x+ 90, y+65, fill = 'lightblue', outline = 'lightblue')
                    labelbat['text'] = "Loupe!"
                    scorepoints()
                    labelessai['text'] = "essai numero: " + str(gstate.score)



                if gstate.score>=diffi:
                    labelbat['text'] = "Tu as perdu,\n Tu as depasse le nombre d'essais limite\n voici les bateaux : \n"+ "bateau 1: " + str(gstate.bateau1) + "\n" + "bateau 2: " + str(gstate.bateau2) + "\n" +"bateau 3: " + str(gstate.bateau3)

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

                last = souris




        def scorepoints():
            gstate.score = gstate.score + 1


        if game == True:
            board()
            global labelbat
            master.bind('<Button>', selection)
            newWindow = Toplevel(master)
            newWindow.title("Tableau de Bord")
            newWindow.geometry("400x300")
            framenew = Frame(newWindow)
            framenew.pack()
            quitter = Button(framenew, text = "Quitter", bg = "red", font = "Helvtica 10 bold", command = master.destroy)
            quitter.pack(pady = 2)
            labelessai = Label(framenew, text = '', font = 'Helvetica 15 bold')
            labelessai.pack(pady = 2)
            labelbat = Label(newWindow, text = '', font = 'Helvetica 15 bold')
            labelbat.pack(pady = 2)






        master.mainloop()
