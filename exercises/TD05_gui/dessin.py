from tkinter import * 

fenetre = Tk()
label = Label(fenetre, text="Choisir une couleur")
label.pack()
# bouton de sortie
bouton=Button(fenetre, text="Fermer", command=fenetre.quit)
bouton.pack()
# canvas
canvas = Canvas(fenetre, width=150, height=120, background='black')
ligne1 = canvas.create_line(75, 0, 75, 120)
ligne2 = canvas.create_line(0, 60, 150, 60)
txt = canvas.create_text(75, 60, text="Cible", font="Arial 16 italic", fill="blue")
canvas.pack()
Canvas(fenetre, width=250, height=50, bg='ivory').pack(side=RIGHT, padx=5, pady=5)
Button(fenetre, text ='Cercle').pack(side=TOP, padx=5, pady=5)
Button(fenetre, text ='Carré').pack(side= BOTTOM, padx=5, pady=5)
Button(fenetre, text ='Croix').pack(side=BOTTOM, padx=5, pady=5)
fenetre.mainloop()