import re
from bs4 import BeautifulSoup
import selenium.common.exceptions


def fun_titulo(elemento):
    titulo = (elemento.find_element_by_id('vjs-jobtitle')).text
    return titulo

def company(elemento):
    try:
        empresa = (((elemento.find_element_by_class_name('sjcl')).find_element_by_class_name('company'))).text
    except selenium.common.exceptions.NoSuchElementException:
        empresa = 'No registra'
    return empresa

def rating(elemento):
    try:
        puntuacion = (((elemento.find_element_by_class_name('sjcl')).find_element_by_class_name('ratingsDisplay'))).text
    except:
        puntuacion = 'No disponible'
    return puntuacion
#<span class="location accessible-contrast-color-location xh-highlight">Dallas, TX</span>
def ciudad(elemento):
    try:
        x = (elemento.find_element_by_class_name('sjcl')).text
        q = re.findall(r'\n(.*)', x)[0]
        if '(' in q:
            ciudad = re.findall(r'(.*)\(', q)[0]
        else:
            ciudad = q
    except:
        ciudad = 'No disponible'
    return ciudad


def fun_paga(element):
    try:
        pago = (element.find_element_by_class_name('salaryText')).text
    except:
        pago = 'No registra salario'
    return pago

def descripcion(elemento):
    resumen = (elemento.find_element_by_class_name('summary')).text
    return resumen

def resumen(recuadro):
    resumen_completo = re.sub(r'\nDenunciar empleo', '', (recuadro.find_element_by_id('vjs-content')).text)
    return resumen_completo
