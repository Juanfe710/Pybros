def directorio_usuario_sesion():
    """"
    lee tipo, nombre, nombre usuario y contraseña del archivo txt
    :return: Lista con los dicionarios de cada usuario
    """
    archivo = open('Datos/usuarios.txt', 'r', encoding="utf-8")
    lineas = archivo.readlines()
    archivo.close()

    datos_completos=[]
    for linea in lineas:
        datos = linea.split(';')
        dato_usuario={}
        dato_usuario.setdefault(datos[0], datos[1])    
        dato_usuario.setdefault(datos[2], datos[3])
        dato_usuario.setdefault("libro1", datos[4])
        dato_usuario.setdefault("libro2", datos[5])
        dato_usuario.setdefault("libro3", datos[6])
        datos_completos.append(dato_usuario) 

    return datos_completos

def directorio_usuario_registro():
    """"
    lee tipo, nombre, nombre usuario y contraseña del archivo txt
    :return: Lista con los nombres de los usuarios
    """
    archivo = open('Datos/usuarios.txt', 'r', encoding="utf-8")
    lineas = archivo.readlines()
    archivo.close()

    n_usuarios=[]
    for linea in lineas:
        datos = linea.split(';')
        n_usuarios.append((datos[2]).lower())

    return n_usuarios

def GUI_inicio():
    """
    Interfaz grafica que permite seleccionar al usuario si ingresar o registrarse
    :return NONE
    """
    import tkinter as tk
    from tkinter import ttk
    from tkinter import PhotoImage
    ventana = tk.Tk()
    ventana.title("Ingreso Pybros")
    ventana.geometry('800x400')
    imagen_fondo=PhotoImage(file="Iconos_y_fondos/inicio.png")
    fondo=tk.Label(ventana, image=imagen_fondo)
    fondo.place(x=0, y=0)

    imagen_sesion=PhotoImage(file = "Iconos_y_fondos/sesion.png")
    boton_sesion = tk.Button(ventana, image = imagen_sesion, relief = 'flat', bd = 0, highlightthickness=0, command=lambda: cambio_a_ingreso(ventana))                             
    boton_sesion.place(x = 160, y = 310)

    imagen_registro=PhotoImage(file = "Iconos_y_fondos/registro.png")
    boton_registro = tk.Button(ventana, image = imagen_registro, relief = 'flat', bd = 0, highlightthickness=0, command=lambda: cambio_a_registro(ventana))                             
    boton_registro.place(x = 420, y = 310)

    ventana.mainloop()
    return

def cambio_a_ingreso(ventana):
    """
    Elimina la ventana actual y abre la descrita
    :param Tk Ventana de la interfaz gráfica
    """
    ventana.destroy()
    GUI_ingreso()

def GUI_ingreso():

    """
    Interfaz Grafica que permite seleccionar el tipo de usuario
    :return NONE
    """
    import tkinter as tk
    from tkinter import ttk
    from tkinter import PhotoImage
    ventana = tk.Tk()
    ventana.title("Biblioteca - Ingreso")
    ventana.geometry('800x550')
    imagen_inicio=PhotoImage(file="Iconos_y_fondos/inicio.png")
    fondo=tk.Label(ventana, image=imagen_inicio)
    fondo.place(x=0, y=0)
    
    label_1 = tk.Label(ventana, fg="black", bg="white", font=("DEAR SUNSHINE", 20), text='Tipo Usuario', justify="left", relief="flat")
    label_1.place(x = 100, y = 310)
    
    combo_buscar = ttk.Combobox(ventana)
    combo_buscar['values'] = ('Usuario', 'Administrador')
    combo_buscar['font'] = ("Arial Black", 15)
    combo_buscar['foreground'] = ("purple")
    combo_buscar.current(0)
    combo_buscar.place(x = 330, y = 310)

    label_2 = tk.Label(ventana, fg="black", bg="white", font=("DEAR SUNSHINE", 20), text='Nombre Usuario', justify="left", relief="flat")
    label_2.place(x = 100, y = 360)

    ent_usuario = tk.Entry(ventana, font=("Calibri 20"), relief="sunken")
    ent_usuario.place(x = 330, y = 360)

    label_3 = tk.Label(ventana, fg="black", bg="white", font=("DEAR SUNSHINE", 20), text='Contraseña', justify="left", relief="flat")
    label_3.place(x = 100, y = 410)

    ent_contraseña = tk.Entry(ventana, font=("Calibri 20"), relief="sunken", show='*')
    ent_contraseña.place(x = 330, y = 410)
    
    imagen_ingresar=PhotoImage(file = "Iconos_y_fondos/ingresar.png")
    boton_buscar = tk.Button(ventana, image = imagen_ingresar, relief = 'flat', bd = 0, highlightthickness=0, command=lambda: ingresar(combo_buscar.get(), ent_usuario.get(), ent_contraseña.get(), ventana))                             
    boton_buscar.place(x = 280, y = 460)

    imagen_volver=PhotoImage(file = "Iconos_y_fondos/volver.png")
    boton_volver = tk.Button(ventana, image = imagen_volver, relief = 'flat', bd = 0, highlightthickness=0, command= lambda: volver(ventana))
    boton_volver.place(x = 14, y = 470)

    ventana.mainloop()
    return

def ingresar(tipo_usuario, nombre_usuario, contraseña, ventana):
    """
    Determina si el usuario puede ingresar o no
    :param str tipo_usuario clasifica el usuario
    :param str nombre_usuario entrada puesta por el usuario
    :param str contraseña entrada clave para ingresar puesta por el usuario
    :param Tk ventana interfaz grafica
    """
    from tkinter import messagebox

    datos_usuarios=directorio_usuario_sesion()

    contador=0
    u_ingreso=0
    tipo=0

    biblioteca = leer_libros()

    for elemento in datos_usuarios:
        if tipo_usuario in elemento:
            if nombre_usuario in elemento:
                if contraseña==elemento[nombre_usuario]:
                    cuenta=elemento[tipo_usuario]
                    if tipo_usuario=='Usuario':
                        ventana.destroy()
                        GUI_usuario(biblioteca, cuenta)
                    elif tipo_usuario=='Administrador':
                        ventana.destroy()
                        GUI_administrador(biblioteca, cuenta) 
                    u_ingreso+=1
                    break
                else:
                    messagebox.showerror(message="Contraseña incorrecta", title="Error contraseña")
                    u_ingreso+=1
                    break
            else:
                contador+=1
        else:
            tipo+=1

    if contador>0 and u_ingreso==0:
        messagebox.showerror(message="Usuario no registrado", title="Error usuario")                
    elif tipo>0 and u_ingreso==0:
        messagebox.showerror(message="Tipo de usuario incorrecto", title="Error tipo")     

def cambio_a_registro(ventana):
    """
    Elimina la ventana actual y abre la descrita
    :param Tk Ventana de la interfaz gráfica
    """
    ventana.destroy()
    GUI_registro()

