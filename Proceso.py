
from tkinter import filedialog
from tkinter import messagebox
from tkinter import filedialog as fd
from tkinter import messagebox as mb
from BarraProgreso import *
import re

class Operativo():

    def __init__(self):
        pass 
    
    def sustitucionTexto(self,textoOriginal,texto1,texto2):
        textoSustituido = textoOriginal.replace(texto1, texto2)
        return textoSustituido 
        
    def realizandoProceso(self,Textos):

        ContenedorTexto = Textos.replace(',', ', ')    
        ContenedorTexto = ContenedorTexto.replace('\uf0fc ', '') 
        ContenedorTexto = Operativo.cambiandoBullets(self,ContenedorTexto)
        ContenedorTexto = Operativo.colocandoPuntosDespuesRenglon(self,ContenedorTexto)
        ContenedorTexto  = ' '.join(ContenedorTexto.split())        
        ContenedorTexto = Operativo.colocandoPuntosEnDondeNoLosHay(self,ContenedorTexto) 
        ContenedorTexto = Operativo.cambiandoBulletsdeCinco(self,ContenedorTexto)
        ContenedorTexto= ContenedorTexto.replace('\x0c', '\n ') 
        ContenedorTexto = Operativo.limpiarTextodeSaltoLinea(self,ContenedorTexto) 
        ContenedorTexto = Operativo.arreglandoNumros(self,ContenedorTexto)
        ContenedorTexto = Operativo.arregloIncisos(self,ContenedorTexto)
        ContenedorTexto = Operativo.insertarSaltosdeLineaEstrategicos(self,ContenedorTexto) 
        ContenedorTexto = ContenedorTexto.lstrip()

        return ContenedorTexto

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
                # \n . " " M
                if Casilla4 == "\n" and Casilla3 == "." and Casilla2 == " " and Casilla1.isupper() == True :
                    Casilla3 = Casilla3.replace('.', '•') 
                    TextoFinal = TextoFinal +Final
                    # \n o " " M
                elif Casilla4 == "\n" and Casilla3 == "o" and Casilla2 == " " and Casilla1.isupper() == True :
                    Casilla3 = Casilla3.replace('o', '•') 
                    TextoFinal = TextoFinal +Final
                    # \n - " " M
                elif Casilla4 == "\n" and Casilla3 == "-" and Casilla2 == " " and Casilla1.isupper() == True :
                    Casilla3 = Casilla3.replace('-', '•') 
                    TextoFinal = TextoFinal + Final
                elif Casilla4 == "\n" and Casilla3 == "*" and Casilla2 == " " and Casilla1.isupper() == True :
                    Casilla3 = Casilla3.replace('*', '•') 
                    TextoFinal = TextoFinal + Final
                    # m " " \n \n
                elif Casilla4.islower() == True and Casilla3 == " " and Casilla2 == "\n" and Casilla1 == "\n" :
                    Casilla3 = Casilla3.replace(' ', '.\n') 
                    TextoFinal = TextoFinal + Final    
                elif Casilla4.islower() == True and Casilla3 == "." and Casilla2.isupper() == True  and Casilla1.islower() == True :
                    Casilla3 = Casilla3.replace('.', '. ') 
                    Casilla3 = ". "
                    TextoFinal = TextoFinal + Final    
                else:
                    TextoFinal = TextoFinal + Final

                    
            return TextoFinal

    def colocandoPuntosDespuesRenglon(self,ContenedorTexto):
        #ContenedorTexto  = '\n'.join(ContenedorTexto.split()) 
        ContenedorTexto = ContenedorTexto +"XX"
        Casilla2 = ""
        Casilla1 = ""
        TextoFinal = ""
        for letra in ContenedorTexto:
                Final = Casilla2
                Casilla2 = Casilla1
                Casilla1 = letra
                # M \n m
                if Casilla2 == "\n" and Casilla1.isupper() == True:
                    Casilla2 = Casilla2.replace('\n', '.\n') 
                    TextoFinal = TextoFinal + Final
                else:
                    TextoFinal = TextoFinal + Final
                    
        return TextoFinal

    def colocandoPuntosEnDondeNoLosHay(self,ContenedorTexto):
        ContenedorTexto = ContenedorTexto +"XXXX"
        Casilla4 = ""
        Casilla3 = ""
        Casilla2 = ""
        Casilla1 = ""
        TextoFinal = ""

        for letra in ContenedorTexto:
                Final = Casilla4
                Casilla4 = Casilla3
                Casilla3 = Casilla2
                Casilla2 = Casilla1
                Casilla1 = letra
                # M \n m
                if Casilla4.islower() == True and Casilla3 == "\n" and Casilla2.isupper() == True and Casilla1.islower() == True:
                    Casilla3 = Casilla3.replace('\n', '.')  
                    TextoFinal = TextoFinal + Final

                else:
                    TextoFinal = TextoFinal + Final
                    
        return TextoFinal

    def cambiandoBulletsdeCinco(self,CambiandolosPuntos):
            CambiandolosPuntos = CambiandolosPuntos +"xxxxx"
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

                # \n . " " \n M
                if Casilla5 == "\n" and Casilla4 == "." and Casilla3 == " " and Casilla2 == "\n"  and Casilla1.isupper() == True :
                    Casilla4 = Casilla4.replace(".","•")
                    TextoFinal = TextoFinal +Final
                    # \n o " " \n M
                elif Casilla5 == "\n" and Casilla4 == "o" and Casilla3 == " " and Casilla2 == "\n"   and Casilla1.isupper() == True :
                    Casilla4 = Casilla4.replace("o","•")
                    TextoFinal = TextoFinal +Final
                    # \n - " " \n M
                elif Casilla5 == "\n" and Casilla4 == "-" and Casilla3 == " " and Casilla2 == "\n"   and Casilla1.isupper() == True :
                    Casilla4 = Casilla4.replace("-","•")
                    TextoFinal = TextoFinal +Final
                elif Casilla5 == "\n" and Casilla4 == "*" and Casilla3 == " " and Casilla2 == "\n"   and Casilla1.isupper() == True :
                    Casilla4 = Casilla4.replace("*","•")
                    TextoFinal = TextoFinal +Final
                elif Casilla5.islower() == True and Casilla4 == " " and Casilla3 == "\n " and Casilla2 == "\n"   and Casilla1.isupper() == True :
                    Casilla4 = ".\n"
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

    def arreglandoNumros(self,CambiandolosPuntos):
            CambiandolosPuntos = CambiandolosPuntos +"xxxx"
            Casilla4 = ""
            Casilla3 = ""
            Casilla2 = ""
            Casilla1 = ""
            TextoFinal = ""

            for letra in CambiandolosPuntos:

                Final = Casilla4
                Casilla4 = Casilla3
                Casilla3 = Casilla2
                Casilla2 = Casilla1
                Casilla1 = letra
                # 8 . \n \n
                if Casilla4.isnumeric() == True  and Casilla3 == "." and Casilla2 == "\n" and Casilla1 == "\n" :
                    Casilla3 = Casilla3.replace('.', '.')  
                    TextoFinal = TextoFinal +Final
                # m . M m
                if Casilla4.isnumeric() == True  and Casilla3 == "." and Casilla2 == " " and Casilla1.isupper() == True :
                    Casilla3 = Casilla3.replace('.', '.')  
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
            # \n \n M
            if comprobar != None and Casilla3 == "\n" and Casilla2 == "\n" and Casilla1.isupper() == True :
                Casilla3 = " "
                Casilla2 = " "
                TextoFinal = TextoFinal +Final
            else:
                TextoFinal = TextoFinal +Final
                
        return TextoFinal

    def insertarSaltosdeLineaEstrategicos(self,RegresoLimpiarTexto):

        ContenedorTexto = RegresoLimpiarTexto
        ContenedorTexto = ContenedorTexto.replace("•","\n•")
        ContenedorTexto = ContenedorTexto.replace("-\n","")
        ContenedorTexto = ContenedorTexto.replace("- \n","")
        ContenedorTexto = ContenedorTexto.replace("- ","")
        ContenedorTexto = ContenedorTexto.replace('.)', ').')
        ContenedorTexto = ContenedorTexto.replace('."', '".')
        ContenedorTexto = ContenedorTexto.replace('!', '!\n')
        ContenedorTexto = ContenedorTexto.replace('¿','\n¿')
        ContenedorTexto = ContenedorTexto.replace('?', '?\n')
        ContenedorTexto = ContenedorTexto.replace(':', ':\n')
        ContenedorTexto = ContenedorTexto.replace('y/o', 'y, o')
        ContenedorTexto = ContenedorTexto.replace('y / o', 'y, o')
        ContenedorTexto = ContenedorTexto.replace('(', '( ')
        ContenedorTexto = ContenedorTexto.replace(')', ' )')
        ContenedorTexto = ContenedorTexto.replace('}', '}\n')
        ContenedorTexto = ContenedorTexto.replace('. .', '.')
        ContenedorTexto = ContenedorTexto.replace('.', '.\n')
        ContenedorTexto = ContenedorTexto.replace('\npng', 'png')
        ContenedorTexto = ContenedorTexto.replace('\njpg', 'jpg')
        ContenedorTexto = ContenedorTexto.replace('\npdf', 'pdf')
        ContenedorTexto = ContenedorTexto.replace('\n.\n', '\n')

        return ContenedorTexto



