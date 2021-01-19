import io
import os
import os.path
import sys
from tkinter import filedialog
from tkinter import filedialog as fd
from tkinter import messagebox

class ManejoArchivo():
    def __init__(self):
        pass

    def cargarInformacion(self):
        filename = filedialog.askopenfilename( )
        #file = open(filename, 'r')
        file = open(filename, 'r', encoding="utf-8")
        buff = file.read()
        file.close()
        return buff,filename

    def guardarEnArchivo(Archivoagurdar):
        nombrearch = fd.asksaveasfilename(initialdir="/", title="Guardar como", filetypes=(
                    ("txt files", "*.txt"), ("todos los archivos", "*.*")))
        if nombrearch!= '':
            archi1=open(nombrearch, "w", encoding = "utf-8")
            archi1.write(Archivoagurdar)
            archi1.close()
            messagebox.showinfo("Información", "Los datos fueron guardados en el archivo.")
