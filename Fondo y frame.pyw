from tkinter import *
import os

fondo=Tk()

ruta_icono=r"D:\\NUEVO PORTATAIL\\PROGRAMACIÓN\\PYTHON\\EJERCICIO 16 Interfaces gráficas"   #la ruta debe ir antecedida de la letra r y las barras invertidas van dobles
nombre_icono="termo1.ico"                               #nombre y extensión del  archivo imagen que se usará en el icono

fondo.title("Titulo principal")                         #Titulo de la ventana
fondo.resizable(True,True)                              #permiso para redimensionar la ventana
fondo.iconbitmap(os.path.join(ruta_icono,nombre_icono)) #busca y asigna ruta completa de la imagen al icono del Tk
fondo.geometry("1050x610")                              #dimensiones por defecto del Tk.
fondo.config(bg="gray")                                 #color del Tk
fondo.config(bd=15,relief="ridge")                      #tamaño y tipo de borde

fr=Frame()                                              #se el frame
fr.pack(side="top", anchor="w")                         #se empaqueta el frame y se ubica según necesidad
#fr.pack(fill="x")                                      #para ocupar todo  el alto del Tk
#fr.pack(fill="y", expand="True")                       #para ocupar todo  el alto del Tk
#fr.pack(fill="both, expand="True")                     #para ocupar todo el Tk
fr.config(bg="brown", width="800", height="500")        #color y dimensiones del frame
fr.config(bd=25, relief="groove")                       #tamaño y tipo de borde
fr.config(cursor="hand2")                               #cursor en el frame

fondo.mainloop()

