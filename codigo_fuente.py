# Biblioteca de los libros:
def biblioteca_administrador():
    from io import open
    import os
    """

    lee los libros y crea listas segun las categorias, ademas de clasificar los datos individuales de los textos
    :return: Lista categorias

    """
    global biblioteca
    matematicas = []
    areas_practicas = []
    fisica = []
    ciencias_naturales = []

    libros = ["matematicas.txt", "areas_practicas.txt", "fisica.txt", "ciencias_naturales.txt"]
    biblioteca = [matematicas, areas_practicas, fisica, ciencias_naturales]

    for i in range(len(libros)):
        archivo = open(libros[i], "r", encoding="utf-8")
        lineas = archivo.readlines()
        archivo.close()

        for linea in lineas:
            campos = linea.split(";")
            libro = {"autor": campos[0], "fecha": campos[1], "titulo": campos[2], "lugar": campos[3],
                     "editorial": campos[4], "cantidad": campos[5], "cita": campos[6]}
            biblioteca[i].append(libro)

    return biblioteca


def biblioteca_usuarios():
    """
    Lee de un .txt la base de datos de los libros a los que los usuarios pueden tener acceso.
    :return: Lista libros    

    """
    global libros
    libros = []
    archivo = open('libros_usuario.txt', 'r', encoding="utf-8")
    lineas = archivo.readlines()
    for linea in lineas:
        datos_libro = linea.split('|')
        libros.append(datos_libro)
    return libros


def directorio_usuarios():
    """
    Lee de un .txt la base de datos que contiene los usuarios que pueden acceder a la biblioteca.
    :return: Lista usuarios
    
    """
    global usuarios
    usuarios = []
    archivo = open('usuarios.txt', 'r', encoding="utf-8")
    lineas = archivo.readlines()
    for linea in lineas:
        datos_usuario = linea.split(';')
        usuarios.append(datos_usuario)
    return usuarios


# Interfaces gráficas de los buscadores:
def Interfaz_Inicio():
    """
    Interfaz Grafica que permite seleccionar el tipo de usuario
    """
    import tkinter as tk
    from tkinter import ttk
    ventana = tk.Tk()
    ventana.title("Biblioteca")
    ventana['background'] = ('blue')

    # GUI Entrada
    bien = "Bienvenido a PYBROS"
    label_1 = tk.Label(ventana, fg="white", bg="darkgoldenrod1", font=("Verdana", 24), text=bien, justify="center",
                       relief="raised")
    label_1.grid(row=0, column=0, columnspan=8, padx=5, pady=5)
    label_2 = tk.Label(ventana, fg="darkgoldenrod1", bg="blue", font=("DEAR SUNSHINE", 20), text='Tipo Usuario',
                       justify="left", relief="flat")
    label_2.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
    label_3 = tk.Label(ventana, fg="darkgoldenrod1", bg="blue", font=("DEAR SUNSHINE", 20), text='Login Name',
                       justify="left", relief="flat")
    label_3.grid(row=2, column=0, columnspan=2, padx=5, pady=5)
    combo_buscar = ttk.Combobox(ventana)
    combo_buscar['values'] = ('Usuario', 'Administrador')
    combo_buscar['font'] = ("Arial Black", 15)
    combo_buscar['foreground'] = ("darkgoldenrod1")
    combo_buscar.current(0)
    combo_buscar.grid(row=1, column=2, columnspan=6, padx=5, pady=5)
    ent_texto = tk.Entry(ventana, font=("Calibri 20"), relief="sunken")
    ent_texto.grid(row=2, column=2, columnspan=6, padx=5, pady=5)
    boton_buscar = tk.Button(ventana, fg="white", bg="darkgoldenrod1", text="Ingreso", font=("Calibri 20"),
                             command=lambda: usuario(combo_buscar.get(), ent_texto.get()))
    boton_buscar.grid(row=3, column=2, columnspan=4, padx=5, pady=5)

    ventana.mainloop()
    return


