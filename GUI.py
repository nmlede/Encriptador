####################################################################################
################################### Librerias ######################################

import App
import tkinter as tk  
from herramientas import leer_config

####################################################################################
############################## Variables Globales ##################################

CONFIG=leer_config('data.json')
TEXTO_ETIQUETA=CONFIG['texto_etiqueta']
VERSION=CONFIG['version_aplicacion']

####################################################################################
################################## Main Window #####################################

ventana=tk.Tk()
ventana.title(f'Encriptador {VERSION}')
ventana.configure(bg='grey')

def cerrar_ventana():
    ventana.destroy()
    ventana.quit()
    
####################################################################################
################################### Etiquetas ######################################

etiqueta_titulo=tk.Label(ventana, text=TEXTO_ETIQUETA, font='Ubunto 12') # Creamos etiqueta
etiqueta_titulo.grid(row=0, column=0, columnspan=4, padx=2, pady=2)

####################################################################################
#################################### Botones #######################################

boton_mm=tk.Button(ventana, text='Mostrar Mensajes',font='Ubuntu 8' , width=14, height=1, command= lambda: App.mostrar_mensajes_guardados())
boton_mm.grid(row=1, column=0, padx=2, pady=1)

boton_mc=tk.Button(ventana, text='Mostrar Claves',font='Ubuntu 8', width=14, height=1, command= lambda: App.mostrar_claves_guardadas())
boton_mc.grid(row=1, column=1, padx=2, pady=1)

boton_me=tk.Button(ventana, text='Mostrar Encriptados', font='Ubuntu 8', width=14, height=1, command= lambda: App.mostrar_encriptados_guardados())
boton_me.grid(row=1, column=2, padx=2, pady=1)

boton_em=tk.Button(ventana, text='Encriptar Mensaje', font='Ubuntu 8', width=14, height=1, command= lambda: App.encriptar_mensaje())
boton_em.grid(row=2, column=0, padx=2, pady=1)

boton_me=tk.Button(ventana, text='Desencriptar Mensaje', font='Ubuntu 8', width=14, height=1, command= lambda: App.desencriptar())
boton_me.grid(row=2, column=1, padx=2, pady=1)

boton_bt=tk.Button(ventana, text='Borrar Informacion', font='Ubuntu 8', width=14, height=1, command= lambda: App.borrar_informacion())
boton_bt.grid(row=2, column=2, padx=2, pady=1)

boton_cv=tk.Button(ventana, text='Cerrar Aplicacion', font='Ubuntu 8', width=14, height=1, command= lambda: cerrar_ventana())
boton_cv.grid(row=3, column=1, padx=2, pady=1)


####################################################################################
###################################### Loop ########################################

ventana.mainloop()

