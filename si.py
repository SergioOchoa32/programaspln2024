import os
carpeta_nombre="Documents"
archivos_lista=os.listdir(carpeta_nombre)
for archivo_nombre in archivos_lista:
    print(archivo_nombre)