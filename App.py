####################################################################
########################### Librerias ##############################

from cryptography.fernet import Fernet
import os

####################################################################
########################### Detalles ###############################

#[INFO] = informacion.
#[ACC] = accion, ingreso de datos, decision de usuario.
#[ERROR] = error.
FOLDERS=['/Mensajes/','/Claves/','/Encriptados/']

####################################################################
################ Funciones para mostrar informacion ################

def mostrar_mensajes_guardados():
    pwd=os.getcwd()
    pwd_str=os.listdir(pwd+FOLDERS[0])
    
    if len(pwd_str)>0:
        print('[INFO] Mensajes:')
        os.system('ls '+pwd+'/Mensajes | grep .txt')
    else:
        print('[INFO] No hay mensajes guardados.')
    return pwd_str


def mostrar_claves_guardadas():
    pwd=os.getcwd()
    pwd_str=os.listdir(pwd+FOLDERS[1])
    
    if len(pwd_str)>0:
        print('[INFO] Claves:')
        os.system('ls '+pwd+'/Claves | grep .key')
    else:
        print('[INFO] No hay claves guardadas.')
    return pwd_str


def mostrar_encriptados_guardados():
    pwd=os.getcwd()
    pwd_str=os.listdir(pwd+FOLDERS[2])
    
    if len(pwd_str)>0:
        print('[INFO] Encriptados:')
        os.system('ls '+pwd+'/Encriptados | grep .enc')
    else:
        print('[INFO] No hay mensajes encriptados guardados.')
    return pwd_str

####################################################################
############### Funciones para generar informacion #################

def generar_mensaje():
    nombre_mensaje=input('[INFO] Ingrese el nombre del mensaje a generar: ')
    mensaje = input("[ACC] Ingrese el contenido del mensaje: ")
    with open(f"Mensajes/{nombre_mensaje}.txt","w") as archivo_mensaje:
        archivo_mensaje.write(mensaje)
    print('[INFO] Mensaje generado.')


def generar_clave():
    clave = Fernet.generate_key()
    nombre_clave=input('[ACC] Ingrese el nombre de la clave a generar: ')
    with open(f"Claves/{nombre_clave}.key","wb") as archivo_clave:
        archivo_clave.write(clave)
    print('[INFO] Clave generada.')


def generar_encriptado(mensaje, fernet):
    mostrar_encriptados_guardados()
    encriptado = fernet.encrypt(mensaje)
    nombre_encriptado=input('[ACC] Ingrese el nombre del encriptado a generar: ')
    with open(f"Encriptados/{nombre_encriptado}.enc","wb") as archivo_encriptado:
        archivo_encriptado.write(encriptado)
    print('[INFO] Encriptado generado.')

####################################################################
############## Funciones para cargar informacion ###################

def cargar_mensaje():
    pwd=mostrar_mensajes_guardados()
    
    if len(pwd)>0:
        nombre_mensaje=input('[ACC] Ingrese el nombre del mensaje a cargar: ')
        print('[INFO] Mensaje cargado.')
        return open(f"Mensajes/{nombre_mensaje}.txt","rb").read(), nombre_mensaje


def cargar_clave():
    pwd=mostrar_claves_guardadas()
    
    if len(pwd)>0:
        nombre_clave=input('[ACC] Ingrese el nombre de la clave a cargar: ')
        print('[INFO] Clave cargada.')
        return open(f"Claves/{nombre_clave}.key","rb").read()


def cargar_encriptado():
    pwd=mostrar_encriptados_guardados()
    
    if len(pwd)>0:
        nombre_encriptado=input('[ACC] Ingrese el nombre del mensaje encriptado a cargar: ')
        print('[INFO] Encriptado cargado.')
        return open(f"Encriptados/{nombre_encriptado}.enc","rb").read()


####################################################################
################## Borrar toda la informacion ######################

def borrar_informacion():
    pwd=os.getcwd()
    print('[INFO] Borrar informacion.\n')
    
    while True:
        print('[ACC] Seleccione una opcion:')
        borrar=int(input('1- Mensajes.\n2- Claves.\n3- Encriptados.\n'))
        
        if (borrar==1):
            pwd_mensajes=os.listdir(pwd+FOLDERS[0])
            if len(pwd_mensajes)>0:
                os.system('rm '+pwd+FOLDERS[0]+'*.txt')
                print(f'[INFO] El contenido en {FOLDERS[0]} ha sido eliminado.')
            else:
                print(f'[INFO] El directorio {FOLDERS[0]} esta vacio.')
            break
        
        elif (borrar==2):
            pwd_claves=os.listdir(pwd+FOLDERS[1])
            if len(pwd_claves)>0:
                os.system('rm '+pwd+FOLDERS[1]+'*.key')
                print(f'[INFO] El contenido en {FOLDERS[1]} ha sido eliminado.')
            else:
                print(f'[INFO] El directorio {FOLDERS[1]} esta vacio.')
            break

        elif (borrar==3):
            pwd_encriptados=os.listdir(pwd+FOLDERS[2])
            if len(pwd_encriptados)>0:
                os.system('rm '+pwd+FOLDERS[2]+'*.enc')
                print(f'[INFO] El contenido en {FOLDERS[2]} ha sido eliminado.')
            else:
                print(f'[INFO] El directorio {FOLDERS[2]} esta vacio.')
            break
        
        else:
            print('[ERROR] Opcion incorrecta, seleccione nuevamente.')

####################################################################
########## Funciones para eventos encriptar/desencriptar ###########

def encriptar_mensaje():
    pwd=os.getcwd()
    pwd_mensajes=os.listdir(pwd+FOLDERS[0])
    seleccion=int(input('[ACC] 1- Ingresar nuevo mensaje.\n2- Encriptar mensaje existente. \n'))
    
    if (seleccion == 1):
        print('[INFO] Ingresando nuevo mensaje.')
        generar_mensaje()
        generar_clave()
        mensaje, nombre_mensaje=cargar_mensaje()
        clave=cargar_clave()	
        fernet = Fernet(clave)
        generar_encriptado(mensaje, fernet)
        os.system(f'rm {pwd}/Mensajes/{nombre_mensaje}.txt')    
 
    if (seleccion == 2):
        if len(pwd_mensajes)>0:
            mensaje, nombre_mensaje=cargar_mensaje()
            clave=cargar_clave()
            fernet=Fernet(clave)
            generar_encriptado(mensaje, fernet)  
            os.system(f'rm {pwd}/Mensajes/{nombre_mensaje}.txt')  
        else:
            print('[INFO] No hay mensajes guardados.')
           


def desencriptar():
    pwd=os.getcwd()
    pwd_encriptados=os.listdir(pwd+FOLDERS[2])
    
    if len(pwd_encriptados)>0:
        encriptado = cargar_encriptado()    
        clave = cargar_clave()
        fernet = Fernet(clave)
        desencriptado = fernet.decrypt(encriptado)
        print("[INFO] Mensaje DESENCRIPTADO: \n",desencriptado)
    else:
        print('[INFO] No hay mensajes para desencriptar.')


