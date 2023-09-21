from tkinter import *
from tkinter import messagebox
from os import remove

lista=[]  
def abrirventana():    
    global cantidad_gasto
    global nombre_gasto
    global ventGastos
    ventGastos=Toplevel()
    ventGastos.title("Calculo de Gastos")
    ventGastos.geometry("800x520+250+110")
    ventGastos.overrideredirect(True)
    ventGastos.configure(bg=colorMedioOscuro)
    ventGastos.focus()
    listaGastos()
    iniciarArchivo()
    cargar()
    ventGastos.grab_set()
    vContenido()

def calcular():
    global cant_gasto_obtenida
    global presupuestoObtenido
    cant_gasto_obtenida=cantidad_gasto.get()
    nom_gasto_obtenido=nombre_gasto.get()
    presupuestoObtenido=presupuesto.get()
    if nom_gasto_obtenido == '' or cant_gasto_obtenida == 0:
        messagebox.showerror('Error','Debe ingresar un Gasto y su valor')
    else:
        if presupuestoObtenido>=cant_gasto_obtenida:
            presupuesto.set(presupuesto.get()-cant_gasto_obtenida)
            restante2=Label(ventGastos,textvariable=presupuesto,font=("ARIAL",12),bg=colorMedioClaro,fg=colorFondoOscuro).place(x=690,y=110)
            lista.append(nom_gasto_obtenido+"$"+str(cant_gasto_obtenida)+"$"+str(presupuestoObtenido)+"$")
            escribirGasto()
            nombre_gasto.set("")
            cantidad_gasto.set("")
            listaGastos()         
        else:
            messagebox.showerror("Error", "El gasto excede el presupuesto exitente Ya no puede gastar")   

def cargar():
    archivo=open("gastos.txt","r")
    linea=archivo.readline()
    if linea:
        while linea:
            if linea[-1]=='\n':
                linea=linea[:-1]
            lista.append(linea)
            linea=archivo.readline()
    archivo.close()

def cerrar():
    ventGastos.destroy()
    remove("gastos.txt")
    lista.clear()

def cerrarPrincipal():
    ventana.destroy()

def escribirGasto():
    archivo=open("gastos.txt","w")
    lista.sort()
    for elemento in lista:
        archivo.write(elemento+"\n")
    archivo.close()

def iniciarArchivo():
    archivo=open("gastos.txt","a")
    archivo.close()

def listaGastos():
    r=Text(ventGastos,width=43,height=19)
    lista.sort()    
    for elemento in lista:
        arreglo=elemento.split("$")
        r.insert(INSERT,arreglo[0]+"\t\t\t"+arreglo[1]+"\t\t\t""\n")
    r.place(x=390,y=150)
    r.config(state=DISABLED,bg=colorMedioClaro,fg=colorFondoOscuro,font=("arial",12))

def validar():    
    presupuestoObtenido=presupuesto.get()
    if presupuestoObtenido>0:
        abrirventana()
    else:
        messagebox.showerror("Error","El presupuesto debe ser mayor a cero")

def vContenido():
    global cantidad_gasto
    global nombre_gasto
    nombre_gasto=StringVar()
    cantidad_gasto=IntVar()
    rt=cantidad_gasto.get()
    presupuestoObtenido=presupuesto.get()
    R=presupuestoObtenido-rt    
    e_gastos=Label(ventGastos,text="CONTROL DE GASTOS",font=("ARIAL BLACK",20),bg=colorMedioOscuro,fg=colorClaroAmarillo).place(x=260,y=5)

    #ingreso de gastos
    e_ig=Label(ventGastos,text="Ingresar Gasto",font=("calibri",18),bg=colorClaroAmarillo,fg=colorFondoOscuro).place(x=110,y=60)
    e_g=Label(ventGastos,text="GASTO:",font=("arial",16),bg=colorMedioOscuro,fg=colorFondoOscuro).place(x=10,y=115)
    c_g=Entry(ventGastos,textvariable=nombre_gasto,bg=colorClaroAmarillo,fg=colorFondoOscuro,width=31,font=("rial",16)).place(x=10,y=140)
    e_cg=Label(ventGastos,text="CANTIDAD:",font=("rial",16),bg=colorMedioOscuro,fg=colorFondoOscuro).place(x=10,y=182)
    c_cg=Entry(ventGastos,textvariable=cantidad_gasto,bg=colorClaroAmarillo,fg=colorFondoOscuro,width=31,font=("rial",16)).place(x=10,y=210)
    btn_agregar_gasto=Button(ventGastos,text="INGRESAR GASTO",font=("ARIAL"),command=calcular,bg=colorFondoOscuro,fg=colorLetra,width=40).place(x=10,y=250)
    btn_salir=Button(ventGastos,text="SALIR",font=("ARIAL"),command=cerrar,bg=colorFondoOscuro,fg=colorLetra,width=40).place(x=10,y=300)    
    
    #Listado de gastos
    e_lg=Label(ventGastos,text="Listado de Gastos",font=("calibri",18),bg=colorClaroAmarillo,fg=colorFondoOscuro).place(x=490,y=60)
    framePresupuesto=Frame(ventGastos,bg=colorMedioClaro,width="180",height="38").place(x=390,y=105)    
    prp=Label(ventGastos,text="Q",font=("ARIAL"),bg=colorMedioClaro,fg=colorFondoOscuro).place(x=495,y=110)
    prp1=Label(ventGastos,text=presupuestoObtenido,font=("ARIAL"),bg=colorMedioClaro,fg=colorFondoOscuro).place(x=510,y=110)
    prp2=Label(ventGastos,text="Presupuesto",font=("ARIAL"),bg=colorMedioClaro,fg=colorFondoOscuro).place(x=400,y=110)
    framerestante=Frame(ventGastos,bg=colorMedioClaro,width="180",height="38").place(x=590,y=105)    
    restante=Label(ventGastos,text="Q",font=("ARIAL",12),bg=colorMedioClaro,fg=colorFondoOscuro).place(x=675,y=110)
    restante3=Label(ventGastos,text="Restante",font=("ARIAL",12),bg=colorMedioClaro,fg=colorFondoOscuro).place(x=600,y=110)  

#-------------------------------------------Ventana Principal--------------------------------------------------
ventana=Tk()
ventana.title("App Presupuesto by Markos Sanchez")
ventana.geometry("1000x650+150+10")
colorFondoOscuro="#581845"
colorFondoMedio="#900C3F"
colorMedioOscuro="#C70039"
colorMedioClaro="#FF5733"
colorClaroAmarillo="#FFC300"
colorLetra="#DAF7A6"
ventana.configure(bg=colorFondoMedio)
ventana.resizable(0,0)
#variables
resultado=IntVar()
presupuesto=IntVar()
e_titulo=Label(ventana,text="INGRESE SU PRESUPUESTO",font=("Arial BLACK",26),bg=colorFondoMedio,fg=colorClaroAmarillo).place(x=270,y=150)
frame=Frame(ventana,bg=colorMedioOscuro,width="700",height="150").place(x=160,y=200)
caja_presupuesto=Entry(ventana,textvariable=presupuesto,width="51",font=("GOTHAM",18),bg=colorClaroAmarillo).place(x=179,y=220)
boton=Button(ventana,text="INICIAR",bg=colorFondoOscuro,fg=colorLetra,width="73",font=("ARIAL"),command=validar).place(x=179,y=260)
boton=Button(ventana,text="SALIR",bg=colorFondoOscuro,fg=colorLetra,width="73",font=("ARIAL"),command=cerrarPrincipal).place(x=179,y=300)


ventana.mainloop()
