import sys
import tkinter as tk  
from tkinter import *
from ManejoArchivos import *
from Proceso import *
import pyperclip as clipboard

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = FRMLimpiandoTexto (root)
    # LimpiandoTexto4.3_support.init(root, top)
    root.mainloop()

w = None
def create_FRMLimpiandoTexto(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = FRMLimpiandoTexto (w)
    # LimpiandoTexto4.3_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_FRMLimpiandoTexto():
    global w
    w.destroy()
    w = None

class FRMLimpiandoTexto:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font9 = "-family {Segoe UI} -size 9 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("1264x640")
        top.minsize(120, 1)
        top.maxsize(2810, 881)
        top.resizable(1, 1)
        top.title("Limpiando Texto 4.3")
        top.configure(background="#004040")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        textoParaModificar = StringVar()
        textoqueSustituira = StringVar()
        DirectorioArchivo = StringVar()

        def cargarTexton():
            self.txtCajaTexto.delete(1.0, END)
            textoRecibido,directorio = ManejoArchivo.cargarInformacion(self)
            self.txtCajaTexto.insert("1.0",textoRecibido)
            DirectorioArchivo.set(directorio)
            print(directorio)
            pass

        def borrarTexto():
            self.txtCajaTexto.delete(1.0, END)

        def envioSustituciondeTexto():
            
            texto1 = ""
            texto2 = ""
            textoOriginal = self.txtCajaTexto.get(1.0,END)
            texto1 = self.txbTextoAModificar.get()
            texto2 = self.txbTextoModificado.get()
            TextoRecibido = Operativo.sustitucionTexto(self,textoOriginal,texto1,texto2)
            self.txtCajaTexto.config(state=NORMAL)
            self.txtCajaTexto.delete(1.0,END)
            self.txtCajaTexto.insert(END,TextoRecibido)
            textoParaModificar.set("")
            textoqueSustituira.set("")
            
            pass

        def copiarTexto():
            textoOriginal=self.txtCajaTexto.get(1.0, END)
            clipboard.copy(textoOriginal)
            pass
            
        def realizarProceso():
            textoOriginal = self.txtCajaTexto.get(1.0, END)
            TextoRecibido = Operativo.realizandoProceso(self,textoOriginal)
            self.txtCajaTexto.config(state=NORMAL)
            self.txtCajaTexto.delete(1.0, END)
            self.txtCajaTexto.insert(END, TextoRecibido)
            pass

        def guardando():
            textoOriginal = self.txtCajaTexto.get(1.0, END)
            ManejoArchivo.guardarEnArchivo(textoOriginal)
            pass

        def salir():
            sys.exit(0)
            pass

        self.txtCajaTexto = ScrolledText(top)
        self.txtCajaTexto.place(relx=0.008, rely=0.094, relheight=0.752
                , relwidth=0.982)
        self.txtCajaTexto.configure(background="white")
        self.txtCajaTexto.configure(font=font9)
        self.txtCajaTexto.configure(foreground="black")
        self.txtCajaTexto.configure(highlightbackground="#d9d9d9")
        self.txtCajaTexto.configure(highlightcolor="black")
        self.txtCajaTexto.configure(insertbackground="black")
        self.txtCajaTexto.configure(insertborderwidth="3")
        self.txtCajaTexto.configure(selectbackground="#c4c4c4")
        self.txtCajaTexto.configure(selectforeground="black")
        self.txtCajaTexto.configure(wrap="none")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.332, rely=0.016, height=50, width=357)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#004040")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Arial} -size 28 -weight bold")
        self.Label1.configure(foreground="#ff8000")
        self.Label1.configure(highlightbackground="#ff8000")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Limpando Texto 4.3''')

        self.txbTextoAModificar = tk.Entry(top)
        self.txbTextoAModificar.place(relx=0.008, rely=0.859, height=20
                , relwidth=0.47)
        self.txbTextoAModificar.configure(background="white")
        self.txbTextoAModificar.configure(disabledforeground="#a3a3a3")
        self.txbTextoAModificar.configure(font="-family {Courier New} -size 10")
        self.txbTextoAModificar.configure(foreground="#000000")
        self.txbTextoAModificar.configure(highlightbackground="#d9d9d9")
        self.txbTextoAModificar.configure(highlightcolor="black")
        self.txbTextoAModificar.configure(insertbackground="black")
        self.txbTextoAModificar.configure(selectbackground="#c4c4c4")
        self.txbTextoAModificar.configure(textvariable = textoParaModificar)
        self.txbTextoAModificar.configure(selectforeground="black")

        self.txbDireccionArchivo = tk.Entry(top)
        self.txbDireccionArchivo.place(relx=0.008, rely=0.906, height=20
                , relwidth=0.818)
        self.txbDireccionArchivo.configure(background="white")
        self.txbDireccionArchivo.configure(disabledforeground="#a3a3a3")
        self.txbDireccionArchivo.configure(font="-family {Courier New} -size 10")
        self.txbDireccionArchivo.configure(foreground="#000000")
        self.txbDireccionArchivo.configure(highlightbackground="#d9d9d9")
        self.txbDireccionArchivo.configure(highlightcolor="black")
        self.txbDireccionArchivo.configure(insertbackground="black")
        self.txbDireccionArchivo.configure(selectbackground="#c4c4c4")
        self.txbDireccionArchivo.configure(textvariable=DirectorioArchivo)
        self.txbDireccionArchivo.configure(selectforeground="black")

        self.btnAbrir = tk.Button(top)
        self.btnAbrir.place(relx=0.835, rely=0.906, height=24, width=67)
        self.btnAbrir.configure(activebackground="#ececec")
        self.btnAbrir.configure(activeforeground="#000000")
        self.btnAbrir.configure(background="#00ff00")
        self.btnAbrir.configure(disabledforeground="#a3a3a3")
        self.btnAbrir.configure(foreground="#000000")
        self.btnAbrir.configure(highlightbackground="#d9d9d9")
        self.btnAbrir.configure(highlightcolor="black")
        self.btnAbrir.configure(pady="0")
        self.btnAbrir.configure(command=lambda: cargarTexton())
        self.btnAbrir.configure(text='''Abrir''')

        self.btnProceso = tk.Button(top)
        self.btnProceso.place(relx=0.894, rely=0.906, height=24, width=63)
        self.btnProceso.configure(activebackground="#ececec")
        self.btnProceso.configure(activeforeground="#000000")
        self.btnProceso.configure(background="#ffff00")
        self.btnProceso.configure(disabledforeground="#a3a3a3")
        self.btnProceso.configure(foreground="#000000")
        self.btnProceso.configure(highlightbackground="#d9d9d9")
        self.btnProceso.configure(highlightcolor="black")
        self.btnProceso.configure(pady="0")
        self.btnProceso.configure(command=lambda: realizarProceso())
        self.btnProceso.configure(text='''Proceso''')

        self.btnGuardar = tk.Button(top)
        self.btnGuardar.place(relx=0.949, rely=0.906, height=24, width=59)
        self.btnGuardar.configure(activebackground="#ececec")
        self.btnGuardar.configure(activeforeground="#000000")
        self.btnGuardar.configure(background="#0080ff")
        self.btnGuardar.configure(disabledforeground="#a3a3a3")
        self.btnGuardar.configure(foreground="#000000")
        self.btnGuardar.configure(highlightbackground="#d9d9d9")
        self.btnGuardar.configure(highlightcolor="black")
        self.btnGuardar.configure(pady="0")
        self.btnGuardar.configure(command=lambda: guardando())
        self.btnGuardar.configure(text='''Guardar''')

        self.btnSalir = tk.Button(top)
        self.btnSalir.place(relx=0.949, rely=0.953, height=24, width=57)
        self.btnSalir.configure(activebackground="#ececec")
        self.btnSalir.configure(activeforeground="#000000")
        self.btnSalir.configure(background="#ff0000")
        self.btnSalir.configure(disabledforeground="#a3a3a3")
        self.btnSalir.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.btnSalir.configure(foreground="#ffffff")
        self.btnSalir.configure(highlightbackground="#d9d9d9")
        self.btnSalir.configure(highlightcolor="#ff8080")
        self.btnSalir.configure(pady="0")
        self.btnSalir.configure(command=lambda: salir())
        self.btnSalir.configure(text='''Salir''')

        self.btnCambiar = tk.Button(top)
        self.btnCambiar.place(relx=0.957, rely=0.859, height=24, width=19)
        self.btnCambiar.configure(activebackground="#ececec")
        self.btnCambiar.configure(activeforeground="#000000")
        self.btnCambiar.configure(background="#ff8000")
        self.btnCambiar.configure(disabledforeground="#a3a3a3")
        self.btnCambiar.configure(foreground="#000000")
        self.btnCambiar.configure(highlightbackground="#d9d9d9")
        self.btnCambiar.configure(highlightcolor="black")
        self.btnCambiar.configure(pady="0")
        self.btnCambiar.configure(command=lambda: envioSustituciondeTexto())
        self.btnCambiar.configure(text='''+''')

        self.btnBorrar= tk.Button(top)
        self.btnBorrar.place(relx=0.937, rely=0.859, height=24, width=19)
        self.btnBorrar.configure(activebackground="#ececec")
        self.btnBorrar.configure(activeforeground="#000000")
        self.btnBorrar.configure(background="#ff8000")
        self.btnBorrar.configure(disabledforeground="#a3a3a3")
        self.btnBorrar.configure(foreground="#000000")
        self.btnBorrar.configure(highlightbackground="#d9d9d9")
        self.btnBorrar.configure(highlightcolor="black")
        self.btnBorrar.configure(pady="0")
        self.btnBorrar.configure(command=lambda: borrarTexto())
        self.btnBorrar.configure(text='''B''')

        self.btnCopiar = tk.Button(top)
        self.btnCopiar.place(relx=0.977, rely=0.859, height=24, width=19)
        self.btnCopiar.configure(activebackground="#ececec")
        self.btnCopiar.configure(activeforeground="#000000")
        self.btnCopiar.configure(background="#ff8000")
        self.btnCopiar.configure(disabledforeground="#a3a3a3")
        self.btnCopiar.configure(foreground="#000000")
        self.btnCopiar.configure(highlightbackground="#d9d9d9")
        self.btnCopiar.configure(highlightcolor="black")
        self.btnCopiar.configure(pady="0")
        self.btnCopiar.configure(command=lambda: copiarTexto())
        self.btnCopiar.configure(text='''C''')

        self.txbTextoModificado = tk.Entry(top)
        self.txbTextoModificado.place(relx=0.485, rely=0.859, height=19
                , relwidth=0.440)
        self.txbTextoModificado.configure(background="white")
        self.txbTextoModificado.configure(disabledforeground="#a3a3a3")
        self.txbTextoModificado.configure(font="-family {Courier New} -size 10")
        self.txbTextoModificado.configure(foreground="#000000")
        self.txbTextoModificado.configure(highlightbackground="#d9d9d9")
        self.txbTextoModificado.configure(highlightcolor="black")
        self.txbTextoModificado.configure(insertbackground="black")
        self.txbTextoModificado.configure(selectbackground="#c4c4c4")
        self.txbTextoModificado.configure(textvariable = textoqueSustituira)
        self.txbTextoModificado.configure(selectforeground="black")

class AutoScroll(object):
    '''Configure the scrollbars for a widget.'''

    def __init__(self, master):
        #  Rozen. Added the try-except clauses so that this class
        #  could be used for scrolled entry widget for which vertical
        #  scrolling is not supported. 5/7/14.
        try:
            vsb = ttk.Scrollbar(master, orient='vertical', command = self.yview)
        except:
            pass
        hsb = ttk.Scrollbar(master, orient='horizontal', command = self.xview)

        #self.configure(yscrollcommand=_autoscroll(vsb),
        #    xscrollcommand=_autoscroll(hsb))
        try:
            self.configure(yscrollcommand = self._autoscroll(vsb))
        except:
            pass
        self.configure(xscrollcommand=self._autoscroll(hsb))

        self.grid(column=0, row=0, sticky='nsew')
        try:
            vsb.grid(column=1, row=0, sticky='ns')
        except:
            pass
        hsb.grid(column=0, row=1, sticky='ew')

        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)

        # Copy geometry methods of master  (taken from ScrolledText.py)
        if py3:
            methods = tk.Pack.__dict__.keys() | tk.Grid.__dict__.keys() \
                  | tk.Place.__dict__.keys()
        else:
            methods = tk.Pack.__dict__.keys() + tk.Grid.__dict__.keys() \
                  + tk.Place.__dict__.keys()

        for meth in methods:
            if meth[0] != '_' and meth not in ('config', 'configure'):
                setattr(self, meth, getattr(master, meth))

    @staticmethod
    def _autoscroll(sbar):
        '''Hide and show scrollbar as needed.'''
        def wrapped(first, last):
            first, last = float(first), float(last)
            if first <= 0 and last >= 1:
                sbar.grid_remove()
            else:
                sbar.grid()
            sbar.set(first, last)
        return wrapped

    def __str__(self):
        return str(self.master)

def _create_container(func):
    '''Creates a ttk Frame with a given master, and use this new frame to
    place the scrollbars and the widget.'''
    def wrapped(cls, master, **kw):
        container = ttk.Frame(master)
        container.bind('<Enter>', lambda e: _bound_to_mousewheel(e, container))
        container.bind('<Leave>', lambda e: _unbound_to_mousewheel(e, container))
        return func(cls, container, **kw)
    return wrapped

class ScrolledText(AutoScroll, tk.Text):
    '''A standard Tkinter Text widget with scrollbars that will
    automatically show/hide as needed.'''
    @_create_container
    def __init__(self, master, **kw):
        tk.Text.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)

import platform
def _bound_to_mousewheel(event, widget):
    child = widget.winfo_children()[0]
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        child.bind_all('<MouseWheel>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-MouseWheel>', lambda e: _on_shiftmouse(e, child))
    else:
        child.bind_all('<Button-4>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Button-5>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-Button-4>', lambda e: _on_shiftmouse(e, child))
        child.bind_all('<Shift-Button-5>', lambda e: _on_shiftmouse(e, child))

def _unbound_to_mousewheel(event, widget):
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        widget.unbind_all('<MouseWheel>')
        widget.unbind_all('<Shift-MouseWheel>')
    else:
        widget.unbind_all('<Button-4>')
        widget.unbind_all('<Button-5>')
        widget.unbind_all('<Shift-Button-4>')
        widget.unbind_all('<Shift-Button-5>')

def _on_mousewheel(event, widget):
    if platform.system() == 'Windows':
        widget.yview_scroll(-1*int(event.delta/120),'units')
    elif platform.system() == 'Darwin':
        widget.yview_scroll(-1*int(event.delta),'units')
    else:
        if event.num == 4:
            widget.yview_scroll(-1, 'units')
        elif event.num == 5:
            widget.yview_scroll(1, 'units')

def _on_shiftmouse(event, widget):
    if platform.system() == 'Windows':
        widget.xview_scroll(-1*int(event.delta/120), 'units')
    elif platform.system() == 'Darwin':
        widget.xview_scroll(-1*int(event.delta), 'units')
    else:
        if event.num == 4:
            widget.xview_scroll(-1, 'units')
        elif event.num == 5:
            widget.xview_scroll(1, 'units')

if __name__ == '__main__':
    vp_start_gui()