def GUI_registro():

    """
    Interfaz Grafica que permite el registro del usuario
    """

    import tkinter as tk
    from tkinter import ttk
    from tkinter import PhotoImage
    ventana = tk.Tk()
    ventana.title("Registro Pybros")
    ventana.geometry('590x560')
    imagen_fondo_registro=PhotoImage(file="Iconos_y_fondos/fondo_registro.png")
    fondo=tk.Label(ventana, image=imagen_fondo_registro)
    fondo.place(x=0, y=0)

    label_1 = tk.Label(ventana, fg="black", bg="white", font=("DEAR SUNSHINE", 20), text='Nombre y apellido', justify="left", relief="flat")
    label_1.place(x = 20, y = 150)

    ent_nombre = tk.Entry(ventana, font=("Calibri 20"), relief="sunken")
    ent_nombre.place(x = 270, y = 150)    

    label_2 = tk.Label(ventana, fg="black", bg="white", font=("DEAR SUNSHINE", 20), text='Nombre Usuario', justify="left", relief="flat")
    label_2.place(x = 20, y = 240)

    ent_usuario = tk.Entry(ventana, font=("Calibri 20"), relief="sunken")
    ent_usuario.place(x = 270, y = 240)   

    label_3 = tk.Label(ventana, fg="black", bg="white", font=("DEAR SUNSHINE", 20), text='Contraseña', justify="left", relief="flat")
    label_3.place(x = 20, y = 330)

    ent_contraseña = tk.Entry(ventana, font=("Calibri 20"), relief="sunken")
    ent_contraseña.place(x = 270, y = 330) 

    imagen_completo_registro=PhotoImage(file = "Iconos_y_fondos/completo_registro.png")
    boton_completo_registro = tk.Button(ventana, image = imagen_completo_registro, relief = 'flat', bd = 0, highlightthickness=0, command=lambda :registrar(ent_nombre.get(),ent_usuario.get(),ent_contraseña.get(), ventana))                             
    boton_completo_registro.place(x = 205, y = 400)

    imagen_volver=PhotoImage(file = "Iconos_y_fondos/volver.png")
    boton_volver = tk.Button(ventana, image = imagen_volver, relief = 'flat', bd = 0, highlightthickness=0, command= lambda: volver(ventana))
    boton_volver.place(x = 18, y = 20)

    ventana.mainloop()

def registrar(nombre_completo,nombre_usuario,contraseña, ventana):
    """
    Determina si el usuario puede queda registrado o no
    :param str nombre_completo entrada de los datos del usuario
    :param str nombre_usuario entrada del nombre que eligio el usuario
    :param str contraseña entrada clave para que usuario pueda ingresar
    :param Tk ventana interfaz grafica
    """
    from tkinter import messagebox

    usuarios=directorio_usuario_registro()
    contador=0
    
    for i in range(len(usuarios)):
        if nombre_usuario.lower()==usuarios[i]:
            contador+=1
    
    signo=0
    minuscula=0
    mayuscula=0
    numero=0

    if nombre_completo=='' or nombre_usuario=='' or contraseña=='':
        messagebox.showerror(message="Registre todos los campos requeridos", title="Datos incompletos")
    else:
        if contador>0:
            messagebox.showerror(message="Nombre de usuario ya registrado", title="Error nombre usuario") 
        else:
            for i in range(len(contraseña)):
                if ord(contraseña[i])>=33 and ord(contraseña[i])<=47:
                    signo+=1
                if ord(contraseña[i])>=65 and ord(contraseña[i])<=90:
                    mayuscula+=1
                if ord(contraseña[i])>=97 and ord(contraseña[i])<=122:
                    minuscula+=1
                if ord(contraseña[i])>=48 and ord(contraseña[i])<=57:
                    numero+=1
                            
            if signo==0:            
                messagebox.showerror(message="La contraseña debe contener alguno de estos signos: ! ' # $ % & * + , - . / ", title="Error contraseña")
            elif mayuscula==0 or minuscula==0:
                messagebox.showerror(message="La contraseña debe alternar entre mayusculas y minusculas ", title="Error contraseña")
            elif numero==0:
                messagebox.showerror(message="La contraseña debe contener un número", title="Error contraseña")
            else:
                archivo=open("Datos/usuarios.txt", "a+", encoding="utf-8") 
                archivo.write("\nUsuario;" + str(nombre_completo) + ";" + str(nombre_usuario) +";"+ str(contraseña) + ";")
                archivo.close()

                messagebox.showinfo(message="Registro exitoso, disfrute ahora de la plataforma de Pybros ", title="Registro completo")
                ventana.destroy()
                GUI_inicio()

def leer_libros():
    
    """
    lee los libros y crea listas segun las categorias, ademas de clasificar los datos individuales de los textos
    :return list categorias: Por catagoria tiene todos los libros del programa
    """

    from io import open 
    matematicas=[]
    areas_practicas=[]
    fisica=[]
    ciencias_naturales=[]      

    libros=["Datos/matematicas.txt", "Datos/areas_practicas.txt","Datos/fisica.txt","Datos/ciencias_naturales.txt"]
    categorias=[matematicas, areas_practicas, fisica, ciencias_naturales]

    for i in range(len(libros)):
        archivo=open(libros[i],"r",encoding="utf-8") 
        lineas = archivo.readlines()
        archivo.close()

        for linea in lineas:
            campos = linea.split(";")
            libro = {"codigo":campos[0], "autor":campos[1], "fecha":campos[2], "titulo":campos[3], "lugar":campos[4], "editorial":campos[5], "cantidad":campos[6], "cita":campos[7], "link_img":campos[8]}
            categorias[i].append(libro)

    return categorias    

