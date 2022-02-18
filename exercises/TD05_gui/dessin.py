from tkinter import * 
fenetre = Tk()
import tkinter as tk
canvas = Canvas(fenetre, width=1000, height=500, background='black')
ligne1 = canvas.create_line(75, 0, 75, 120)
ligne2 = canvas.create_line(0, 60, 150, 60)
txt = canvas.create_text(75, 60, font="Arial 16 italic", fill="blue")
canvas.grid(row=1,column=1,rowspan=3, columnspan=3)
fenetre.title("Mon dessin")
couleur_a_choisir = "magenta"
def color ():
    global couleur_a_choisir
    couleur_a_choisir = input()
import random 
def Cercle():
    x = random.randint(0,900)
    y = random.randint(100,500)
    x1 = (x + 100)
    y1 = (y-100)
    canvas.create_oval(x,y,x1,y1, fill =couleur_a_choisir)
def rectangle():
    x = random.randint(0,900)
    y = random.randint(100,500)
    x1 = (x + 100)
    y1 = (y-100)
    canvas.create_rectangle(x,y,x1,y1, fill = couleur_a_choisir)
def croix():
    x = random.randint(33,933)
    y = random.randint(100,500)
    x1 = (x + 33)
    y1 = (y + 99)
    x0 = (x - 33)
    y0 = (y + 33)
    x2 = (x + 66)
    y2 = (y + 66)
    canvas.create_rectangle(x, y, x1, y1, fill = couleur_a_choisir)
    canvas.create_rectangle(x0,y0, x2,y2, fill= couleur_a_choisir)
def undo():
    v=4
import tkinter.font as tkFont
Button(fenetre, text = "Choisir une couleur",activebackground = "magenta",font = ("helvetica","30" ), command = color ).grid(row=0, column=2)
Button(fenetre, text = "Undo", activebackground="pink", font = ("helvetica","30" ), command = undo).grid(row=0,column=1)
Button(fenetre, text ='Cercle',font = ("helvetica","30" ), command= Cercle, activebackground= "yellow").grid(row=1,column=0)
Button(fenetre, text ='Carré',font = ("helvetica","30" ), command = rectangle,activebackground="red").grid(row=2,column=0)
Button(fenetre, text ='Croix',font = ("helvetica","30" ), command = croix,activebackground="green").grid(row=3,column=0)
fenetre.mainloop() 