def Interfaz_administrador():
    """
    Interfaz Grafica que permite seleccionar que buscar al administrador
    """
    import tkinter as tk
    from tkinter import ttk
    ventana = tk.Tk()
    ventana.title("Biblioteca")

    # GUI Entrada
    bien = "Bienvenido a PYBROS"
    label_1 = tk.Label(ventana, fg="white", bg="darkgoldenrod1", font=("Verdana", 24), text=bien, justify="center",
                       relief="raised")
    label_1.grid(row=0, column=0, columnspan=8, padx=5, pady=5)
    label_2 = tk.Label(ventana, fg="darkgoldenrod1", bg="blue", font=("DEAR SUNSHINE", 30), text=' Criterio',
                       justify="left", relief="flat")
    label_2.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
    combo_buscar = ttk.Combobox(ventana)
    combo_buscar['values'] = ('Materia', 'Autor', 'Título')
    combo_buscar['font'] = ("Arial Black", 15)
    combo_buscar['foreground'] = ("darkgoldenrod1")
    combo_buscar.current(0)
    combo_buscar.grid(row=1, column=2, columnspan=6, padx=5, pady=5)
    ent_texto = tk.Entry(ventana, font=("Calibri 20"), relief="sunken")
    ent_texto.grid(row=2, column=0, columnspan=6, padx=5, pady=5)
    boton_buscar = tk.Button(ventana, fg="white", bg="darkgoldenrod1", text="Buscar", font=("Calibri 20"),
                             command=lambda: buscar_administrador(combo_buscar.get(), ent_texto.get()))
    boton_buscar.grid(row=2, column=6, columnspan=2, padx=5, pady=5)

    ventana.mainloop()
    return


def Interfaz_usuario():
    """
    Interfaz Grafica que permite seleccionar que buscar al usuario
    """
    import tkinter as tk
    from tkinter import ttk
    ventana = tk.Tk()
    ventana.title("Biblioteca")
    ventana['background'] = ('blue')

    # GUI Entrada
    bien = "Bienvenido a PYBROS"
    label_1 = tk.Label(ventana, fg="white", bg="darkgoldenrod1", font=("Verdana", 24), text=bien, justify="center",
                       relief="raised")
    label_1.grid(row=0, column=0, columnspan=8, padx=5, pady=5)
    label_2 = tk.Label(ventana, fg="darkgoldenrod1", bg="blue", font=("DEAR SUNSHINE", 30), text=' Criterio',
                       justify="left", relief="flat")
    label_2.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
    combo_buscar = ttk.Combobox(ventana)
    combo_buscar['values'] = ('Materia', 'Autor', 'Título')
    combo_buscar['font'] = ("Arial Black", 15)
    combo_buscar['foreground'] = ("darkgoldenrod1")
    combo_buscar.current(0)
    combo_buscar.grid(row=1, column=2, columnspan=6, padx=5, pady=5)
    ent_texto = tk.Entry(ventana, font=("Calibri 20"), relief="sunken")
    ent_texto.grid(row=2, column=0, columnspan=6, padx=5, pady=5)
    boton_buscar = tk.Button(ventana, fg="white", bg="darkgoldenrod1", text="Buscar", font=("Calibri 20"),
                             command=lambda: buscar_usuario(combo_buscar.get(), ent_texto.get()))
    boton_buscar.grid(row=2, column=6, columnspan=2, padx=5, pady=5)

    ventana.mainloop()
    return


# Funciones de búsqueda de libros solicitados:
def buscar_administrador(criterio, patron):
    """
    Selecciona que información presentar al ejecutor
    :param int criterio, patron: filtro demmétodo de búsqueda, identificacion del libro o libros
    :return: Lista resultado
    """
    resultado = []
    if criterio == 'Materia':
        if patron == 'Matemáticas':
            for l in biblioteca[0]:
                resultado.append(l)
        elif patron == 'Áreas Prácticas':
            for l in biblioteca[1]:
                resultado.append(l)
        elif patron == 'Física':
            for l in biblioteca[2]:
                resultado.append(l)
        elif patron == 'Ciencias Naturales':
            for l in biblioteca[3]:
                resultado.append(l)
    elif criterio == 'Autor':
        for elemento in biblioteca:
            for l in elemento:
                if patron in l["autor"]:
                    resultado.append(l)
    elif criterio == 'Título':
        for elemento in biblioteca:
            for l in elemento:
                if patron in l["titulo"]:
                    resultado.append(l)
    if len(resultado) == 0:
        from tkinter import messagebox
        messagebox.showinfo(message="Libro no encontrado", title="INFORME")
    else:
        resultado_buscar(resultado)
    return resultado


