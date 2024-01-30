
from tkinter import *
import os
from PIL import Image, ImageTk

#-----------VENTANA-----------------
root = Tk()
root.title("Primera Interfaz")
root.configure(bg="#CEF1FF",padx=10,pady=10)


#---------------------------------------FRAME PADRES----------------------------------------
#--------------------------------------Principales------------------------------------------
frameSup=Frame(root)
frameSup.pack(side="top", fill="none")
frameCen=Frame(root)
frameCen.pack(fill="none")
frameInf=Frame(root)
frameInf.pack(side="bottom",fill="none")


#----------------------------------------IZQUIERDA ARRIBA-----------------------------------
frameNW=Frame(frameSup,bg="yellow")
frameNW.pack(side="left", anchor="n", fill="y", padx=15, pady=12, ipadx=10, ipady=5)

#------------------------------------------DERECHA ARRIBA-----------------------------------
frameNE=Frame(frameSup,bg="yellow")
frameNE.pack(side="left", anchor="n",  fill="none", padx=15, pady=12, ipadx=10, ipady=5)

#----------------------------------------IZQUIERDA ABAJO------------------------------------
frameSW=Frame(frameCen,bg="#63FF4E")
frameSW.pack(side="left", anchor="s", fill="none", padx=15, pady=12, ipadx=10, ipady=5)

#---------------------------------------- DERECHA ABAJO-------------------------------------
frameSE=Frame(frameCen,bg="#63FF4E")
frameSE.pack(side="left", anchor="s", fill="both", padx=15, pady=12, ipadx=10, ipady=4)


textLabelInf1=StringVar()
textLabelInf2=StringVar()
textLabelInf3=StringVar()
textLabelInf4=StringVar()
textLabelInf5=StringVar()

entry1=Entry(frameSW, width=20)
entry1.grid(row=0, column=1, padx=5, pady=10, sticky="nsew")

entry2=Entry(frameSW, width=20)
entry2.grid(row=1, column=1, padx=5, pady=10, sticky="nsew")

entry3=Entry(frameSW, width=20)
entry3.grid(row=2, column=1, padx=5, pady=10, sticky="nsew")

entry4=Entry(frameSW, width=20)
entry4.grid(row=3, column=1, padx=5, pady=10, sticky="nsew")

entry5=Entry(frameSW, width=20)
entry5.grid(row=4, column=1, padx=5, pady=10, sticky="nsew")


#Definimos Label inferiores para poder usarlos en la función
entryInf1=Entry(frameInf, bg="#CEF1FF", textvariable=textLabelInf1)
entryInf1.grid(row=0, column=0)

entryInf2=Entry(frameInf, bg="#CEF1FF", textvariable=textLabelInf2)
entryInf2.grid(row=0, column=1)

entryInf3=Entry(frameInf, bg="#CEF1FF", textvariable=textLabelInf3)
entryInf3.grid(row=0, column=2)

entryInf4=Entry(frameInf, bg="#CEF1FF", textvariable=textLabelInf4)
entryInf4.grid(row=0, column=3)

entryInf5=Entry(frameInf, bg="#CEF1FF", textvariable=textLabelInf5)
entryInf5.grid(row=0, column=4)

def recogeDatos(entrada,salida):
    contenido=entrada.get()
    salida.set(contenido)

#-----------------------------Hijos MEDIO izquierda Botones------------------------------
boton1=Button(frameSW, text="Agregar", bg="#00D9D9", command=lambda:recogeDatos(entry1,textLabelInf1))
boton1.grid(row=0, column=2, padx=5, pady=10, sticky="nsew")
boton1.flash()

boton2=Button(frameSW, text="Agregar", bg="#00D9D9", command=lambda:recogeDatos(entry2,textLabelInf2))
boton2.grid(row=1, column=2, padx=5, pady=10, sticky="nsew")
boton2.flash()

boton3=Button(frameSW,  text="Agregar", bg="#00D9D9", command=lambda:recogeDatos(entry3,textLabelInf3))
boton3.grid(row=2, column=2, padx=5, pady=10, sticky="nsew")
boton3.flash()

boton4=Button(frameSW,  text="Agregar", bg="#00D9D9", command=lambda:recogeDatos(entry4,textLabelInf4))
boton4.grid(row=3, column=2, padx=5, pady=10, sticky="nsew")
boton4.flash()

boton5=Button(frameSW,  text="Agregar", bg="#00D9D9", command=lambda:recogeDatos(entry5, textLabelInf5))
boton5.grid(row=4, column=2, padx=5, pady=10, sticky="nsew")
boton5.flash()

botonGuardar1=Button(frameSW, text="Guardar datos", bg="black", fg="white")
botonGuardar1.grid(row=5, column="2", padx=5, sticky="nsew")


root.mainloop()
