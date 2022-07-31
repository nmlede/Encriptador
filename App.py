from cryptography.fernet import Fernet
import os

####################################################################
################ Funciones para mostrar informacion ################

def mostrar_mensajes_guardados():
    pwd=os.getcwd()
    pwd_str=os.listdir(pwd+'/Mensajes/')
    if len(pwd_str)>0:
        print('[INFO] Mensajes:')
        os.system('ls '+pwd+'/Mensajes | grep .txt')
    else:
        print('[INFO] No hay mensajes guardados.')
    return pwd_str


def mostrar_claves_guardadas():
    pwd=os.getcwd()
    pwd_str=os.listdir(pwd+'/Claves/')
    if len(pwd_str)>0:
        print('[INFO] Claves:')
        os.system('ls '+pwd+'/Claves | grep .key')
    else:
        print('[INFO] No hay claves guardadas.')
    return pwd_str


def mostrar_encriptados_guardados():
    pwd=os.getcwd()
    pwd_str=os.listdir(pwd+'/Encriptados/')
    if len(pwd_str)>0:
        print('[INFO] Encriptados:')
        os.system('ls '+pwd+'/Encriptados | grep .enc')
    else:
        print('[INFO] No hay mensajes encriptados guardados.')
    return pwd_str

####################################################################
############### Funciones para generar informacion #################

def generar_mensaje():
    nombre_mensaje=input('Ingrese el nombre del mensaje a generar: ')
    mensaje = input("Ingrese el mensaje original: ")
    with open(f"Mensajes/{nombre_mensaje}.txt","w") as archivo_mensaje:
        archivo_mensaje.write(mensaje)


def generar_clave():
    clave = Fernet.generate_key()
    nombre_clave=input('Ingrese el nombre de la clave a generar: ')
    with open(f"Claves/{nombre_clave}.key","wb") as archivo_clave:
        archivo_clave.write(clave)


def generar_encriptado(mensaje, fernet):
    mostrar_encriptados_guardados()
    encriptado = fernet.encrypt(mensaje)
    nombre_encriptado=input('Ingrese el nombre para el mensaje encriptado: ')
    with open(f"Encriptados/{nombre_encriptado}.enc","wb") as archivo_encriptado:
        archivo_encriptado.write(encriptado)

####################################################################
############## Funciones para cargar informacion ###################

def cargar_mensaje():
    pwd=mostrar_mensajes_guardados()
    if len(pwd)>0:
        nombre_mensaje=input('[INFO] Ingrese el nombre del mensaje a cargar: ')
        return open(f"Mensajes/{nombre_mensaje}.txt","rb").read(), nombre_mensaje


def cargar_clave():
    pwd=mostrar_claves_guardadas()
    if len(pwd)>0:
        nombre_clave=input('[INFO] Ingrese el nombre de la clave a cargar: ')
        return open(f"Claves/{nombre_clave}.key","rb").read()


def cargar_encriptado():
    pwd=mostrar_encriptados_guardados()
    if len(pwd)>0:
        nombre_encriptado=input('[INFO] Ingrese el nombre del mensaje encriptado a cargar: ')
        return open(f"Encriptados/{nombre_encriptado}.enc","rb").read()


####################################################################
################## Borrar toda la informacion ######################

def borrar_todo():
    pwd=os.getcwd()
    pwd_mensajes=os.listdir(pwd+'/Mensajes/')
    pwd_claves=os.listdir(pwd+'/Claves/')
    pwd_encriptados=os.listdir(pwd+'/Encriptados/')

    if len(pwd_mensajes)>0 and len(pwd_claves)>0 and len(pwd_encriptados)>0: 
        while True:
            borrar=input('[INFO] Desea borrar toda la informacion?: (y/n)')
            if borrar == 'y':
                os.system('rm '+pwd+'/Mensajes/*.txt')
                os.system('rm '+pwd+'/Claves/*.key')
                os.system('rm '+pwd+'/Encriptados/*.enc')
                print('[INFO] Todos los datos han sido eliminados.')
                break
            elif borrar=='n':
                print('[INFO] Los datos NO han sido borrados.')
                break
            else:
                print('[INFO] Opcion incorrecta, seleccione nuevamente.')
    else:
        print('[INFO] Los directorios no contienen archivos.')