def GUI_administrador(biblioteca, cuenta):

    """
    Interfaz Grafica que permite seleccionar que buscar
    :param list biblioteca: Datos de los libros
    :param str cuenta: Nombre completo del administrador
    """

    import tkinter as tk
    from tkinter import ttk
    from tkinter import PhotoImage
    ventana = tk.Tk()
    ventana.title("Biblioteca - Administrador: " + cuenta)
    ventana.geometry('1200x650')
    imagen_fondo=PhotoImage(file="Iconos_y_fondos/fondo.png")
    fondo=tk.Label(ventana, image=imagen_fondo)
    fondo.place(x=0, y=0)

    label_1 = tk.Label(ventana, font= ("Arial 30"), text = "Bienvenido a PYBROS", justify = "center", relief = "flat", bg="white")
    label_1.place(x = 400, y = 2)
    
    label_2 = tk.Label(ventana, font= ("Calibri 20"), text = 'Criterio :', justify = "left", relief = "flat", bg="white")
    label_2.place(x = 320, y = 70)

    combo_buscar = ttk.Combobox(ventana)
    combo_buscar['values'] = ('Materia', 'Autor', 'Título')
    combo_buscar['font'] = ("Calibri 20")
    combo_buscar.current(0)
    combo_buscar.place(x = 440, y = 70)

    ent_texto = tk.Entry(ventana, font = ("Calibri 20"), relief = "sunken")
    ent_texto.place(x = 440, y = 120)

    label_codigo=tk.Listbox(ventana, font=('Arial bold', 12), width=5, height=10)
    label_codigo.place(x = 18, y = 250)

    label_autor=tk.Listbox(ventana, font=('Arial bold', 12), width=37, height=10)
    label_autor.place(x = 63, y = 250)

    label_titulo=tk.Listbox(ventana, font=('Arial bold', 12), width=50, height=10)
    label_titulo.place(x = 396, y = 250)

    label_fecha=tk.Listbox(ventana, font=('Arial bold', 12), width=5, height=10)
    label_fecha.place(x = 846, y = 250)

    label_lugar=tk.Listbox(ventana, font=('Arial bold', 12), width=10, height=10)
    label_lugar.place(x = 891, y = 250)

    label_editorial=tk.Listbox(ventana, font=('Arial bold', 12), width=22, height=10)
    label_editorial.place(x = 981, y = 250)

    label_cantidad=tk.Listbox(ventana, font=('Arial bold', 12), width=3, height=10)
    label_cantidad.place(x = 1179, y = 250)

    imagen_buscar=PhotoImage(file = "Iconos_y_fondos/buscar.png")
    boton_buscar = tk.Button(ventana, image = imagen_buscar, relief = 'flat', bd = 0, highlightthickness=0, command = lambda:buscar_administrador(combo_buscar.get(), ent_texto.get(), biblioteca, label_codigo, label_autor, label_titulo, label_fecha, label_lugar, label_editorial, label_cantidad))
    boton_buscar.place(x = 225, y = 170)
    
    ent_codigo = tk.Entry(ventana, font = ("Calibri 20"), relief = "sunken")
    ent_codigo.place(x = 455, y = 575)

    imagen_cambiar1=PhotoImage(file = "Iconos_y_fondos/cambiar.png")
    boton_cambiar1 = tk.Button(ventana, image = imagen_cambiar1, relief = 'flat', bd = 0, highlightthickness=0, command = lambda: cambiar_administrador(ent_codigo.get(), biblioteca, ventana))
    boton_cambiar1.place(x=795, y=575)
        
    imagen_limpiar=PhotoImage(file = "Iconos_y_fondos/limpiar.png")
    boton_limpiar = tk.Button(ventana, image = imagen_limpiar, relief = 'flat', bd = 0, highlightthickness=0, command = lambda:limpiar_administrador(ent_texto, label_codigo, label_autor, label_titulo, label_fecha, label_lugar, label_editorial, label_cantidad))
    boton_limpiar.place(x = 795, y = 170)

    imagen_volver=PhotoImage(file = "Iconos_y_fondos/volver.png")
    boton_volver = tk.Button(ventana, image = imagen_volver, relief = 'flat', bd = 0, highlightthickness=0, command = lambda:volver(ventana))
    boton_volver.place(x = 18, y = 14)

    ventana.mainloop()
    return

def buscar_administrador(criterio, patron, biblioteca, label_codigo, label_autor, label_titulo, label_fecha, label_lugar, label_editorial, label_cantidad):

    """
    Selecciona que información presentar al ejecutor
    :param str criterio: forma en la que se buscaran los datos
    :param str patron: dato buscado
    :param list biblioteca: Datos de los libros
    :param Tk label_codigo: Espacio destinado a la presentacion de los codigos
    :param Tk label_autor: Espacio destinado a la presentacion de los autores 
    :param Tk label_titulo: Espacio destinado a la presentacion de los titulos 
    :param Tk label_fechas: Espacio destinado a la presentacion de los fechas
    :param Tk label_lugar: Espacio destinado a la presentacion de los lugares de publicacion de los libros
    :param Tk label_editorial: Espacio destinado a la presentacion de las editoriales
    :param Tk label_cantidad: Espacio destinado a la presentacion de las cantidades disponibles
    """
    x=0
    label_codigo.lift()
    label_autor.lift()
    label_titulo.lift()
    label_fecha.lift()
    label_lugar.lift()
    label_editorial.lift()
    label_cantidad.lift()

    label_codigo.delete(0,'end')
    label_autor.delete(0,'end')
    label_titulo.delete(0,'end')
    label_fecha.delete(0,'end')
    label_lugar.delete(0,'end')
    label_editorial.delete(0,'end')
    label_cantidad.delete(0,'end')

    if criterio == 'Materia':
        if patron=='Matemáticas':
            i=0
            for l in biblioteca[0]:
                i+=1
                label_codigo.insert(i, l["codigo"])
                label_autor.insert(i, l["autor"])
                label_titulo.insert(i, l["titulo"]) 
                label_fecha.insert(i, l["fecha"])
                label_lugar.insert(i, l["lugar"])
                label_editorial.insert(i, l["editorial"])
                label_cantidad.insert(i, l["cantidad"])                
        elif patron=='Áreas prácticas':
            i=0
            for l in biblioteca[1]:
                i+=1
                label_codigo.insert(i, l["codigo"])
                label_autor.insert(i, l["autor"])
                label_titulo.insert(i, l["titulo"]) 
                label_fecha.insert(i, l["fecha"])
                label_lugar.insert(i, l["lugar"])
                label_editorial.insert(i, l["editorial"])
                label_cantidad.insert(i, l["cantidad"]) 
        elif patron=='Física':
            i=0
            for l in biblioteca[2]:
                i+=1
                label_codigo.insert(i, l["codigo"])
                label_autor.insert(i, l["autor"])
                label_titulo.insert(i, l["titulo"]) 
                label_fecha.insert(i, l["fecha"])
                label_lugar.insert(i, l["lugar"])
                label_editorial.insert(i, l["editorial"])
                label_cantidad.insert(i, l["cantidad"]) 
        elif patron=='Ciencias naturales':
            i=0
            for l in biblioteca[3]:
                i+=1
                label_codigo.insert(i, l["codigo"])
                label_autor.insert(i, l["autor"])
                label_titulo.insert(i, l["titulo"]) 
                label_fecha.insert(i, l["fecha"])
                label_lugar.insert(i, l["lugar"])
                label_editorial.insert(i, l["editorial"])
                label_cantidad.insert(i, l["cantidad"]) 
        else:
            from tkinter import messagebox
            messagebox.showinfo(message="Categoría no encontrada", title="INFORME")   
    elif criterio == 'Autor':
        i=0      
        for elemento in biblioteca:
            for l in elemento:
                if patron in l["autor"]:
                    i+=1
                    label_codigo.insert(i, l["codigo"])
                    label_autor.insert(i, l["autor"])
                    label_titulo.insert(i, l["titulo"]) 
                    label_fecha.insert(i, l["fecha"])
                    label_lugar.insert(i, l["lugar"])
                    label_editorial.insert(i, l["editorial"])
                    label_cantidad.insert(i, l["cantidad"]) 
                    x+=1
        if x==0 or patron=='':
            label_codigo.delete(0,'end')
            label_autor.delete(0,'end')
            label_titulo.delete(0,'end')
            label_fecha.delete(0,'end')
            label_lugar.delete(0,'end')
            label_editorial.delete(0,'end')
            label_cantidad.delete(0,'end')
            from tkinter import messagebox
            messagebox.showinfo(message="Autor no encontrado", title="INFORME")
    elif criterio == 'Título':
        i=0
        for elemento in biblioteca:
            for l in elemento:
                if patron in l["titulo"]:
                    i+=1
                    label_codigo.insert(i, l["codigo"])
                    label_autor.insert(i, l["autor"])
                    label_titulo.insert(i, l["titulo"]) 
                    label_fecha.insert(i, l["fecha"])
                    label_lugar.insert(i, l["lugar"])
                    label_editorial.insert(i, l["editorial"])
                    label_cantidad.insert(i, l["cantidad"]) 
                    x+=1
        if x==0 or patron=='':
            label_codigo.delete(0,'end')
            label_autor.delete(0,'end')
            label_titulo.delete(0,'end')
            label_fecha.delete(0,'end')
            label_lugar.delete(0,'end')
            label_editorial.delete(0,'end')
            label_cantidad.delete(0,'end')
            from tkinter import messagebox
            messagebox.showinfo(message="Libro no encontrado", title="INFORME")

