import json

# Leer config -------------------------------------
def leer_config(json_file_path):
    diccionario_data=[]
    with open(json_file_path) as data_file:
        diccionario_data=json.load(data_file)

    return diccionario_data

