from tkinter import*
from PIL import Image, ImageTk
from math import*
import random
from Ordi import JeuO, GameState
from JeuDeux import JeuD, GameStateD

#Création de la page
root = Tk()
root.title("Bataille Navale")
root.geometry("700x800")
frame_1 = Frame(root)
frame_1.pack(ipadx = 1, ipady = 1, side = TOP)


def JeuDeux():
    gstateD = GameStateD()
    JeuD(diffi, user, gstateD)

def JeuOrdi():
    gstate = GameState()
    JeuO(diffi, user, gstate)


#Ce sont les règles
loi = (" Les Regles de la bataille navale sont simples:\n" +
        "Choisis ton niveau de difficulté (le nombre d'essais max) du jeu (Tu peux choisir entre 5 et 80)\n"+
        "Puis écris ton nom de Joueur dans la case prévu à cet effet \n"
        "Enfin clique sur 'valider' afin de commencer à Jouer\n"+
        "Quand on 'Joue a Deux':\n" +
        "Le premier Joueur (le placeur) place ses trois bateaux dans l'ordre suivant:\n"+
        "Bateau1 : 2 cases\n"+
        "Bateau2 : 3 cases\n"+
        "Bateau3 : 4 cases\n"+
        "Le placeur doit impérativement placer les bateaux\n"+
        "de facon Horizontale ou Verticale\n"+
        "Il ne peut pas les placer en diagonale ou les superposer\n"+
        "Une fois les 3 bateaux placés, \n"+ "clique une fois sur le plateau pour qu'ils disparaissent\n"+
        "C'est désormais au tour du tireur \n"+
        "Lorsqu'un bateau est touché, une croix rouge apparait \n"+
        "Sinon c'est un carré bleu\n"+
        "De plus, le tableau de bord t'indiqueras si tu as loupé, touché ou coulé un bateau \n"+
        "la partie se termine soit lorsque le tireur a trouvé tous les bateaux \n"+
        "ou lorsque tout ses essais sont utilisé \n"+
        "Quand on 'Jouer contre l'Ordinateur': \n"+
        "Ici tu as qu'un seul role: celui du tireur afin de trouver les bateaux cachés \n"+
        "Encore une fois la partie se termine lorsque tu as trouvé tous les bateaux \n"+
        "ou lorsque tous tes essais ont été utilisés \n" +
        "Quand on perd: \n tous les bateaux vont apparaitre à la fin de la partie\n pour te montrer ou ces derniers étaient cachés \n" +
        "Dans le cas contraire (la victoire du tireur), ton score et ton temps vont apparaitre\n"+
        "sur le tableau de bord que tu pourras ensuite retrouver dans le fichier:\n Score.txt\n"+
        "Avec la liste de tous les précedents vainceurs du jeu.\n"+
        "Si tu veux rejouer, clique sur quitter dans le tableau de bord \n"+
        "Puis relance le jeu \n"+
        "Amuses toi bien ! \n"
            )


def rules():
    global loi
    fen2 = Toplevel(root)
    fen2.title("Regles")
    fen2.geometry("1000x900")
    framefen2 = Frame(fen2)
    framefen2.pack()
    ListeRule = Label(framefen2, text = loi, font = "Helvetica 15 bold")
    ListeRule.pack(pady = 15)



img = ImageTk.PhotoImage(Image.open('bateau.png'))



canvas1 = Canvas( root, width = 400,
				height = 350)

canvas1.pack(fill = "both", expand = True)


canvas1.create_image( 0, 0, image = img,
					anchor = "nw")





#Titre 'Bataille navale' + Boutons pour 'jouer à deux', 'jouer avec ordi' et 'règles'
label_1 = Label(frame_1,text = "Bataille Navale",width = 20, height= 2, fg = 'white', bg = "black",font = "Arial 15 italic")
label_1.pack()

PlayOrdi = Button( text= "Jouer contre l'Ordinateur",width=20,height=2, bg = "beige", command = JeuOrdi)
PlayDeux = Button( text = "Jouer à Deux",width=20,height=2, bg = "beige",command = JeuDeux)
Regles = Button( text = "Règles", width = 20, height = 2, bg = "beige", command = rules)




button1_canvas = canvas1.create_window(275, 10,
									anchor = "nw",
									window = PlayOrdi)
button2_canvas = canvas1.create_window( 275, 60,
                                     anchor = "nw",
									window = PlayDeux)

button3_canvas = canvas1.create_window( 275,110, anchor = "nw",
									window = Regles)



def valider():
        global diffi
        global difficulte
        global name
        global user
        user = name.get()
        diffi = difficulte.get()


#Queleques détails
text = Label(root, text = "Met ton nom de Gamer dans la bar ci-dessous:", font = "Helvetica 15 bold")
text.pack(pady = 5)
name = StringVar()
name.set("username")
nom = Entry(root, textvariable=name)
nom.pack(pady = 2)
choisi = Label(root, text= "Choisit ton nombre d'essais max:", font = "Helvetica 15 bold")
choisi.pack(pady = 5)
difficulte = IntVar()
difficulte.set(0)
diff = Scale(root, variable= difficulte, from_=5, to_=80, orient=HORIZONTAL)
diff.pack()
val = Button(root, text = 'Valider', bg = "green",font= 'Helvetica 10 bold', command= valider)
val.pack(pady = 5)

quitter = Button(text = 'Quitter', width= 20, height = 2, bg = "beige", command = root.destroy)
quitter.pack(pady = 5)



root.mainloop()
