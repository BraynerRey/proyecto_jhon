from cryptography.fernet import Fernet
import os


def retornarkey():
    return open("key.key", "rb").read()


def decrypt(items, key):
    i = Fernet(key)
    for x in items:
        with open(x, "rb") as file:
            file_data = file.read()
        data = i.decrypt(file_data)

        with open(x, "wb") as file:
            file.write(data) 

def PrincipalDeseado():
    if __name__ == "__main__":
        print("Ingrese el nombre del archivo con su extensión")
        nombrearchivo = input()
        archivos = 'C:\\Users\\Brayner\\Desktop\\Nueva'
        os.remove(archivos+"\\"+"readme.txt")
        ##items = os.listdir(archivos)
        archivos_2 = [archivos+'\\'+nombrearchivo]
    ## archivos_2 = [archivos+"\\"+x for x in items]
    ##archivos+"\\"+x for x in items
    ##'C:\\Users\\Brayner\\Desktop\\Nueva\\ggg.txt'

    key = retornarkey()

    decrypt(archivos_2, key)

def PrincipalUnico():
    if __name__ == "__main__":
        ##nombrearchivo = input()
        archivos_2 = 'C:\\Users\\Brayner\\Desktop\\Nueva'
        archivos = ['C:\\Users\\Brayner\\Desktop\\Nueva\\ggg.txt']
        os.remove(archivos_2+"\\"+"readme.txt")
        ##items = os.listdir(archivos)
       ## archivos_2 = [archivos+'\\'+nombrearchivo]
    ## archivos_2 = [archivos+"\\"+x for x in items]
    ##archivos+"\\"+x for x in items
    ##'C:\\Users\\Brayner\\Desktop\\Nueva\\ggg.txt'

    key = retornarkey()

    decrypt(archivos, key)

def PrincipalTodos():
    if __name__ == "__main__":
       ## nombrearchivo = input()
        archivos = 'C:\\Users\\Brayner\\Desktop\\Nueva'
        os.remove(archivos+"\\"+"readme.txt")
        items = os.listdir(archivos)
        archivos_2 = [archivos+'\\'+x for x in items]
    ## archivos_2 = [archivos+"\\"+x for x in items]
    ##archivos+"\\"+x for x in items
    ##'C:\\Users\\Brayner\\Desktop\\Nueva\\ggg.txt'

    key = retornarkey()

    decrypt(archivos_2, key)

lcvalor = 0
print("----Desencriptar de archivos----")
print("Seleccione alguna opcion:")
print("Desencriptar Un solo archivo:1")
print("Desencriptar archivo deseado:2")
print("Desencriptar Todo           :3")
print("Salir                       :4")
lcvalor = int(input())
if lcvalor == 1:
    PrincipalUnico()
    print("Desencriptar finalizado")
elif lcvalor == 2:
    PrincipalDeseado()
    print("Desencriptar finalizado")
elif lcvalor == 3:
    PrincipalTodos()
    print("Desencriptar finalizado")
elif lcvalor == 4:
    print("Desencriptar finalizado")
