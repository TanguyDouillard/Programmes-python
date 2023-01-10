from tkinter import*


def dollars():
    a=var_entrees.get()
    a=round(a)
    b=a*1.12
    label_dollars["text"]=b

def euros():
    a=var_entrees.get()
    a=round(a)
    b=a * 0.89
    label_euros["text"]=b


fenetre = Tk()
fenetre.title("Convertisseur")
fenetre.minsize(height=250, width=250)

#Label dans fenetre
label_convertisseur = Label(fenetre,text="Convertisseur",fg='white', bg="red",font="Arial 15 italic")
label_convertisseur.grid( row = 0 , column = 1, padx = 10, pady = 10)

#bouton dans fenetre
bouton_quitter = Button(fenetre, text = "Quitter",bg = 'red', fg = 'white',command = fenetre.destroy)
bouton_quitter.grid( row = 3, column = 1, padx = 10, pady =10)

#Saisie
var_entrees = DoubleVar()
saisie_entrees = Entry(fenetre,textvariable = var_entrees , width =10)
saisie_entrees.grid(row = 1, column = 1, padx = 10, pady=10)

#frame 1
frame_1 = Frame(fenetre, width=150, height=150, bg = 'black', bd = 3, relief = RAISED)
frame_1.grid(row = 2, column = 1, padx=10,pady=10)

    #Boutons dans frame 1

bouton_dollars = Button(frame_1, text = "$",bg = 'red', fg = 'white',command = dollars)
bouton_euros = Button(frame_1, text = "€",bg = 'red', fg = 'white',command = euros)

bouton_dollars.grid(row = 0, column = 0, padx = 10, pady = 10)
bouton_euros.grid(row = 0, column = 1, padx = 10, pady = 10)

    #Labels dans frame 1

label_dollars = Label(frame_1,text=" ",bg="red", fg="white", width = 10, font="Arial 15 italic")
label_euros = Label(frame_1,text=" ",bg = "red", fg="white", width = 10, font="Arial 15 italic")

label_dollars.grid(row = 1, column = 0, padx = 10, pady = 10)
label_euros.grid(row = 1, column = 1, padx = 10, pady = 10)

fenetre.mainloop()