def cambiar_administrador(entrada, biblioteca, ventana):
    
    """
    Permite cambiar la informacion desde los archivos de texto
    :param str entrada: codigo del libro a cambiar
    :param list biblitoca: contiene todos los libros del programa
    :param Tk ventana: interfaz grafica
    """     
    correcto = False
    for elemento in biblioteca:
        for l in elemento:
            if str(entrada) in l["codigo"]:
                correcto = True
                break
                
    if correcto:
        ventana.destroy()
        GUI_cambio_seleccion(entrada, biblioteca)
    else:
        from tkinter import messagebox
        messagebox.showinfo(message = 'Libro no encontrado', title = 'ADVERTENCIA')
    
def GUI_cambio_seleccion(entrada, biblioteca):
    """
    Interfaz para cambiar los datos del libro
    :param str entrada: codigo del libro a cambiar
    :param list biblitoca: contiene todos los libros del programa
    """
    import tkinter as tk
    from tkinter import ttk
    from tkinter import PhotoImage
    
    ventana = tk.Tk()
    ventana.geometry('400x585')
    ventana.title('Realizar cambios - Administrador')
    imagen_fondo=PhotoImage(file="Iconos_y_fondos/fondo_cambio.png")
    fondo=tk.Label(ventana, image=imagen_fondo)
    fondo.place(x=0, y=0)
    
    label_titulo = tk.Label(ventana, text = 'CAMBIOS', font = ('Arial 20'), justify = 'center', relief = 'flat', bg = 'white')
    label_titulo.place(x = 150, y = 50)
    
    label_subtitulo = tk.Label(ventana, font= ("Calibri 20"), text = 'Elija el dato a cambiar :', justify = "center", relief = "flat", bg="white")
    label_subtitulo.place(x = 100, y = 200)
    
    imagen_año = PhotoImage(file = 'Iconos_y_fondos/año.png')
    boton_año = tk.Button(ventana, image = imagen_año, relief = 'flat', bd = 0, highlightthickness=0, command = lambda: GUI_cambiar_ano(biblioteca,entrada, ventana))
    boton_año.place(x=150, y=300)
    
    imagen_codigo = PhotoImage(file = 'Iconos_y_fondos/codigo.png')
    boton_codigo = tk.Button(ventana, image = imagen_codigo, relief = 'flat', bd = 0, highlightthickness=0, command = lambda: GUI_cambiar_co(biblioteca, entrada, ventana))
    boton_codigo.place(x=150, y=400)
    
    imagen_cantidad = PhotoImage(file = 'Iconos_y_fondos/cantidad.png')
    boton_cantidad = tk.Button(ventana, image = imagen_cantidad, relief = 'flat', bd = 0, highlightthickness=0, command = lambda: GUI_cambiar_ca(biblioteca, entrada, ventana))
    boton_cantidad.place(x=150, y=500)
    
    ventana.mainloop()
   
def GUI_cambiar_ano(biblioteca, codigo_li,ventana):
    """
    Interfaz para cambiar el año del libro seleccionado
    :param list biblioteca: contiene todos los libros del programa
    :param str codigo_li: codigo del libro a cambiar
    :param Tk ventana: interfaz grafica
    """
    ventana.destroy()
    import tkinter as tk
    from tkinter import ttk
    from tkinter import PhotoImage
    
    ventana = tk.Tk()
    ventana.geometry('500x400')
    ventana.title('Realizar cambios - Administrador')
    imagen_fondo=PhotoImage(file="Iconos_y_fondos/fondo.png")
    fondo=tk.Label(ventana, image=imagen_fondo)
    fondo.place(x=0, y=0)
    
    label_cambio = tk.Label(ventana, font = ("Calibri 20"), text = "Ingrese el nuevo valor", justify = "center", relief = "flat", bg = "white")
    label_cambio.place(x = 125, y = 50)
    
    ent_cambio = tk.Entry(ventana, font = ("Calibri 20"), relief = "sunken")
    ent_cambio.place(x = 125, y = 200)
    
    imagen_cambio = PhotoImage(file = 'Iconos_y_fondos/cambiar.png')
    boton_cambio = tk.Button(ventana, image = imagen_cambio, relief = 'flat', bd = 0, highlightthickness=0, command = lambda:cambio_archivo_ano(ventana, biblioteca, ent_cambio.get(), codigo_li))
    boton_cambio.place(x = 125, y = 300)
    
    ventana.mainloop()
      
def cambio_archivo_ano(ventana, biblioteca, entrada, codigo_li):
    """
    Permite cambiar el año del libro seleccionado
    :param Tk ventana: interfaz grafica
    :param list biblioteca: contiene todos los libros del programa
    :param str entrada: dato por el cual se va a cambiar
    :param str codigo_li: codigo del libro a cambiar
    """
    for elemento in range(len(biblioteca)):
        for l in biblioteca[elemento]:
            if l['codigo'] == codigo_li:
                l['fecha'] = entrada
                change_archivo(elemento, l)
                break
    ventana.destroy()
    
def GUI_cambiar_co(biblioteca, codigo_li, ventana):
    """
    Interfaz para cambiar el codigo del libro seleccionado
    :param Tk ventana: interfaz grafica
    :param list biblioteca: contiene todos los libros del programa
    :param str codigo_li: codigo del libro a cambiar
    """
    ventana.destroy()
    import tkinter as tk
    from tkinter import ttk
    from tkinter import PhotoImage
    
    ventana = tk.Tk()
    ventana.geometry('500x400')
    ventana.title('Realizar cambios - Administrador')
    imagen_fondo=PhotoImage(file="Iconos_y_fondos/fondo.png")
    fondo=tk.Label(ventana, image=imagen_fondo)
    fondo.place(x=0, y=0)
    
    label_cambio = tk.Label(ventana, font = ("Calibri 20"), text = "Ingrese el nuevo valor", justify = "center", relief = "flat", bg = "white")
    label_cambio.place(x = 125, y = 50)
    
    ent_cambio = tk.Entry(ventana, font = ("Calibri 20"), relief = "sunken")
    ent_cambio.place(x = 125, y = 200)
    
    imagen_cambio = PhotoImage(file = 'Iconos_y_fondos/cambiar.png')
    boton_cambio = tk.Button(ventana, image = imagen_cambio, relief = 'flat', bd = 0, highlightthickness=0, command = lambda:cambio_archivo_codigo(ventana, biblioteca, ent_cambio.get(), codigo_li))
    boton_cambio.place(x = 125, y = 300)
    
    ventana.mainloop()
    
def cambio_archivo_codigo(ventana, biblioteca, entrada, codigo_li):
    """
    Permite cambiar el codigo del libro seleccionado
    :param Tk ventana: interfaz grafica
    :param list biblioteca: contiene todos los libros del programa
    :param str entrada: dato por el cual se va a cambiar
    :param str codigo_li: codigo del libro a cambiar
    """
    for elemento in range(len(biblioteca)):
        for l in biblioteca[elemento]:
            if l['codigo'] == codigo_li:
                l['codigo'] = entrada
                change_archivo(elemento, l)
                break
    ventana.destroy()
    
