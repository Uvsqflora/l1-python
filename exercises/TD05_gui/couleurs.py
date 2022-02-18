from tkinter import * 
fenetre = Tk()
import tkinter as tk
canvas = Canvas(fenetre, width=256, height=256, background='black')
txt = canvas.create_text(75, 60, font="Arial 16 italic", fill="blue")
canvas.grid(row=1,column=1,rowspan=3, columnspan=3)
fenetre.title("Couleurs")

colors = ["red", "green","blue"]
r , g, b= "red", "green", "blue"
def get_color(r, g, b):
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)
import tkinter.font as tkFont
import random 
def draw_pixel(i,j,color):
    canvas.create_rectangle(i,j,i,j, fill=color,outline=color )

def draw_random():
    for i in range(256):
        for j in range(256):
            color=random.choice(colors)
            draw_pixel(i,j,color)

def degrade_gris():
    for i in range(256):
        for j in range(256):
            color = get_color(i,i,i)
            draw_pixel(i,j,color)

def degrade_2D ():
    for i in range (256):
        for j in range(256):
            color = get_color (i,0,j)
            draw_pixel(i,j,color)
    
 
Button(fenetre, text =('Aléatoire'), font = ("helvetica","20",), command= draw_random, bg= "white", fg ="blue").grid(row=1,column=0)
Button(fenetre, text ='Dégradé gris',font = ("helvetica","20" ), command = degrade_gris,bg= "white",fg ="blue").grid(row=2,column=0)
Button(fenetre, text ='Dégradé 2D',font = ("helvetica","20" ), command = degrade_2D,bg= "white",fg ="blue").grid(row=3,column=0)
fenetre.mainloop() 
