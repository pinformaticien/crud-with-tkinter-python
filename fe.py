from tkinter import *
from tkinter import ttk
from ttkthemes import themed_tk as tk
import be # be means backend

#CREATION DE LA FENETRE PRINCIPALE
rt = tk.ThemedTk()
rt.get_themes()
rt.set_theme("radiance")
rt.wm_title("Systéme de Gestion des Personnels ")

#SECTION DES DIFFERENTES FONCTIONS RLEIEES AUX BOUTONS

#LORSQU'UN ENREGISTREMENT DE LA ttk.Listbox EST SELECTIONNE
def gtr(event): # gtr = get the record
    global tt # target tuple
    yoid=lb1.curselection()[0] # gets the actual nbr in: ttk.Listbox
    tt=lb1.get(yoid) # get rec assoc'd w/yoid yoid=your id
    e1.delete(0, END)
    e1.insert(END, tt[1])
    e2.delete(0, END)
    e2.insert(END, tt[2])
    e3.delete(0, END)
    e3.insert(END, tt[3])
    e4.delete(0, END)
    e4.insert(END, tt[4])
    


def updt_command():
        if(len(fn.get())!=0):
                be.updt(tt[0], fn.get(), ln.get(), dpt.get(), sal.get())
                

#La fonction de recherche d'enregistrement[s]
def findit_command():
        lb1.delete(0, END)
        for row in be.findit(fn.get(),ln.get(),dpt.get(),sal.get()):
                lb1.insert(END, row)



#La fonction qui efface les donnees dans les champs de saisie
def clearit_command():
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)


#la fonction de suppression d'un enregistrement
def dele_command():
    if(len(fn.get())!=0):
        be.dele(tt[0])
        clearit_command()
        view_command()

#la fonction permettant de lister tous les enregisterement
def view_command():
    lb1.delete(0, END)
    for row in be.view():
        lb1.insert(END, row)

#la fonction d'ajout
def add_command():
    if(len(fn.get())!=0):
        be.addrec(fn.get(), ln.get(), dpt.get(), sal.get())
        #Maintenant on insére l'enregistrement dans la ttk.Listbox
        lb1.delete(0, END)
        lb1.insert(END, (fn.get(), ln.get(), 
                    dpt.get(), sal.get()))


#SECTION DES BOUTONS DE COMMANDES
b1=ttk.Button(rt, text="List Recs", width=25,\
            command=view_command)
b1.grid(row=0, column=0)

b2=ttk.Button(rt, text="Add Recs", width=25,\
        command=add_command)
b2.grid(row=0, column=1)

b3=ttk.Button(rt, text="Delete", width=18,\
            command=dele_command)
b3.grid(row=0, column=2)

b4=ttk.Button(rt, text="Update", width=10,\
        command=updt_command)
b4.grid(row=0, column=4)

b5=ttk.Button(rt, text="Find", width=10,\
                command=findit_command)
b5.grid(row=0, column=5)

b6=ttk.Button(rt, text="Clear", width=10,\
            command=clearit_command)
b6.grid(row=0, column=6)






#ttk.LabelS POUR LES VARIABLES
r=2

l0=ttk.Label(rt, text="")
l0.grid(row=r-1, column=0)

l1=ttk.Label(rt, text="F.Name")
l1.grid(row=r, column=0)

l2=ttk.Label(rt, text="L.Name")
l2.grid(row=r+1, column=0)

l3=ttk.Label(rt, text="Dept")
l3.grid(row=r+2, column=0)

l4=ttk.Label(rt, text="Salary")
l4.grid(row=r+3, column=0)

#LES CHAMPS DE SAISIE DES VARIABLES
fn=StringVar()
e1=ttk.Entry(rt, textvariable=fn)
e1.grid(row=r, column=1)


ln=StringVar()
e2=ttk.Entry(rt, textvariable=ln)
e2.grid(row=r+1, column=1)


dpt=StringVar()
e3=ttk.Entry(rt, textvariable=dpt)
e3.grid(row=r+2, column=1)


sal=StringVar()
e4=ttk.Entry(rt, textvariable=sal)
e4.grid(row=r+3, column=1)


#SECTION DE ttk.Listbox
lb1=Listbox(rt, height=6, width=40)
lb1.grid(row=8, column=0, rowspan=8, columnspan=6)

#ttk.Scrollbar pour la ttk.Listbox
sb=ttk.Scrollbar(rt)
sb.grid(row=7, column=5, rowspan=8)

lb1.configure(yscrollcommand=sb.set)
sb.configure(command=lb1.yview)

#EVENEMENT LORS D'UNE SELECTION D'UN ENREGISTREMENT
lb1.bind('<<ttk.ListboxSelect>>', gtr)

#boucle mainloop
rt.mainloop()