def GUI_cambiar_ca(biblioteca, codigo_li, ventana):
    """
    Interfaz para cambiar la cantidad del libro seleccionado
    :param Tk ventana: interfaz grafica
    :param list biblioteca: contiene todos los libros del programa
    :param str codigo_li: codigo del libro a cambiar
    """
    ventana.destroy()
    import tkinter as tk
    from tkinter import ttk
    from tkinter import PhotoImage
    
    ventana = tk.Tk()
    ventana.geometry('500x400')
    ventana.title('Realizar cambios - Administrador')
    imagen_fondo=PhotoImage(file="Iconos_y_fondos/fondo.png")
    fondo=tk.Label(ventana, image=imagen_fondo)
    fondo.place(x=0, y=0)
    
    label_cambio = tk.Label(ventana, font = ("Calibri 20"), text = "Ingrese el nuevo valor", justify = "center", relief = "flat", bg = "white")
    label_cambio.place(x = 125, y = 50)
    
    ent_cambio = tk.Entry(ventana, font = ("Calibri 20"), relief = "sunken")
    ent_cambio.place(x = 125, y = 200)
    
    imagen_cambio = PhotoImage(file = 'Iconos_y_fondos/cambiar.png')
    boton_cambio = tk.Button(ventana, image = imagen_cambio, relief = 'flat', bd = 0, highlightthickness=0, command = lambda:cambio_archivo_cantidad(ventana, biblioteca, ent_cambio.get(), codigo_li))
    boton_cambio.place(x = 125, y = 300)
    
    ventana.mainloop()
    
def cambio_archivo_cantidad(ventana, biblioteca, entrada, codigo_li):
    """
    Permite cambiar la cantidad del libro seleccionado
    :param Tk ventana: interfaz grafica
    :param list biblioteca: contiene todos los libros del programa
    :param str entrada: dato por el cual se va a cambiar
    :param str codigo_li: codigo del libro a cambiar
    """
    for elemento in range(len(biblioteca)):
        for l in biblioteca[elemento]:
            if l['codigo'] == codigo_li:
                l['cantidad'] = entrada
                change_archivo(elemento, l)
                break
    ventana.destroy()

def change_archivo(indice, l):

    if indice == 0:
        archivo = open("Iconos_y_fondos/matematicas.txt", 'r', encoding = 'utf-8')
        libros = archivo.readlines()
        archivo.close()
        
        actualizacion = open("Iconos_y_fondos/matematicas.txt", 'w', encoding='utf-8')
        for line in libros:
            if l["titulo"] not in line:
                actualizacion.write(line)
        nuevo_libro = l['codigo']+';'+l['autor']+';'+l['fecha']+';'+l['titulo']+';'+l['lugar']+';'+l['editorial']+';'+l['cantidad']+';'+l['cita']+';'+l['link_img']+';'
        actualizacion.write(nuevo_libro+'\n')
        actualizacion.close()
    elif indice == 1:
        archivo = open("Iconos_y_fondos/areas_practicas.txt", 'r', encoding = 'utf-8')
        libros = archivo.readlines()
        archivo.close()
        
        actualizacion = open("Iconos_y_fondos/areas_practicas.txt", 'w', encoding='utf-8')
        for line in libros:
            if l['titulo'] not in line:
                actualizacion.write(line)
        nuevo_libro = l['codigo']+';'+l['autor']+';'+l['fecha']+';'+l['titulo']+';'+l['lugar']+';'+l['editorial']+';'+l['cantidad']+';'+l['cita']+';'+l['link_img']+';'
        actualizacion.write(nuevo_libro+'\n')
        actualizacion.close()
    elif indice == 2:
        archivo = open("Iconos_y_fondos/fisica.txt", 'r', encoding = 'utf-8')
        libros = archivo.readlines()
        archivo.close()
        
        actualizacion = open("Iconos_y_fondos/fisica.txt", 'w', encoding='utf-8')
        for line in libros:
            if l['titulo'] not in line:
                actualizacion.write(line)
        nuevo_libro = l['codigo']+';'+l['autor']+';'+l['fecha']+';'+l['titulo']+';'+l['lugar']+';'+l['editorial']+';'+l['cantidad']+';'+l['cita']+';'+l['link_img']+';'
        actualizacion.write(nuevo_libro+'\n')
        actualizacion.close()
    elif indice == 3:
        archivo = open("Iconos_y_fondos/ciencias_naturales.txt", 'r', encoding = 'utf-8')
        libros = archivo.readlines()
        archivo.close()
        
        actualizacion = open("Iconos_y_fondos/ciencias_naturales.txt", 'w', encoding='utf-8')
        for line in libros:
            if l['titulo'] not in line:    
                actualizacion.write(line)
        nuevo_libro = l['codigo']+';'+l['autor']+';'+l['fecha']+';'+l['titulo']+';'+l['lugar']+';'+l['editorial']+';'+l['cantidad']+';'+l['cita']+';'+l['link_img']+';'
        actualizacion.write(nuevo_libro+'\n')
        actualizacion.close()

def limpiar_administrador(entrada, label_codigo, label_autor, label_titulo, label_fecha, label_lugar, label_editorial, label_cantidad):
    """
    Limpia o deja en blanco todas las etiquetas
    :param Tk entrada: Espacio destinado para ingresar el dato a buscar
    :param Tk label_codigo: Espacio destinado a la presentacion de los codigos
    :param Tk label_autor: Espacio destinado a la presentacion de los autores 
    :param Tk label_titulo: Espacio destinado a la presentacion de los titulos 
    :param Tk label_fechas: Espacio destinado a la presentacion de los fechas
    :param Tk label_lugar: Espacio destinado a la presentacion de los lugares de publicacion de los libros
    :param Tk label_editorial: Espacio destinado a la presentacion de las editoriales
    :param Tk label_cantidad: Espacio destinado a la presentacion de las cantidades disponibles
    """
    entrada.delete(0, 'end')
    label_codigo.delete(0,'end')
    label_autor.delete(0,'end')
    label_titulo.delete(0,'end')
    label_fecha.delete(0,'end')
    label_lugar.delete(0,'end')
    label_editorial.delete(0,'end')
    label_cantidad.delete(0,'end')

