import datetime
import os
import re
import unicodedata


def cambiar_texto_a_sin_acentos(texto):
    """ A caracteres sin acentos """
    texto = unicodedata.normalize('NFD', texto)
    texto = texto.encode('ascii', 'ignore')
    texto = texto.decode("utf-8")
    return(str(texto))

def cambiar_texto_a_ruta_segura(texto):
    """ A una ruta segura en minúsculas, espacios a guiones y sin caracteres acentuados, pero mantiene diagonales """
    texto = cambiar_texto_a_sin_acentos(texto.lower())
    texto = re.sub('[ ]+', '-', texto)
    texto = re.sub('[^0-9a-zA-Z_/-]', '', texto)
    return(texto)

def cambiar_texto_a_identificador(texto):
    """ A identificador en minúsculas, espacios a guiones y sin caracteres acentuados """
    texto = cambiar_texto_a_sin_acentos(texto.lower())
    texto = re.sub('[/]+', '-', texto)
    texto = re.sub('[ ]+', '-', texto)
    texto = re.sub('[^0-9a-zA-Z_-]', '', texto)
    return(texto)

def cambiar_texto_a_palabras_en_mayusculas(texto):
    """ El primer caracter de cada palabra en mayúscula, el resto en minúsculas, guiones a espacios """
    texto = re.sub('[-]+', ' ', texto)
    return(texto.title())
