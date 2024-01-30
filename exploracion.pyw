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
frameSW.grid(row=0, column=0, padx=15, pady=12, ipadx=10, ipady=5)

#---------------------------------------- DERECHA ABAJO-------------------------------------
frameSE=Frame(frameCen,bg="#63FF4E")
frameSE.grid(row=0, column=1, padx=15, pady=12, ipadx=10, ipady=4)





#---------------------------------Hijos Arriba---------------------------------
#----------------------------FRAME3. Hijo IZQUIERDA----------------------------
frame1=Frame(frameNW,bg="red")
frame1.grid(row=0,  column=0, padx=7, pady=12, ipadx=10, ipady=5)

#----------------------------FRAME4. Hijo IZQUIERDA----------------------------
frame2=Frame(frameNW,bg="blue")
frame2.grid(row=0,  column=1, padx=7, pady=12, ipadx=10, ipady=5)

#----------------------------FRAME5 Hijo IZQUIERDA-----------------------------
frame3=Frame(frameNW,bg="red")
frame3.grid(row=1,  column=0, padx=7, pady=12, ipadx=10, ipady=5)

#----------------------------FRAME6 Hijo IZQUIERDA-----------------------------
frame4=Frame(frameNW,bg="blue")
frame4.grid(row=1,  column=1, padx=7, pady=12, ipadx=10, ipady=5)



#--------------------------LABEL1. Titulo. Hijo DERECHA------------------------
label1=Label(frameNE,text="Contenido UNO")
label1.grid(row=0, column=0, padx=5, pady=5, ipadx=5, ipady=5, sticky="nsew")
label1.config(font="Courier", bg="#A4C0CB", relief="groove")

#--------------------------LABEL2. Titulo. Hijo DERECHA-------------------------
label2=Label(frameNE,text="Contenido DOS")
label2.grid(row=0, column=1, padx=5, pady=5, ipadx=5, ipady=5, sticky="nsew")
label2.config(font="Courier", bg="#A4C0CB", relief="groove")

#--------------------------LABEL3. Titulo. Hijo DERECHA-------------------------
label3=Label(frameNE,text="Contenido TRES")
label3.grid(row=0, column=2, padx=5, pady=5, ipadx=5, ipady=5, sticky="nsew")
label3.config(font="Courier", bg="#A4C0CB", relief="groove")

#--------------------------LABEL 4. Texto largo. Hijo DERECHA----------------------------
label4=Label(frameNE,text="Este es el primer contenido largo que incluye saltos de linea")
label4.grid(row=1, column=0, padx=5, pady=5, ipadx=5, ipady=5)
label4.config(font=("Times New Roman",12), bg="#A4C0CB", relief="sunken", wraplength=200)

#--------------------------LABEL 5. Texto largo. Hijo DERECHA-----------------------------
label5=Label(frameNE,text="Este es el segundo contenido largo que incluye saltos de linea")
label5.grid(row=1, column=1, padx=5, pady=5, ipadx=5, ipady=5)
label5.config(font=("Times New Roman",12), bg="#A4C0CB", relief="sunken", wraplength=200)

#--------------------------LABEL 6 Texto largo. Hijo DERECHA-----------------------------
label6=Label(frameNE,text="Este es el tercer contenido largo que incluye saltos de linea")
label6.grid(row=1, column=2, padx=5, pady=5, ipadx=5, ipady=5)
label6.config(font=("Times New Roman",12), bg="#A4C0CB", relief="sunken", wraplength=200)






#------------------------------------Hijos MEDIO------------------------------------------
#------------------------------Hijos izquierda MEDIO Cuadros de texto---------------------
label7=Label(frameSW,text="Nombre", width=10)
label7.grid(row=0,column=0, padx=10, pady=10, ipadx=10, ipady=10)
label7.config(font=("Arial",11), fg="white", bg="#211BA6", relief="ridge", wraplength=200)

label7=Label(frameSW,text="Apellido", width=10)
label7.grid(row=1,column=0, padx=10, pady=10, ipadx=10, ipady=10)
label7.config(font=("Arial",11), fg="white", bg="#211BA6", relief="ridge", wraplength=200)