def GUI_usuario(biblioteca, cuenta):

    """
    Interfaz Grafica que permite seleccionar que buscar
    :param list biblioteca: Datos de los libros
    :param str cuenta: Nombre completo del usuario
    """

    import tkinter as tk
    from tkinter import ttk
    from tkinter import PhotoImage

    ventana = tk.Tk()
    ventana.title("Biblioteca - Usuario")
    ventana.geometry('1200x650')
    imagen=PhotoImage(file="Iconos_y_fondos/fondo.png")
    fondo=tk.Label(ventana, image=imagen)
    fondo.place(x=0, y=0)

    label_1 = tk.Label(ventana, font= ("Arial 30"), text = "Bienvenido a PYBROS", justify = "center", relief = "flat", bg="white")
    label_1.place(x = 400, y = 2)

    label_2 = tk.Label(ventana, font= ("Calibri 20"), text = 'Criterio :', justify = "left", relief = "flat", bg="white")
    label_2.place(x = 320, y = 70)

    combo_buscar = ttk.Combobox(ventana)
    combo_buscar['values'] = ('Materia', 'Autor', 'Título')
    combo_buscar['font'] = ("Calibri 20")
    combo_buscar.current(0)
    combo_buscar.place(x = 440, y = 70)

    ent_texto = tk.Entry(ventana, font = ("Calibri 20"), relief = "sunken")
    ent_texto.place(x = 440, y = 120)

    imagen_usuario=PhotoImage(file = "Iconos_y_fondos/usuario.png")
    boton_usuario = tk.Button(ventana, image = imagen_usuario, relief = 'flat', bd = 0, highlightthickness=0, command = lambda:cambio_a_inf_usuario(ventana, biblioteca, cuenta))
    boton_usuario.place(x = 18, y = 14)

    label_resultado=tk.Listbox(ventana, font=('Arial bold', 12), width=106, height=10)
    label_resultado.place(x = 145, y = 250)

    label_codigo=tk.Listbox(ventana, font=('Arial bold', 12), width=5, height=10)
    label_codigo.place(x = 145, y = 250)

    label_autor=tk.Listbox(ventana, font=('Arial bold', 12), width=37, height=10)
    label_autor.place(x = 190, y = 250)

    label_titulo=tk.Listbox(ventana, font=('Arial bold', 12), width=56, height=10)
    label_titulo.place(x = 522, y = 250)

    label_fecha=tk.Listbox(ventana, font=('Arial bold', 12), width=5, height=10)
    label_fecha.place(x = 1027, y = 250)

    label_cantidad=tk.Listbox(ventana, font=('Arial bold', 12), width=3, height=10)
    label_cantidad.place(x = 1072, y = 250)

    imagen_volver=PhotoImage(file = "Iconos_y_fondos/volver.png")
    boton_volver = tk.Button(ventana, image = imagen_volver, relief = 'flat', bd = 0, highlightthickness=0, command= lambda: volver(ventana))
    boton_volver.place(x = 18, y = 570)

    label_3 = tk.Label(ventana, font= ("Calibri 20"), text = 'Ingrese código :', justify = "left", relief = "flat", bg="white")
    label_3.place(x = 195, y = 575)

    ent_codigo = tk.Entry(ventana, font = ("Calibri 20"), relief = "sunken")
    ent_codigo.place(x = 450, y = 575)

    imagen_buscar=PhotoImage(file = "Iconos_y_fondos/buscar.png")
    boton_buscar = tk.Button(ventana, image = imagen_buscar, relief = 'flat', bd = 0, highlightthickness=0, command = lambda:buscar_usuario(combo_buscar.get(), ent_texto.get(), biblioteca, label_resultado, label_codigo, label_autor, label_titulo, label_fecha, label_cantidad))
    boton_buscar.place(x = 225, y = 170)

    imagen_citar=PhotoImage(file = "Iconos_y_fondos/citar.png")
    boton_citar = tk.Button(ventana, image = imagen_citar, relief = 'flat', bd = 0, highlightthickness=0, command = lambda:citar_usuario(combo_buscar.get(), ent_texto.get(), biblioteca, label_resultado))
    boton_citar.place(x = 505, y = 170)
    
    imagen_ver=PhotoImage(file = "Iconos_y_fondos/ver_libro.png")
    boton_ver = tk.Button(ventana, image = imagen_ver, relief = 'flat', bd = 0, highlightthickness=0, command = lambda:ver_usuario(ent_codigo.get(), biblioteca, ventana, cuenta))
    boton_ver.place(x = 745, y = 575)
    
    imagen_limpiar=PhotoImage(file = "Iconos_y_fondos/limpiar.png")
    boton_limpiar = tk.Button(ventana, image = imagen_limpiar, relief = 'flat', bd = 0, highlightthickness=0, command = lambda:limpiar_usuario(ent_texto,ent_codigo, label_resultado, label_codigo, label_autor, label_titulo, label_fecha, label_cantidad))
    boton_limpiar.place(x = 795, y = 170)

    ventana.mainloop()
    return

def citar_usuario(criterio, patron, biblioteca, label_resultado):
    
    """
    Selecciona la cita a presentar al ejecutor
    
    :param str criterio: forma en la que se buscaran los datos
    :param str patron: dato buscado
    :param list biblioteca: Datos de los libros
    :param Tk label_resultado: Espacio destinado a la presentacion de las citas de los libros   
    """
    x=0
    inf=''
    label_resultado.lift()
    if criterio == 'Materia':
        if patron=='Matemáticas':
            i=0
            label_resultado.delete(0,'end')
            for l in biblioteca[0]:
                i+=1
                inf=l["cita"]
                label_resultado.insert(i, inf)                
        elif patron=='Áreas prácticas':
            i=0
            label_resultado.delete(0,'end')
            for l in biblioteca[1]:
                i+=1
                inf=l["cita"]
                label_resultado.insert(i, inf) 
        elif patron=='Física':
            i=0
            label_resultado.delete(0,'end')
            for l in biblioteca[2]:
                i+=1
                inf=l["cita"]
                label_resultado.insert(i, inf) 
        elif patron=='Ciencias naturales':
            i=0
            label_resultado.delete(0,'end')
            for l in biblioteca[3]:
                i+=1
                inf=l["cita"]
                label_resultado.insert(i, inf) 
        else:
            label_resultado.delete(0,'end')
            from tkinter import messagebox
            messagebox.showinfo(message="Categoría no encontrada", title="INFORME")   
    elif criterio == 'Autor':
        i=0
        label_resultado.delete(0,'end')        
        for elemento in biblioteca:
            for l in elemento:
                if patron in l["autor"]:
                    i+=1
                    inf=l["cita"]
                    label_resultado.insert(i, inf) 
                    x+=1
        if x==0 or patron=='':
            label_resultado.delete(0,'end')
            from tkinter import messagebox
            messagebox.showinfo(message="Autor no encontrado", title="INFORME")
    elif criterio == 'Título':
        i=0
        label_resultado.delete(0,'end')
        for elemento in biblioteca:
            for l in elemento:
                if patron in l["titulo"]:
                    i+=1
                    inf=l["cita"]
                    label_resultado.insert(i, inf) 
                    x+=1
        if x==0 or patron=='':
            label_resultado.delete(0,'end')
            from tkinter import messagebox
            messagebox.showinfo(message="Libro no encontrado", title="INFORME")

