
from tkinter import filedialog
from tkinter import messagebox
from tkinter import filedialog as fd
from tkinter import messagebox as mb
import re

class Operativo():

    def __init__(self):
        pass 
    
    def sustitucionTexto(self,textoOriginal,texto1,texto2):
        textoSustituido = textoOriginal.replace(texto1, texto2)
        return textoSustituido 
        
    def realizandoProceso(self,Textos):
        ContenedorTexto = Operativo.cambiandoBullets(self,Textos) # Esta funcion cambia los bullets
        ContenedorTexto = Operativo.colocandoPuntosEnDondeNoLosHay(self,ContenedorTexto)
        ContenedorTexto = Operativo.cambiandoBulletsdeCinco(self,ContenedorTexto)
        ContenedorTexto= ContenedorTexto.replace('\x0c', '\n ') # templaza los saltos de pagina, por saltos de Linea
        ContenedorTexto = Operativo.limpiarTextodeSaltoLinea(self,ContenedorTexto) # quita los saltos de linea
        ContenedorTexto = Operativo.quitandoEspacios(self,ContenedorTexto) # quita los espacios de mas
        ContenedorTexto = Operativo.insertarSaltosdeLineaEstrategicos(self,ContenedorTexto) # despues de ciertos caracteres da saltos de linea
        ContenedorTexto = Operativo.Espacioencomasypuntos(self,ContenedorTexto)
        ContenedorTexto= Operativo.arreglandoNumros(self,ContenedorTexto)
        ContenedorTexto = Operativo.arregloIncisos(self,ContenedorTexto)
        return ContenedorTexto

    def colocandoPuntosEnDondeNoLosHay(self,ContenedorTexto):
        ContenedorTexto = ContenedorTexto +"XXX"
        Casilla3 = ""
        Casilla2 = ""
        Casilla1 = ""
        TextoFinal = ""
        for letra in ContenedorTexto:
                Final = Casilla3
                Casilla3 = Casilla2
                Casilla2 = Casilla1
                Casilla1 = letra
                if Casilla3.isupper() == True and Casilla2 == "\n" and Casilla1.islower == True:
                    Casilla3 = ".\n"
                    TextoFinal = TextoFinal + Final
                else:
                    TextoFinal = TextoFinal + Final
                    
        return TextoFinal
        
        
    def cambiandoBullets(self,CambiandolosPuntos):
            CambiandolosPuntos = CambiandolosPuntos +"XXXX"

            Casilla4 = ""
            Casilla3 = ""
            Casilla2 = ""
            Casilla1 = ""
            TextoFinal =""

            for letra in CambiandolosPuntos:

                Final = Casilla4
                Casilla4 = Casilla3
                Casilla3 = Casilla2
                Casilla2 = Casilla1
                Casilla1 = letra
                if Casilla4 == "\n" and Casilla3 == "." and Casilla2 == " " and Casilla1.isupper() == True :
                    Casilla3 = "•"
                    TextoFinal = TextoFinal +Final
                elif Casilla4 == "\n" and Casilla3 == "o" and Casilla2 == " " and Casilla1.isupper() == True :
                    Casilla3 = "•"
                    TextoFinal = TextoFinal +Final
                elif Casilla4 == "\n" and Casilla3 == "-" and Casilla2 == " " and Casilla1.isupper() == True :
                    Casilla3 = "•"
                    TextoFinal = TextoFinal + Final
                elif Casilla4.islower() == True and Casilla3 == " " and Casilla2 == "\n" and Casilla1 == "\n" :
                        Casilla3 = ".\n"
                        TextoFinal = TextoFinal + Final    
                else:
                    TextoFinal = TextoFinal + Final
                    
            return TextoFinal

    def cambiandoBulletsdeCinco(self,CambiandolosPuntos):
            Casilla5 = ""
            Casilla4 = ""
            Casilla3 = ""
            Casilla2 = ""
            Casilla1 = ""
            TextoFinal =""

            for letra in CambiandolosPuntos:

                Final = Casilla5
                Casilla5 = Casilla4
                Casilla4 = Casilla3
                Casilla3 = Casilla2
                Casilla2 = Casilla1
                Casilla1 = letra

                if Casilla5 == "\n" and Casilla4 == "." and Casilla3 == " " and Casilla2 == "\n"  and Casilla1.isupper() == True :
                    Casilla4 = "•"
                    TextoFinal = TextoFinal +Final
                elif Casilla5 == "\n" and Casilla4 == "o" and Casilla3 == " " and Casilla2 == "\n"   and Casilla1.isupper() == True :
                    Casilla4 = "•"
                    TextoFinal = TextoFinal +Final
                elif Casilla5 == "\n" and Casilla4 == "-" and Casilla3 == " " and Casilla2 == "\n"   and Casilla1.isupper() == True :
                    Casilla4 = "•"
                    TextoFinal = TextoFinal +Final
                else:
                    TextoFinal = TextoFinal +Final
                    
            return TextoFinal

    def limpiarTextodeSaltoLinea(self,TextoaLimpiar):
        TextoLimpio = ""
        for linea in TextoaLimpiar:
            if linea[-1]== '\n':
                linea=linea[:-1]
            TextoLimpio = TextoLimpio + linea
        return TextoLimpio

    def quitandoEspacios(self,TextoaTrabajar):
        TextoaTrabajar = TextoaTrabajar +"XXX"
        TextoFinal = ""

        Quitandodosespacios = TextoaTrabajar.replace('  ', ' ')
        Quitandotresespacios = Quitandodosespacios.replace('   ', ' ')
        QuitandoCuatroespacios = Quitandotresespacios.replace('    ', ' ')
        TextoFinal = QuitandoCuatroespacios.replace('     ', ' ')
                
        return TextoFinal

    def insertarSaltosdeLineaEstrategicos(self,RegresoLimpiarTexto):

        ContenedorTexto = RegresoLimpiarTexto
        ContenedorTexto = ContenedorTexto.replace('. ', '.\n\n')
        ContenedorTexto = ContenedorTexto.replace('p.\n\n', 'p.')
        ContenedorTexto = ContenedorTexto.replace('! ', '!\n\n')
        ContenedorTexto = ContenedorTexto.replace('? ', '?\n\n')
        ContenedorTexto = ContenedorTexto.replace(': ', ':\n\n')
        ContenedorTexto = ContenedorTexto.replace('.png', '.png\n\n')
        ContenedorTexto = ContenedorTexto.replace('.jpg', '.jpg\n\n')
        ContenedorTexto = ContenedorTexto.replace('.pdf', '.pdf\n\n')
        ContenedorTexto = ContenedorTexto.replace('y/o', 'y, o')
        ContenedorTexto = ContenedorTexto.replace('(', '( ')
        ContenedorTexto = ContenedorTexto.replace(')', ' )')

        return ContenedorTexto

    def Espacioencomasypuntos(self,CambiandolosPuntos):
            CambiandolosPuntos = CambiandolosPuntos +"XXXX"

            Casilla4 = ""
            Casilla3 = ""
            Casilla2 = ""
            Casilla1 = ""
            TextoFinal =""

            for letra in CambiandolosPuntos:

                Final = Casilla4
                Casilla4 = Casilla3
                Casilla3 = Casilla2
                Casilla2 = Casilla1
                Casilla1 = letra

                if Casilla4.islower() == True and Casilla3 == "," and Casilla2.islower() == True  :
                        Casilla3 = ", "
                        TextoFinal = TextoFinal + Final    

                if Casilla4.islower() == True and Casilla3 == "." and Casilla2.isupper() == True  :
                        Casilla3 = ".\n"
                        TextoFinal = TextoFinal + Final    
                else:
                    TextoFinal = TextoFinal + Final
                    
            return TextoFinal

    def arreglandoNumros(self,CambiandolosPuntos):
            Casilla4 = ""
            Casilla3 = ""
            Casilla2 = ""
            Casilla1 = ""
            TextoFinal =""

            for letra in CambiandolosPuntos:

                Final = Casilla4
                Casilla4 = Casilla3
                Casilla3 = Casilla2
                Casilla2 = Casilla1
                Casilla1 = letra
                if Casilla4.isnumeric() == True  and Casilla3 == "." and Casilla2 == "\n" and Casilla1 == "\n" :
                    Casilla2 = " "
                    Casilla1 = ""
                    TextoFinal = TextoFinal +Final
                if Casilla4.islower() == True  and Casilla3 == "." and Casilla2.isupper() == True and Casilla1.islower() == True :
                    Casilla3 == ".\n\n"
                    TextoFinal = TextoFinal + Final
                else:
                    TextoFinal = TextoFinal + Final
                    
            return TextoFinal

    def arregloIncisos(self,texto):
        texto=texto + "XXXXXX"
        Casilla6 = " "
        Casilla5 = " "
        Casilla4 = " "
        Casilla3 = " "
        Casilla2 = " "
        Casilla1 = " "
        Final = " "
        verificar = ""
        TextoFinal = ""

        for letra in texto:
            Final = Casilla6
            Casilla6 = Casilla5
            Casilla5 = Casilla4
            Casilla4 = Casilla3
            Casilla3 = Casilla2
            Casilla2 = Casilla1
            Casilla1 = letra
            verificar = ""

            verificar = Casilla6 + Casilla5 + Casilla4

            DatoaVerificar = re.compile(r'\.\d\.')
            comprobar = DatoaVerificar.search(verificar)
            
            if comprobar != None and Casilla3 == "\n" and Casilla2 == "\n" and Casilla1.isupper() == True :
                Casilla3 = " "
                Casilla2 = " "
                TextoFinal = TextoFinal +Final
            else:
                TextoFinal = TextoFinal +Final
                
        return TextoFinal

    def CargandoCasillas(self,texto):
       
        Casilla6 = ""
        Casilla5 = ""
        Casilla4 = ""
        Casilla3 = ""
        Casilla2 = ""
        Casilla1 = ""
        Final = ""
        TextoFinal = ""
        texto = texto + "XXXXXX"
    
        for letra in texto:
            Final = Casilla6
            Casilla6 = Casilla5
            Casilla5 = Casilla4
            Casilla4 = Casilla3
            Casilla3 = Casilla2
            Casilla2 = Casilla1
            Casilla1 = letra
            if Casilla6 != "":
                TextoFinal = TextoFinal + Final
        return TextoFinal
        