label7=Label(frameSW,text="Ciudad", width=10)
label7.grid(row=2,column=0, padx=10, pady=10, ipadx=10, ipady=10)
label7.config(font=("Arial",11), fg="white", bg="#211BA6", relief="ridge", wraplength=200)

label7=Label(frameSW,text="Profesión", width=10)
label7.grid(row=3,column=0, padx=10, pady=10, ipadx=10, ipady=10)
label7.config(font=("Arial",11), fg="white", bg="#211BA6", relief="ridge", wraplength=200)

label7=Label(frameSW,text="Entidad", width=10)
label7.grid(row=4,column=0, padx=10, pady=10, ipadx=10, ipady=10)
label7.config(font=("Arial",11), fg="white", bg="#211BA6", relief="ridge", wraplength=200)


#-----------------------------Hijos izquierda MEDIO Cuadros de entrada------------------
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


#------------Definimos Label inferiores para poder usarlos en la función-----------
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


#-----------------------------Hijos MEDIO izquierda Botones------------------------------
def recogeDatos(entrada,salida):
    contenido=entrada.get()
    salida.set(contenido)


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

#--------------------------------------Botón guardar Izquierdo--------------------------

Datos=[]
def guardaDatos(nombre,apellido,ciudad,profesion,entidad):
    datos=[nombre,apellido,ciudad,profesion,entidad]
    for i in datos:
        Datos.append(i)
    frameSW.destroy()
    print(Datos)
    texto1="Nombre"+": "+Datos[0]+'\n'+\
        "Apellido"+": "+Datos[1]+'\n'+\
          "Ciudad"+": "+Datos[2]+'\n'+\
       "profesion"+": "+Datos[3]+'\n'+\
         "Entidad"+": "+Datos[4]
    
    #-------crear nuevo frame para los datos introducidos--------
    frameNewIzq=Frame(frameCen,bg="White")
    frameNewIzq.grid(row=0, column=0, padx=15, pady=12, ipadx=10, ipady=5)

    labelDatos=Label(frameNewIzq,text=texto1, justify="left")
    labelDatos.pack()


botonGuardar1=Button(frameSW, text="Guardar datos", bg="black", fg="white",
                     command=lambda:guardaDatos(
                         textLabelInf1.get(),
                         textLabelInf2.get(),
                         textLabelInf3.get(),
                         textLabelInf4.get(),
                         textLabelInf5.get()))
botonGuardar1.grid(row=5, column="2", padx=5, sticky="nsew")



#------------importar imagenes y redimensionar------------------------------------------
ruta=r"D:\\NUEVO PORTATAIL\\PROGRAMACIÓN\\PYTHON\\EJERCICIO 16 Interfaces gráficas"          #ruta de archivos
nombres=["logopython.png",
         "logojava.png",
         "logojavascript.png",
         "logoHTML.png",
         "logoCSS.png"]
img=[]

for nombre in nombres:
    rutacompleta=Image.open(os.path.join(ruta,nombre))                                       #construir la ruta completa
    imagenOriginal=rutacompleta.resize((30,30), Image.LANCZOS)                               #redimensionar la imagen con el método de interpolación LANCZOS
    imagenRedimen=ImageTk.PhotoImage(imagenOriginal)                                         #crear objeto que representa la imagen
    img.append(imagenRedimen)                                                                #enlistar los objetos


#-----------------hijos MEDIO DERECHA imagenes---------------------------------
img1=Label(frameSE, image=img[0],)
img1.grid(row=0,column=0, padx=15, pady=15)

img2=Label(frameSE, image=img[1],)
img2.grid(row=1,column=0, padx=15, pady=15)

img3=Label(frameSE, image=img[2],)
img3.grid(row=2,column=0, padx=15, pady=15)

img4=Label(frameSE, image=img[3],)
img4.grid(row=3,column=0, padx=15, pady=15)

img5=Label(frameSE, image=img[4],)
img5.grid(row=4,column=0, padx=15, pady=15)

#-------------------------Hijos MEDIO DERECHA Lista de chequeo-----------------------
checkPython=IntVar()
checkJava=IntVar()
checkJavascript=IntVar()
checkHTML=IntVar()
checkCSS=IntVar()

check1=Checkbutton(frameSE,text="Python", justify="left", width=7, anchor="w", 
                   variable=checkPython, onvalue=1, offvalue=0)
