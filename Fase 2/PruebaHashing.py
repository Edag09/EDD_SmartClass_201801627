import hashlib

mensaje = "Hola Mundo"
contrasenia = hashlib.sha256(mensaje.encode("utf-8"))
print(contrasenia.hexdigest())
