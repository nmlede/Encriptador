# Encriptador
A little piece of shit written in Python, yes, but it's my first little piece of shit written in Python! :D

Lo que hay aca es un intento de script que cifra y descifra un mensaje contenido en un archivo utilizando una clave privada generada por el propio script
utilizando el modulo cryptography.fernet de Python.

El programa es simple. La opcion 1 genera la clave privada con la cual cifra el mensaje que nosotros ingresamos en formato String.
Se genera un archivo "clave.key", otro "mensaje.txt" y "encripotado.txt" que contienen los elementos necesarios para mantener seguro el mensaje
y descifrarlo posteriormente mediante la opcion 2.

Esta de mas decir que sin la clave privada y el mensaje cifrado es imposible descrifrar el mensaje original, haciendo aun mas seguro el sistema de cifrado.

Como dije, un pedacito de mierda, pero mi primer pedacito de mierda en Python :D