check1.grid(row=0, column=1, sticky="w")

check2=Checkbutton(frameSE,text="Java", justify="left", width=7, anchor="w",
                   variable=checkJava, onvalue=2, offvalue=0)
check2.grid(row=1, column=1, sticky="w")

check3=Checkbutton(frameSE,text="JavaScript", justify="left", width=7, anchor="w",
                   variable=checkJavascript, onvalue=3, offvalue=0)
check3.grid(row=2, column=1, sticky="w")

check4=Checkbutton(frameSE,text="HTML", justify="left", width=7, anchor="w",
                   variable=checkHTML, onvalue=4, offvalue=0)
check4.grid(row=3, column=1, sticky="w")

check5=Checkbutton(frameSE,text="CSS", justify="left", width=7, anchor="w",
                   variable=checkCSS, onvalue=5, offvalue=0)
check5.grid(row=4, column=1, sticky="w")


#-------------------------Hijos MEDIO DERECHA Lista de selección--------------------
item=IntVar()
elementos=Listbox(frameSE,selectmode="SINGLE")
elementos.insert( 0,
    "Item 1",
    "Item 2",
    "Item 3",
    "Item 4",     
    "Item 5",
    "Item 6",
    "Item 7",
    "Item 8",
    "Item 9",
    "Item 10",)
elementos.grid(row=0,column=2, rowspan=3, padx=10, pady=10)


#---------------HIJOS derecha MEDIO. Botones radiales-------------------
frameradios=Frame(frameSE)
frameradios.grid(row=3, column=2, rowspan=2)


OptionRadios=IntVar()
radio1=Radiobutton(frameradios,text="Opción Primera", width=14,
                   variable=OptionRadios, value=1, justify="left").pack()

radio2=Radiobutton(frameradios,text="Opción Segunda", width=14,
                   variable=OptionRadios, value=2, justify="left").pack()

radio3=Radiobutton(frameradios,text="Opción Tercera", width=14,
                   variable=OptionRadios, value=3, justify="left").pack()

radio4=Radiobutton(frameradios,text="Opción Cuarta", width=14,
                   variable=OptionRadios, value=4, justify="left").pack()

#------------DICCIONARIOS con opciones, items y elecciones-------------
dicRadio={
        1:"Primera",
        2:"Segunda",
        3:"Tercera",
        4:"Cuarta"
        }

dicLenguaje={
        1:"Python",
        2:"Java",
        3:"Javascript",
        4:"HTML",
        5:"CSS"
        }

dicItem={
        1:"Item 1",
        2:"Item 2",
        3:"Item 3",
        4:"Item 4",
        5:"Item 5",
        6:"Item 6",
        7:"Item 7",
        8:"Item 8",
        9:"Item 9",
        10:"Item 10",
}

radioElec=0
lenguajes=[]
itemSeleccionados=0

def guardaOpciones():
    global radioElec
    global lenguajes
    global itemSeleccionados
    radioElec=OptionRadios.get()
    lenguajes=[checkPython.get(),
               checkJava.get(),
               checkJavascript.get(),
               checkHTML.get(),
               checkCSS.get(),]
    
    itemSeleccionados=elementos.curselection()
    valoritem=itemSeleccionados[0]+1


    texto2="Opción Elegida:"+\
            dicRadio[radioElec]+'\n'+\
            "Items Elegidos: "+dicItem[valoritem]+'\n'
    
    texto3="Lenguajes elegidos: "
    
    for i in lenguajes:
        if i!=0:
            texto3+=dicLenguaje[i]+", "
    texto4=texto2+texto3

    frameSE.destroy()         
           
    #-------crear nuevo frame para los datos introducidos--------
    frameNewIzq=Frame(frameCen,bg="White")
    frameNewIzq.grid(row=1, column=0, padx=15, pady=12, ipadx=10, ipady=5)

    labelDatos=Label(frameNewIzq,text=texto4, justify="left")
    labelDatos.pack()


botonGuardar2=Button(frameSE, text="Guardar opciones", bg="black", fg="white", command=guardaOpciones)
botonGuardar2.grid(row=5, columnspan=3, padx=5, sticky="nsew")


root.mainloop()