def buscar_usuario(criterio, patron):
    """
    Selecciona que información presentar al ejecutor
    :param int criterio, patron: filtro demmétodo de búsqueda, identificacion del libro o libros
    :return: Lista resultado
    """
    global resultado
    resultado = []
    for i in libros:
        if criterio == 'Materia' and patron in i[0]:
            resultado.append(i)
        elif criterio == 'Autor' and patron in i[1]:
            resultado.append(i)
        elif criterio == 'Título' and patron in i[2]:
            prestamo(i)
            resultado.append(i)
    if len(resultado) == 0:
        from tkinter import messagebox
        messagebox.showinfo(message="Libro no encontrado", title="INFORME")
    else:
        resultado_buscar(resultado)
    return resultado


def resultado_buscar(resultado):
    """
    Muestra la información requerida en el buscador.
    :param resultado: Lista resultado
    """
    import tkinter as tk
    from tkinter import ttk
    ventana = tk.Tk()
    ventana.title("Resultado")
    Label_1 = tk.Listbox(ventana)
    for item in range(len(resultado)):
        Label_1.insert(item, resultado[item])
    Label_1.pack(side="left", fill="both", expand=True)
    #mainloop()


# Funciones que toman acción en los libros:
def disponibilidad(libro):
    """
    Verifica que en el inventario de libros el libro solicitado no esté agotado.

    :param int libro: información del libro que se solicitó
    :return dispionible: booleano que indica si está o no disponible.
    """
    cantidad = int(libro[3])
    disponible = True
    if cantidad != 0:
        disponible = True
        print('El libro {} está listo para encontrar su nuevo dueño temporal :)'.format(libro[3]))
    else:
        print('Lo sentimos, el libro {} que solicitaste está agotado por el momento, pero seguro dentro de un par de días estará disponible. Esperamos verte pronto.'.format(
                libro[3]))
        disponible = False
    return disponible


def prestamo(libro):
    """
    Cuando el libro esté disponible, disminuye en uno la cantidad de libros en el inventario. Y después imprime en pantalla la referencia bibliográfica en normas APA.
    :param int libro: información del libro que se solicitó.
    :return cantidad: entero que indica la cantidad restante del libro.
    """
    cantidad=int(libro[3])
    if disponibilidad(libro):
        cantidad -= 1
        print(libro[:3])
        print('Ya tomaste prestado el libro. Recuerda que tienes 8 días hábiles disponibles para devolverlo.\nLa cantidad de libros restantes en el inventario es de: 0 ')
    return cantidad


# Función de entradas:
def usuario(criterio, patron):
    """
    Direcciona el tipo de ingreso según su rol en la biblioteca (usuario o administrador)
    :param int criterio, patron: selección de rol dentro de la librería, identificación de la persona.
    :return: NONE
    """
    userexist = False
    for i in usuarios:
        if criterio == 'Administrador' and i[0] == "admin" and patron == i[1]:
            userexist = True
        elif criterio == 'Usuario' and i[0] == "user" and patron == i[1]:
            userexist = True

    if userexist:
        if criterio == 'Usuario':
            biblioteca_usuarios()
            Interfaz_usuario()
            buscar_usuario()
            print(resultado)
        elif criterio == 'Administrador':
            biblioteca_administrador()
            Interfaz_administrador()
            buscar_administrador()
    else:
        from tkinter import messagebox
        messagebox.showerror(message="Usted es un hacker", title="ERROR")


def main():
    directorio_usuarios()
    Interfaz_Inicio()



main()