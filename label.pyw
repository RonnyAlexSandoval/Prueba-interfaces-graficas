
from tkinter import *
import os
from PIL import Image, ImageTk


root=Tk()
root.title("Fisica Moderna")
fr=Frame(root, width=700, height=600)                           #se especifica el contenedor padre del frame
fr.pack()                                                       #se empaqueta



#TITULO1
label1=Label(fr, text="Gato de Schrodinger", fg="blue", font=("Times New Roman", 15))         #se especifica el contenedor padre edl label
#label1.pack()                                                                                #empaquetado adaptable
label1.place(x=50,y=50)                                                                       #empaquetado no adaptable con coordenadas y color

#TITULO2
Label(fr,text="Paradoja del gato", fg="red", font=("Times New Roman", 10)).place(x=50,y=80)   #de forma abreviada sin usar una variable Label1

#IMAGEN1
ruta=r"D:\\NUEVO PORTATAIL\\PROGRAMACIÓN\\PYTHON\\EJERCICIO 16 Interfaces gráficas"          #ubicar ruta del archivo
nombre1="schrodinger.png"                                                                     #escribir nombre de imagen y extensión
img_original1=Image.open(os.path.join(ruta,nombre1))                                         #construir la ruta completa de la imagen y abrirla
imagen1=img_original1.resize((50,70), Image.LANCZOS)                                          #redimensionar la imagen con el método de interpolación LANCZOS
img1=ImageTk.PhotoImage(imagen1)                                                              #crear objeto que representa la imagen
Label(fr, image=img1).place(x=50,y=100)                                                       #colocar imagen en el label




#TITULO3
Label(fr,text="Agujeros negros",fg="blue", font=("Times New Roman", 15)).place(x=250,y=50)

#TITULO4
Label(fr,text="Singularidad", fg="red",font=("Times New Roman", 10)).place(x=250,y=80)

#IMAGEN2
nombre2="blackhold.png"
img_original2=Image.open(os.path.join(ruta,nombre2))
imagen2=img_original2.resize((50,70), Image.LANCZOS)
img2=ImageTk.PhotoImage(imagen2)
Label(fr,image=img2).place(x=250,y=100)



#TITULO5
Label(fr,text="Relatividad Especial",fg="blue", font=("Times New Roman",15)).place(x=450,y=50)

#TITULO6
Label(fr,text="Cono de Luz",fg="red",font=("Times New Roman", 10)).place(x=450,y=80)

#IMAGEN3
nombre3="conoluz.png"
img_original3=Image.open(os.path.join(ruta,nombre3))
imagen3=img_original3.resize((50,70),Image.LANCZOS)
img3=ImageTk.PhotoImage(imagen3)
Label(fr,image=img3).place(x=450,y=100)


root.mainloop()