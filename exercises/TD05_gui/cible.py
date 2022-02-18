import tkinter as tk
CANVAS_WIDTH, CANVAS_HEIGHT = 600, 600
root = tk.Tk()
canvas = tk.Canvas(root, width = CANVAS_WIDTH, height = CANVAS_HEIGHT, bg = "black")
color= ["blue", "green", "black", "yellow", "magenta", "red"]
n = int(input("Choisir un nombre de cercle"))
x1 = CANVAS_WIDTH / 2
y1 = CANVAS_HEIGHT / 2
for i in range (n): 
    x = x1*i/n
    y = y1*i/n
    x1 = CANVAS_WIDTH-x
    y1 = CANVAS_HEIGHT-y
    
    canvas.create_oval(x,y,x1,y1, fill= color[i%len(color)])

canvas.grid()
root.mainloop()