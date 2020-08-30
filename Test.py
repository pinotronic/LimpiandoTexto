#from Proceso import *

def CargandoCasillas(texto):
       
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


texto ="abcdefghijklmnñopqrstuvwxyz"
print(CargandoCasillas(texto))
