import tkinter as tk
CANVAS_WIDTH, CANVAS_HEIGHT = 600, 400
root = tk.Tk()
canvas = tk.Canvas(root, width = CANVAS_WIDTH, height = CANVAS_HEIGHT)
# Début de votre code
x0 = 100
x1 = CANVAS_WIDTH - 300
y = CANVAS_HEIGHT / 2
canvas.create_line(y + 100, x1, y+100, x0)
canvas.create_oval(x1 - 50, y - 150, x1 + 50, y-50 )
canvas.create_oval(x1 - 50, y + 50, x1 + 50, y - 50)
canvas.create_oval(x1 - 50, y+50  , x1 + 50, y + 150)
# Fin de votre code
canvas.grid()
root.mainloop()