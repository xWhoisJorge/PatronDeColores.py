#2: Patron de colores

from tkinter import *
root = Tk()
root.title("Patron Colores")
root.geometry("300x300")
root.resizable(0,0)

cuadro1 = Frame()
cuadro1.grid(row=0,column=0)
cuadro1.config(width="100", height="100")
cuadro1.config(bg="#B2085D")

cuadro2 = Frame()
cuadro2.grid(row=1,column=0)
cuadro2.config(width="100", height="100")
cuadro2.config(bg="#3A3D44")

cuadro3 = Frame()
cuadro3.grid(row=2,column=0)
cuadro3.config(width="100", height="100")
cuadro3.config(bg="#B2085D")

cuadro4 = Frame()
cuadro4.grid(row=0,column=1)
cuadro4.config(width="100", height="100")
cuadro4.config(bg="#3A3D44")

cuadro5 = Frame()
cuadro5.grid(row=1,column=1)
cuadro5.config(width="100", height="100")
cuadro5.config(bg="#B2085D")

cuadro6 = Frame()
cuadro6.grid(row=2,column=1)
cuadro6.config(width="100", height="100")
cuadro6.config(bg="#3A3D44")

cuadro7 = Frame()
cuadro7.grid(row=0,column=2)
cuadro7.config(width="100", height="100")
cuadro7.config(bg="#B2085D")

cuadro8 = Frame()
cuadro8.grid(row=1,column=2)
cuadro8.config(width="100", height="100")
cuadro8.config(bg="#3A3D44")

cuadro9 = Frame()
cuadro9.grid(row=2,column=2)
cuadro9.config(width="100", height="100")
cuadro9.config(bg="#B2085D")

root.mainloop()