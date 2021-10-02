from cryptography.fernet import Fernet


# FUNCION PARA ESCRIBIR Y GUARDAR CLAVE.
def generar_clave():
    clave = Fernet.generate_key()
    with open("clave.key","wb") as archivo_clave:
        archivo_clave.write(clave)
        

# FUNCION PARA ESCRIBIR Y GUARDAR MENSAJE.
def generar_mensaje():
    mensaje = input("Ingrese el mensaje original: ")
    with open("mensaje.txt","w") as archivo_mensaje:        
        archivo_mensaje.write(mensaje)
        

# FUNCION PARA CARGAR CLAVE.
def cargar_clave():
    return open("clave.key","rb").read()


# FUNCION PARA CARGAR MENSAJE.
def cargar_mensaje():
    return open("mensaje.txt","rb").read()


# FUNCION PARA ESCRIBIR Y GUARDAR MENSAJE ENCRIPTADO.
def generar_encriptado():
    encriptado = fernet.encrypt(mensaje)
    with open("encriptado.txt","wb") as archivo_encriptado:
        archivo_encriptado.write(encriptado)

# FUNCION PARA CARGAR MENSAJE ENCRIPTADO.
def cargar_encriptado():
    return open("encriptado.txt","rb").read()


if __name__=="__main__":
    print("\nPrograma ENCRIPTADOR/DESENCRIPTADOR")

    otra_opcion = "y"

    while (otra_opcion == "y"):

        while True:

            try:
                selector = int(input("\nSeleccione una opcion:\n1- Encriptar.\n2- Desencriptar.\n"))
                if(selector == 1):
                    generar_clave()
                    generar_mensaje()                
                    clave = cargar_clave()
                    mensaje = cargar_mensaje()
                    fernet = Fernet(clave)
                    generar_encriptado()
                    encriptado = cargar_encriptado()
                    print("\nMensaje ENCRIPTADO: \n",encriptado)
                    break
            
                elif(selector == 2):
                    try:
                        encriptado = cargar_encriptado()    
                        clave = cargar_clave()
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
            otra_opcion = input()
            if (otra_opcion == "y" or otra_opcion == "n"):
                break
            else:
                print("\nOpcion incorrecta, intente nuevamente")

print("\nFin del programa")