####################################################################
########## Funciones para eventos encriptar/desencriptar ###########

def encriptar_mensaje():
    pwd=os.getcwd()
    pwd_mensajes=os.listdir(pwd+'/Mensajes/')
    seleccion=int(input('[INFO] Seleccione una opcion:\n1- Ingresar nuevo mensaje.\n2- Encriptar mensaje existente. \n'))
    if (seleccion == 1):
        print('[INFO] Ingresando nuevo mensaje.')
        generar_mensaje()
        generar_clave()
        mensaje, nombre_mensaje=cargar_mensaje()
        clave=cargar_clave()	
        fernet = Fernet(clave)
        generar_encriptado(mensaje, fernet)
        os.system(f'rm {pwd}/Mensajes/{nombre_mensaje}')    
 
    if (seleccion == 2):
        if len(pwd_mensajes)>0:
            mensaje, nombre_mensaje=cargar_mensaje()
            clave=cargar_clave()
            fernet=Fernet(clave)
            generar_encriptado(mensaje, fernet)  
            os.system(f'rm {pwd}/Mensajes/{nombre_mensaje}')  

        else:
            print('[INFO] No hay mensajes guardados.')
           


def desencriptar():
    pwd=os.getcwd()
    pwd_mensajes=os.listdir(pwd+'/Mensajes/')
    if len(pwd_mensajes)>0:
        encriptado = cargar_encriptado()    
        clave = cargar_clave()
        fernet = Fernet(clave)
        desencriptado = fernet.decrypt(encriptado)
        print("[INFO] Mensaje DESENCRIPTADO: \n",desencriptado)
    else:
        print('[INFO] No hay mensajes para desencriptar.')


####################################################################
############################# MAIN #################################

# if __name__=='__main__':
#     print("\n[INFO] Programa ENCRIPTADOR/DESENCRIPTADOR")
#     opcion = True
#     while (opcion):
#         try:
#             selector = int(input("[INFO] Seleccione una opcion:\n1- Encriptar nuevo mensaje.\n2- Encriptar mensaje existente.\n3- Desencriptar.\n"))
#             if(selector == 1):
#                 try:
#                     encriptar_nuevo_mensaje()
#                     print('[INFO] Mensaje encriptado')
#                 except Exception as error:
#                     print("[ERROR] No se ha podido encriptar el mensaje")
#                     print(f'[ERROR] {error}')
#                     break
#             elif(selector==2):
#                 try:
#                     encriptado_mensaje_existente()
#                     print('[INFO] Mensaje encriptado')
#                 except Exception as error:
#                     print('[ERROR] No se ha podido encriptar el mensaje')
#                     print(f'[ERROR] {error}')
#             elif(selector == 3):
#                 try:
#                     desencriptar()
#                     print(f'[INFO] Mensaje desencriptado')
#                 except FileNotFoundError as error:
#                     print(f"[ERROR] No se encontraron archivos encriptados")
#                     print(f"[ERROR] {error}")
#                     break
#             else:
#                 print("[ERROR] Opcion incorrecta, intente nuevamente")
        
#         except ValueError as error:
#             print("[ERROR] Opcion incorrecta, intente nuevamente")
#             print(f"[ERROR] {error}")

#         while True:
#             print("[INFO] Desea seleccionar otra opcion? (y/n): ")
#             opcion = input()
#             if (opcion == "y"):
#                 opcion=True 
#                 break
#             elif(opcion == "n"):
#                 opcion=False
#                 break
#             else:
#                 print("[ERROR] Opcion incorrecta, intente nuevamente")

# print("\n[INFO] Fin del programa")
