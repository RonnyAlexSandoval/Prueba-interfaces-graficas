from tkinter import *

root=Tk("900x700")
root.title("Formulario")
fr=Frame(root)
fr.pack()


#PRIMERA FILA
label11=Label(fr,text="Nombre: ")
label11.grid(row=0,column=0, sticky="w", padx=10, pady=10)

cuadro11=Entry(fr)
cuadro11.grid(row=0,column=1, padx=10, pady=10)

label12=Label(fr,text="Apellido: ")
label12.grid(row=0,column=2, sticky="w", padx=10, pady=10)

cuadro12=Entry(fr)
cuadro12.grid(row=0,column=3, padx=10, pady=10)

label13=Label(fr,text="Genero: ")
label13.grid(row=0,column=4, sticky="w", padx=10, pady=10)

cuadro13=Entry(fr)
cuadro13.grid(row=0,column=5, padx=10, pady=10)



#SEGUNDA FILA
label21=Label(fr,text="País: ")
label21.grid(row=1,column=0, sticky="w", padx=10, pady=10)

cuadro21=Entry(fr)
cuadro21.grid(row=1,column=1, padx=10, pady=10)

label22=Label(fr,text="Estado: ")
label22.grid(row=1,column=2, sticky="w", padx=10, pady=10)

cuadro22=Entry(fr)
cuadro22.grid(row=1,column=3, padx=10, pady=10)

label23=Label(fr,text="Ciudad: ")
label23.grid(row=1,column=4, sticky="w", padx=10, pady=10)

cuadro23=Entry(fr)
cuadro23.grid(row=1,column=5, padx=10, pady=10)


#TERCERA FILA
label31=Label(fr,text="E-mail: ")
label31.grid(row=2,column=0, sticky="w", padx=10, pady=10)

cuadro31=Entry(fr)
cuadro31.grid(row=2,column=1, padx=10, pady=10)

label32=Label(fr,text="Contraseña: ")
label32.grid(row=2,column=2, sticky="w", padx=10, pady=10)

cuadro32=Entry(fr)
cuadro32.grid(row=2,column=3, padx=10, pady=10)
cuadro32.config(show="*")

label33=Label(fr,text="Repetir contraseña: ")
label33.grid(row=2,column=4, sticky="w", padx=10, pady=10)

cuadro33=Entry(fr)
cuadro33.grid(row=2,column=5, padx=10, pady=10)
cuadro33.config(show="*")


root.mainloop()



#EL mismo formulario anterior sepuede construir con un bucle for
"""
root = Tk()
root.title("Formulario")
fr = Frame(root)
fr.pack()

campos = [
    ("Nombre", "Apellido", "Género"),
    ("País", "Estado", "Ciudad"),
    ("E-mail", "Contraseña", "Repetir contraseña")
]

for i, fila in enumerate(campos):
    for j, etiqueta in enumerate(fila):
        label = Label(fr, text=etiqueta + ": ")
        label.grid(row=i, column=j*2, sticky="w", padx=10, pady=10)

        cuadro = Entry(fr)
        cuadro.grid(row=i, column=j*2+1, padx=10, pady=10)
        if etiqueta == "Contraseña" or etiqueta == "Repetir contraseña":
            cuadro.config(show="*")

root.mainloop()
"""