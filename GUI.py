import tkinter as tk  
from tkinter import *
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
from tkinter import font  as tkfont # python 3
import os.path
from Proceso import *
from ManejoArchivos import *

class USFMENU(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        TextoParaModificar = StringVar()
        TextoqueSustituira = StringVar()
        DirectorioArchivo = StringVar()
        
        def cargarTexton():
            textoRecibido,directorio = ManejoArchivo.cargarInformacion(self)
            content_text.insert(END,textoRecibido)
            DirectorioArchivo.set(directorio)
            print(directorio)
            pass

        def envioSustituciondeTexto():
            
            texto1 = ""
            texto2 = ""
            textoOriginal = content_text.get(1.0,END)
            texto1 = TextoParaModificar.get()
            texto2 = TextoqueSustituira.get()
            TextoRecibido = Operativo.sustitucionTexto(self,textoOriginal,texto1,texto2)
            content_text.config(state=NORMAL)
            content_text.delete(1.0,END)
            content_text.insert(END,TextoRecibido)
            TextoParaModificar.set("")
            TextoqueSustituira.set("")
            pass

        def realizarProceso():
            textoOriginal = content_text.get(1.0, END)
            TextoRecibido = Operativo.realizandoProceso(self,textoOriginal)
            content_text.config(state=NORMAL)
            content_text.delete(1.0, END)
            content_text.insert(END, TextoRecibido)
            pass

        def guardando():
            textoOriginal = content_text.get(1.0, END)
            ManejoArchivo.guardarEnArchivo(textoOriginal)
            pass

        def salir():
            sys.exit(0)
            pass

        label = tk.Label(self, text="Limpiando Texto 4.2", font=controller.title_font)
        label.place(x=500, y=10)

        txtFrame = Frame(self, borderwidth=1, relief="sunken")

        content_text = Text(txtFrame, wrap=NONE, height=29,
                            width=132, borderwidth=0,font="Arial 12 bold")
        vscroll = Scrollbar(txtFrame, orient=VERTICAL,
                            command=content_text.yview)
        content_text['yscroll'] = vscroll.set

        vscroll.pack(side="right", fill="y")
        content_text.pack(side="left", fill="both", expand=True)

        txtFrame.place(x=10, y=50)
    
        TXBParaModificar = tk.Entry(self, textvariable = TextoParaModificar, justify="center", width=95).place(x=10, y=623)

        TXBTextoaSustituir = tk.Entry(self, textvariable = TextoqueSustituira, justify="center", width=95).place(x=600, y=623)
        
        TXBDirectoriodeArchivo = tk.Entry(self, textvariable=DirectorioArchivo, justify="center", width=170).place(x=10, y=647)

        BTNCambio = tk.Button(self, text="+", justify="center",
                              command=lambda: envioSustituciondeTexto(), width=5)
        BTNCambio.place(x=1195, y=623)

        BTNGuardar = tk.Button(self, text="Guardar", justify="center",
                             command=lambda: guardando(), width=6)
        BTNGuardar.place(x=1143, y=648)

        BTNsalir = tk.Button(self, text="salir", justify="center",
                             command=lambda: salir(), width=5)
        BTNsalir.place(x=1195, y=648)

        BTNAbrir = tk.Button(self, text="Abrir", justify="center",
                             command=lambda: cargarTexton(), width=5)
        BTNAbrir.place(x=1050, y=648)

        BTNProceso = tk.Button(self, text="Proceso", justify="center",
                             command=lambda: realizarProceso(), width=6)
        BTNProceso.place(x=1095, y=648)
        pass
