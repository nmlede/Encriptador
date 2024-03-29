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
TEXTO_TERMINAL=CONFIG['texto_terminal']
FONT_LABEL=CONFIG['font_label']
FONT_BUTTON=CONFIG['font_button']

####################################################################################
################################## Main Window #####################################

ventana=tk.Tk()
ventana.title(f'Encriptador {VERSION}')
ventana.configure(bg='grey')
# ventana.geometry('600x500')

def cerrar_ventana():
    # ventana.destroy()
    ventana.quit()
    
####################################################################################
################################### Etiquetas ######################################

etiqueta_titulo=tk.Label(ventana, text=TEXTO_ETIQUETA, font=FONT_LABEL) # Creamos etiqueta
etiqueta_titulo.grid(row=0, column=0, columnspan=4, padx=2, pady=2)

####################################################################################
#################################### Botones #######################################

boton_mm=tk.Button(ventana, text='Mostrar Mensajes',font=FONT_BUTTON , width=14, height=1, command= lambda: App.mostrar_mensajes_guardados())
boton_mm.grid(row=1, column=0, padx=2, pady=1)

boton_mc=tk.Button(ventana, text='Mostrar Claves',font=FONT_BUTTON, width=14, height=1, command= lambda: App.mostrar_claves_guardadas())
boton_mc.grid(row=1, column=1, padx=2, pady=1)

boton_me=tk.Button(ventana, text='Mostrar Encriptados', font=FONT_BUTTON, width=14, height=1, command= lambda: App.mostrar_encriptados_guardados())
boton_me.grid(row=1, column=2, padx=2, pady=1)

boton_em=tk.Button(ventana, text='Encriptar Mensaje', font=FONT_BUTTON, width=14, height=1, command= lambda: App.encriptar_mensaje())
boton_em.grid(row=2, column=0, padx=2, pady=1)

boton_me=tk.Button(ventana, text='Desencriptar Mensaje', font=FONT_BUTTON, width=14, height=1, command= lambda: App.desencriptar())
boton_me.grid(row=2, column=1, padx=2, pady=1)

boton_bt=tk.Button(ventana, text='Borrar Informacion', font=FONT_BUTTON, width=14, height=1, command= lambda: App.borrar_informacion())
boton_bt.grid(row=2, column=2, padx=2, pady=1)

boton_cv=tk.Button(ventana, text='Cerrar Aplicacion', font=FONT_BUTTON, width=14, height=1, command= lambda: cerrar_ventana())
boton_cv.grid(row=3, column=1, padx=2, pady=1)

####################################################################################
###################################### Terminal ####################################

etiqueta_terminal=tk.Label(ventana, text=TEXTO_TERMINAL, font=FONT_LABEL)
etiqueta_terminal.grid(row=4, column=0, columnspan=4, padx=2, pady=1)

terminal=tk.Frame(ventana, background='black', width=500, height=300)
terminal.grid(row=5, column=0, rowspan=10, columnspan=3, padx=5, pady=5)

terminal_id = terminal.winfo_id()

####################################################################################
###################################### Loop ########################################

ventana.mainloop()

