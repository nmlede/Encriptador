from cryptography.fernet import Fernet


# FUNCION PARA ESCRIBIR Y GUARDAR CLAVE.
def generarClave():
    clave = Fernet.generate_key()
    with open("clave.key","wb") as archivoClave:
        archivoClave.write(clave)
        

# FUNCION PARA ESCRIBIR Y GUARDAR MENSAJE.
def generarMensaje():
    mensaje = input("Ingrese el mensaje original: ")
    with open("mensaje.txt","w") as archivoMensaje:        
        archivoMensaje.write(mensaje)
        

# FUNCION PARA CARGAR CLAVE.
def cargarClave():
    return open("clave.key","rb").read()


# FUNCION PARA CARGAR MENSAJE.
def cargarMensaje():
    return open("mensaje.txt","rb").read()


# FUNCION PARA ESCRIBIR Y GUARDAR MENSAJE ENCRIPTADO.
def generarEncriptado():
    encriptado = fernet.encrypt(mensaje)
    with open("encriptado.txt","wb") as archivoEncriptado:
        archivoEncriptado.write(encriptado)

# FUNCION PARA CARGAR MENSAJE ENCRIPTADO.
def cargarEncriptado():
    return open("encriptado.txt","rb").read()



print("\nPrograma ENCRIPTADOR/DESENCRIPTADOR")

otraOpcion = "y"

while (otraOpcion == "y"):

    while True:

        try:
            selector = int(input("\nSeleccione una opcion:\n1- Encriptar.\n2- Desencriptar.\n"))
            if(selector == 1):
                generarClave()
                generarMensaje()                
                clave = cargarClave()
                mensaje = cargarMensaje()
                fernet = Fernet(clave)
                generarEncriptado()
                encriptado = cargarEncriptado()
                print("\nMensaje ENCRIPTADO: \n",encriptado)
                break
            
            elif(selector == 2):
                try:
                    encriptado = cargarEncriptado()    
                    clave = cargarClave()
                    fernet = Fernet(clave)
                    desencriptado = fernet.decrypt(encriptado)
                    print("\nMensaje DESENCRIPTADO: \n",desencriptado)
                    break
                except FileNotFoundError:
                    print("No se encontraron archivos encriptados")
                    break
            else:
                print("\nOpcion incorrecta, intente nuevamente")
        
        except ValueError:
            print("\nOpcion incorrecta, intente nuevamente")

    print("\nDesea seleccionar otra opcion? (y/n): ")
    while True:
        otraOpcion = input()
        if (otraOpcion == "y" or otraOpcion == "n"):
            break
        else:
            print("\nOpcion incorrecta, intente nuevamente")

print("\nFin del programa")

"""
TODO: 
    Modularizar las funciones e importar el modulo. 
    Crear .exe con paquetes distribuibles.
    Agregar GUI
"""
