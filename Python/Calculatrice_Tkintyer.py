from tkinter import *

def Bouton_0():
    pass

def Bouton_1():
    pass

def Bouton_2():
    pass

def Bouton_3():
    pass

def Bouton_4():
    pass

def Bouton_5():
    pass

def Bouton_6():
    pass

def Bouton_7():
    pass

def Bouton_8():
    pass

def Bouton_9():
    pass


def Addition ():
    global a, operation
    a=var_Entrees.get()
    operation=1


def Soustraction ():
    global a, operation
    a=var_Entrees.get()
    operation=2

def Multiplication ():
    global a, operation
    a=var_Entrees.get()
    operation=3

def Division ():
    global a, operation
    a=var_Entrees.get()
    operation=4

def Egal ():
    global a, operation
    b=var_Entrees.get()

    if operation==1:
        resultat_Addition=a+b
        label_resultat["text"]=resultat_Addition

    elif operation==3:
        resultat_Multiplication=a*b
        label_resultat["text"]=resultat_Multiplication

    elif operation==2:
        resultat_Soustraction=a-b
        label_resultat["text"]=resultat_Soustraction

    elif operation==4:
        resultat_Division=a/b
        label_resultat["text"]=resultat_Division



#-------------------------------------------------------------------------------


fenetre = Tk()
fenetre.title("Calculatrice")

#fenetre1
frame_1 = Frame(fenetre, width=350, height=150, bg = 'grey', bd = 3, relief = RAISED)
frame_1.pack(padx=10,pady=10)

    #Labels

var_Entrees = IntVar()
saisie_Entrees = Entry(frame_1,textvariable = var_Entrees , width =10)
saisie_Entrees.pack(side = BOTTOM,padx=5,pady=5)

label_resultat = Label(frame_1,text=" ",bg="white", width = 10, font="Arial 15 italic")
label_resultat.pack(side = TOP,padx=5,pady=5)


#fenetre2
frame_2 = Frame(fenetre, width=350, height=400, bg = 'grey', bd = 3, relief = RAISED)
frame_2.pack(padx=10,pady=10)

    #boutons
bouton_Addition = Button(frame_2, text = "+",bg = 'white',command = Addition)
bouton_Soustraction = Button(frame_2, text = "-",bg = 'white',command = Soustraction)
bouton_Multiplication = Button(frame_2, text = "x",bg = 'white',command = Multiplication)
bouton_Division = Button(frame_2, text = "/",bg = 'white',command = Division)
bouton_Egal = Button(frame_2, text = "=",bg = 'white',command = Egal)
bouton_quitter = Button(fenetre,text = " Quitter ",bg = 'white' ,command = fenetre.destroy)
        #boutons nombres
bouton_0 = Button(frame_2, text = "0", bg = 'white', command = Bouton_0)
bouton_1 = Button(frame_2, text = "1", bg = 'white', command = Bouton_1)
bouton_2 = Button(frame_2, text = "2", bg = 'white', command = Bouton_2)
bouton_3 = Button(frame_2, text = "3", bg = 'white', command = Bouton_3)
bouton_4 = Button(frame_2, text = "4", bg = 'white', command = Bouton_4)
bouton_5 = Button(frame_2, text = "5", bg = 'white', command = Bouton_5)
bouton_6 = Button(frame_2, text = "6", bg = 'white', command = Bouton_6)
bouton_7 = Button(frame_2, text = "7", bg = 'white', command = Bouton_7)
bouton_8 = Button(frame_2, text = "8", bg = 'white', command = Bouton_8)
bouton_9 = Button(frame_2, text = "9", bg = 'white', command = Bouton_9)

bouton_Addition.pack(side = LEFT,padx = 10,pady = 10)
bouton_Soustraction.pack(side = LEFT,padx = 10,pady = 10)
bouton_Multiplication.pack(side = LEFT,padx = 10,pady = 10)
bouton_Division.pack(side = LEFT,padx = 10,pady = 10)
bouton_Egal.pack(side = LEFT, padx = 10,pady = 10)
bouton_quitter.pack(side = LEFT,padx=10,pady=10)

bouton_1.pack(side = TOP, padx=10, pady=10)
bouton_2.pack(side = TOP, padx=10, pady=10)
bouton_3.pack(side = TOP, padx=10, pady=10)
bouton_4.pack(side = TOP, padx=10, pady=10)
bouton_5.pack(side = TOP, padx=10, pady=10)
bouton_6.pack(side = TOP, padx=10, pady=10)
bouton_7.pack(side = TOP, padx=10, pady=10)
bouton_8.pack(side = TOP, padx=10, pady=10)
bouton_9.pack(side = TOP, padx=10, pady=10)



fenetre.mainloop()