def buscar_usuario(criterio, patron, biblioteca, label_resultado, label_codigo, label_autor, label_titulo, label_fecha, label_cantidad):

    """
    Selecciona que información presentar al ejecutor
    :param str criterio: forma en la que se buscaran los datos
    :param str patron: dato buscado
    :param list biblioteca: Datos de los libros
    :param Tk label_codigo: Espacio destinado a la presentacion de los codigos
    :param Tk label_autor: Espacio destinado a la presentacion de los autores 
    :param Tk label_titulo: Espacio destinado a la presentacion de los titulos 
    :param Tk label_fechas: Espacio destinado a la presentacion de los fechas
    :param Tk label_lugar: Espacio destinado a la presentacion de los lugares de publicacion de los libros
    :param Tk label_editorial: Espacio destinado a la presentacion de las editoriales
    :param Tk label_cantidad: Espacio destinado a la presentacion de las cantidades disponibles
    """
    x = 0
    label_codigo.lift()
    label_autor.lift()
    label_titulo.lift()
    label_fecha.lift()
    label_cantidad.lift()

    label_resultado.delete(0,'end')
    label_codigo.delete(0,'end')
    label_autor.delete(0,'end')
    label_titulo.delete(0,'end')
    label_fecha.delete(0,'end')
    label_cantidad.delete(0,'end')  

    if criterio == 'Materia':
        if patron== 'Matemáticas':
            i = 0                      
            for l in biblioteca[0]:
                i+=1
                label_codigo.insert(i, l["codigo"])
                label_autor.insert(i, l["autor"])
                label_titulo.insert(i, l["titulo"]) 
                label_fecha.insert(i, l["fecha"])
                label_cantidad.insert(i, l["cantidad"])               
        elif patron == 'Áreas prácticas':
            i = 0
            for l in biblioteca[1]:
                i+=1
                label_codigo.insert(i, l["codigo"])
                label_autor.insert(i, l["autor"])
                label_titulo.insert(i, l["titulo"]) 
                label_fecha.insert(i, l["fecha"])
                label_cantidad.insert(i, l["cantidad"]) 
        elif patron == 'Física':
            i = 0
            for l in biblioteca[2]:
                i+=1
                label_codigo.insert(i, l["codigo"])
                label_autor.insert(i, l["autor"])
                label_titulo.insert(i, l["titulo"]) 
                label_fecha.insert(i, l["fecha"])
                label_cantidad.insert(i, l["cantidad"])  
        elif patron=='Ciencias naturales':
            i=0
            for l in biblioteca[3]:
                i+=1
                label_codigo.insert(i, l["codigo"])
                label_autor.insert(i, l["autor"])
                label_titulo.insert(i, l["titulo"]) 
                label_fecha.insert(i, l["fecha"])
                label_cantidad.insert(i, l["cantidad"])  
        else:
            label_resultado.delete(0,'end')
            label_codigo.delete(0,'end')
            label_autor.delete(0,'end')
            label_titulo.delete(0,'end')
            label_fecha.delete(0,'end')
            label_cantidad.delete(0,'end')  
            from tkinter import messagebox
            messagebox.showinfo(message="Categoría no encontrada", title="INFORME")   
    elif criterio == 'Autor':
        i=0     
        for elemento in biblioteca:
            for l in elemento:
                if patron in l["autor"]:
                    i+=1
                    label_codigo.insert(i, l["codigo"])
                    label_autor.insert(i, l["autor"])
                    label_titulo.insert(i, l["titulo"]) 
                    label_fecha.insert(i, l["fecha"])
                    label_cantidad.insert(i, l["cantidad"])  
                    x+=1
        if x==0 or patron=='':
            label_resultado.delete(0,'end')
            label_codigo.delete(0,'end')
            label_autor.delete(0,'end')
            label_titulo.delete(0,'end')
            label_fecha.delete(0,'end')
            label_cantidad.delete(0,'end')  
            from tkinter import messagebox
            messagebox.showinfo(message="Autor no encontrado", title="INFORME")
    elif criterio == 'Título':
        i=0
        for elemento in biblioteca:
            for l in elemento:
                if patron in l["titulo"]:
                    i+=1
                    label_codigo.insert(i, l["codigo"])
                    label_autor.insert(i, l["autor"])
                    label_titulo.insert(i, l["titulo"]) 
                    label_fecha.insert(i, l["fecha"])
                    label_cantidad.insert(i, l["cantidad"]) 
                    x+=1
        if x==0 or patron=='':
            label_resultado.delete(0,'end')
            label_codigo.delete(0,'end')
            label_autor.delete(0,'end')
            label_titulo.delete(0,'end')
            label_fecha.delete(0,'end')
            label_cantidad.delete(0,'end')  
            from tkinter import messagebox
            messagebox.showinfo(message="Libro no encontrado", title="INFORME")

def ver_usuario(entrada, biblioteca, ventana, cuenta):
    
    """
    Selecciona el libro a presentar al ejecutor
    """
    correcto = False
    for elemento in biblioteca:
        for l in elemento:
            if str(entrada) in l["codigo"]:
                correcto = True
                break
                
    if correcto:
        ventana.destroy()
        link1, codigo = busqueda_link_libro(entrada)
        ruta = descarga_imagen(link1, entrada, codigo)
        mostrar_imagen(ruta, entrada, biblioteca, cuenta, codigo)
    else:
        from tkinter import messagebox
        messagebox.showinfo(message = 'Libro no encontrado', title = 'ADVERTENCIA')

def busqueda_link_libro(busqueda):
    link_libro = ''
    codigo = ''
    biblioteca=leer_libros()
    for elemento in biblioteca:
        for l in elemento:
            if l["codigo"] == busqueda:
                link_libro=l["link_img"]
                codigo=l["codigo"]
    if link_libro == '':
        link_libro = 'NO DISPONIBLE'

    l_imagen = extraer_link(link_libro)
    return l_imagen, codigo

def extraer_link(link_libro_1):
    from bs4 import BeautifulSoup
    from urllib.request import urlopen

    if link_libro_1=="NO DISPONIBLE":
        link_imagenes='NO DISPONIBLE'
    else:
        url = link_libro_1
        page = urlopen(url)
        html = page.read().decode("utf-8")
        soup = BeautifulSoup(html, "html.parser")
        imagenes = soup.find_all("img")
        imagen = imagenes[0]["src"]
        link_imagenes="http://library.lol" + imagen
    return link_imagenes
       
def descarga_imagen(link_imagen, busqueda, numero):
    import requests
    import shutil
    if link_imagen=='NO DISPONIBLE':
        nombre_local_imagen="Portadas_libros/No_disponible.PNG"
    else:
        
        url = link_imagen
        nombre_local_imagen = numero + ".png"
        imagen = requests.get(url).content
        with open(nombre_local_imagen, 'wb') as handler:
            handler.write(imagen)
        shutil.move(nombre_local_imagen, "Portadas_libros/" + nombre_local_imagen)
                
    return nombre_local_imagen   

def mostrar_imagen(portada, busqueda, biblioteca, cuenta, codigo):
    import tkinter as tk
    from tkinter import PhotoImage
    from PIL import Image, ImageTk

    ventana = tk.Tk()
    ventana.title("Portada libro")
    ventana.geometry('900x1500')
    imagen=PhotoImage(file="Iconos_y_fondos/fondo_cambio.png")
    fondo=tk.Label(ventana, image=imagen)
    fondo.place(x=1, y=1)
    try:
        #imagen_fondo=PhotoImage(file=portada)
        imagen_fondo=ImageTk.PhotoImage(Image.open("Portadas_libros/" + portada)) 
        fondo=tk.Label(ventana, image=imagen_fondo)
        fondo.place(x=0, y=0)
    except:
        imagen_fondo=PhotoImage(file="Portadas_libros/No_disponible.PNG")
        fondo=tk.Label(ventana, image=imagen_fondo)
        fondo.place(x=0, y=0)
    
    imagen_biblioteca=PhotoImage(file = "Iconos_y_fondos/biblioteca.png")
    boton_biblioteca = tk.Button(ventana, image = imagen_biblioteca, relief = 'flat', bd = 0, highlightthickness=0, command = lambda:cambio_a_biblioteca(ventana, biblioteca, cuenta))
    boton_biblioteca.place(x = 75, y = 520)

    imagen_resevar=PhotoImage(file = "Iconos_y_fondos/reservar.png")
    boton_resevar = tk.Button(ventana, image = imagen_resevar, relief = 'flat', bd = 0, highlightthickness=0, command = lambda:reservar(ventana, biblioteca, cuenta, codigo) )
    boton_resevar.place(x = 75, y = 590)

    ventana.mainloop()
    return

