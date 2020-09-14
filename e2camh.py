"""
https://github.com/wolf9846/programacionparaciberseguridad
Carlos Mz H
este script hace consultas a la pagina de noticias de la UANL en un rango
especifico dado por el ususario donde si el rango inicial es mayor que
el final solo se tomara el final.
primero realizara una peticion para determinar el estatus de la pagina
si no esta en rango arroja el mensaje de pagina no encontrada, si esta en
rango busca los encabezados h3 de HTMl , despues busca los enlaces para
finalmente dar con los parrafos y abrir
"""

try:
    import os
    import sys
except ImportError:
    os.system('pip install os-sys')
    print('Installing os-sys...')
    print('Ejecuta de nuevo tu script...')
    sys.exit()

try:
    import requests
except ImportError:
    os.system('pip install requests')
    print('Installing requests...')
    print('Ejecuta de nuevo tu script...')
    sys.exit()

try:
    import webbrowser
except ImportError:
    os.system('pip install webbrowser')
    print('Installing webbrowser...')
    print('Ejecuta de nuevo tu script...')
    sys.exit()

try:
    from bs4 import BeautifulSoup as bs
except ImportError:
    os.system('pip install beautifulsoup4')
    print('Installing BeautifulSoup...')
    print('Ejecuta de nuevo tu script...')
    sys.exit()

print("Este script navega en las páginas de noticas de la UANL")
INICIORANGO = int(input("Pagina inicial para buscar: "))
FINRANGO = int(input("Pagina final para buscar: "))
DEPENDENCIA = input("Ingrese las siglas de la Facultad a buscar: ")
if INICIORANGO > FINRANGO:
    INICIORANGO, FINRANGO = FINRANGO, INICIORANGO
for i in range(INICIORANGO, FINRANGO, 1):
    url = "https://www.uanl.mx/noticias/page/"+str(i)
    pagina = requests.get(url)
    if pagina.status_code != 200:
        raise TypeError("Pagina no encontrada")
    if pagina.status_code == 200:
        soup = bs(pagina.content, "html.parser")
        info = soup.select("h3 a")
        for etiqueta in info:
            url2 = etiqueta.get("href")
            pagina2 = requests.get(url2)
            if pagina2.status_code == 200:
                soup2 = bs(pagina2.content, "html.parser")
                parrafos = soup2.select("p")

                for elemento in parrafos:
                    if DEPENDENCIA in elemento.getText():
                        print("Abriendo", url2)
                        webbrowser.open(url2)
                        break
