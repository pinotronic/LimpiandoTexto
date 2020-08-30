# Esta aplicacion quita los espacios a los documentos de texto, dejando todo
# sin espacio se recomienda utilizar la otra aplicacion para insertar 
# espacios despues de los puntos.

import tkinter as tk  
from tkinter import *
from tkinter import ttk
from GUI import *
from Proceso import *
from ManejoArchivos import *

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        # tk.Tk.iconbitmap(self, default="icono.ico")
        tk.Tk.wm_title(self, "Limpiando Texto 4.2")
        tk.Tk.colormapwindows="#e4007c"

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        container = tk.Frame(self)
        
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=15)
        container.grid_columnconfigure(0, weight=15)
        
        self.frames = {}
        F =USFMENU
        page_name = F.__name__
        frame = F(parent=container, controller=self)
        self.frames[page_name] = frame

        frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("USFMENU")
        
    def show_frame(self, page_name):
        '''Mostrar un marco para el nombre de página dado'''
        frame = self.frames[page_name]
        frame.tkraise()
        frame.config(bg="#e4007c")

if __name__ == "__main__":
    app = SampleApp()
    app.geometry("1250x680+55+10")
    
    app.mainloop()