def usuarios_reservar():
    archivo = open('Datos/usuarios.txt', 'r', encoding="utf-8")
    lineas = archivo.readlines()
    archivo.close()
    datos_completos=[]
    for linea in lineas:
        datos = linea.split(';')
        datos_completos.append(datos)
    return datos_completos

def reservar(ventana, biblioteca, cuenta, codigo):
    from datetime import datetime, date, time, timedelta
    import calendar
    ahora = datetime.now()
    ahora = ahora.replace(microsecond=0)
    fecha_de_entrega =  ahora + timedelta(hours=1)    
    fecha_de_entrega = time(fecha_de_entrega.day, fecha_de_entrega.hour, fecha_de_entrega.minute, fecha_de_entrega.second)

    datos_usuarios=directorio_usuario_sesion()
    hola=False  
    for elemento in biblioteca:
        for l in elemento:
            if l["codigo"]==codigo:
                hola=True

    inf_usu=usuarios_reservar()
    Vacio=True

    reserva=''    
    if hola:
        for elemento in datos_usuarios:
            if 'Usuario' in elemento:
                if elemento['Usuario']==cuenta:
                    if elemento["libro1"]==' ':
                        posicion=4
                        reserva=codigo +'*'+str(fecha_de_entrega)
                    elif elemento["libro2"]==' ':
                        posicion=5
                        reserva=codigo +'*'+str(fecha_de_entrega)
                    elif elemento["libro3"]==' ':
                        posicion=6
                        reserva=codigo +'*'+str(fecha_de_entrega)
                    else:
                        Vacio=False
                        from tkinter import messagebox
                        messagebox.showinfo(message="Usted ya alcanzó el límite de los libros guardados.", title="INFORME")
    
    archivo = open('Datos/usuarios.txt', 'w', encoding="utf-8")
    for linea in archivo:
        if cuenta not in linea:
            archivo.write(linea)
    
    archivo.close()

def limpiar_usuario(entrada, entcodigo, resultado, codigo, autor, titulo, fecha, cantidad):
    """
    Limpia o deja en blanco todas las etiquetas
    :param Tk entrada: Espacio destinado para ingresar el dato a buscar
    :param Tk entcodigo: Espacio destinado para ingresar el codigo a buscar
    :param Tk codigo: Espacio destinado a la presentacion de los codigos
    :param Tk autor: Espacio destinado a la presentacion de los autores 
    :param Tk titulo: Espacio destinado a la presentacion de los titulos 
    :param Tk fecha: Espacio destinado a la presentacion de los fechas
    :param Tk cantidad: Espacio destinado a la presentacion de las cantidades disponibles
    """
    entrada.delete(0, 'end')
    entcodigo.delete(0, 'end')
    resultado.delete(0, 'end')
    codigo.delete(0, 'end')
    autor.delete(0, 'end')
    titulo.delete(0, 'end')
    fecha.delete(0, 'end')
    cantidad.delete(0, 'end')

def volver(ventana):
    """
    Elimina la ventana actual y abre la descrita
    :param Tk Ventana: de la interfaz gráfica
    """
    ventana.destroy()
    GUI_inicio()

def cambio_a_inf_usuario(ventana, biblioteca, cuenta):
    """
    Elimina la ventana actual y abre la descrita
    :param Tk Ventana: de la interfaz gráfica
    :param list biblioteca: Datos de los libros
    :param str cuenta: Nombre completo del usuario
    """
    ventana.destroy()
    GUI_inf_usuario(biblioteca, cuenta)

def GUI_inf_usuario(biblioteca, cuenta):
    """
    Interfaz Grafica que presenta la informacion perteneciente al usuario
    :param list biblioteca: Datos de los libros
    :param str cuenta: Nombre completo del usuario
    """
    import tkinter as tk
    from tkinter import ttk
    from tkinter import PhotoImage
    ventana = tk.Tk()
    ventana.title("Información usuario")
    ventana.geometry('1200x650')
    imagen_fondo=PhotoImage(file="Iconos_y_fondos/fondo_usuario.png")
    fondo=tk.Label(ventana, image=imagen_fondo)
    fondo.place(x=0, y=0)

    imagen_biblioteca=PhotoImage(file = "Iconos_y_fondos/biblioteca.png")
    boton_biblioteca = tk.Button(ventana, image = imagen_biblioteca, relief = 'flat', bd = 0, highlightthickness=0, command = lambda:cambio_a_biblioteca(ventana, biblioteca, cuenta))
    boton_biblioteca.place(x = 18, y = 14)

    label_1 = tk.Label(ventana, font= ("Arial 30"), text = "Información cuenta", justify = "center", relief = "flat", bg="white")
    label_1.place(x = 400, y = 2)
    
    label_2 = tk.Label(ventana, font= ("Calibri 20"), text = 'Nombre :', justify = "left", relief = "flat", bg="white")
    label_2.place(x = 20, y = 90)

    label_nombre = tk.Label(ventana, font= ("Calibri 20"), text = cuenta, justify = "left", relief = "flat", bg="white")
    label_nombre.place(x = 120, y = 90)

    label_3 = tk.Label(ventana, font= ("Calibri 20"), text = 'Libros reservados :', justify = "left", relief = "flat", bg="white")
    label_3.place(x = 20, y = 170)

    label_4 = tk.Label(ventana, font= ("Calibri 20"), text = 'código', justify = "left", relief = "flat", bg="white")
    label_4.place(x = 20, y = 210)

    label_5 = tk.Label(ventana, font= ("Calibri 20"), text = 'titulo', justify = "left", relief = "flat", bg="white")
    label_5.place(x = 120, y = 210)

    label_6 = tk.Label(ventana, font= ("Calibri 20"), text = 'autor', justify = "left", relief = "flat", bg="white")
    label_6.place(x = 400, y = 210)

    label_7 = tk.Label(ventana, font= ("Calibri 20"), text = 'fecha limite de entrega', justify = "left", relief = "flat", bg="white")
    label_7.place(x = 690, y = 210)

    label_8 = tk.Label(ventana, font= ("Calibri 20"), text = 'Ingrese código :', justify = "left", relief = "flat", bg="white")
    label_8.place(x = 195, y = 570)

    ent_codigo = tk.Entry(ventana, font = ("Calibri 20"), relief = "sunken")
    ent_codigo.place(x = 455, y = 570)

    imagen_devolver=PhotoImage(file = "Iconos_y_fondos/devolver.png")
    boton_devolver = tk.Button(ventana, image = imagen_devolver, relief = 'flat', bd = 0, highlightthickness=0)
    boton_devolver.place(x = 795, y = 570)

    imagen_volver=PhotoImage(file = "Iconos_y_fondos/volver.png")
    boton_volver = tk.Button(ventana, image = imagen_volver, relief = 'flat', bd = 0, highlightthickness=0, command = lambda:volver(ventana))
    boton_volver.place(x = 18, y = 570)

    ventana.mainloop()
    return

def cambio_a_biblioteca(ventana, biblioteca, cuenta):
    """
    Elimina la ventana actual y abre la descrita
    :param Tk Ventana: de la interfaz gráfica
    """
    ventana.destroy()
    GUI_usuario(biblioteca, cuenta)

def main():
    """
    Dirige a la interfaz de inicio
    """
    GUI_inicio()

main()