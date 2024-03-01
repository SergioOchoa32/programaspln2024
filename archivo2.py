c="C:\\Users\\Sergio\\Documents\\"
e="texto.txt"
s="archivo_finalizado.txt"

with open(c+s,"r") as archivo:
    texto=archivo.read()

print(archivo)

palabra=input("Ingresa la palabra a buscar: ")
palabra1=palabra.lower()

if palabra1 in texto:
    print("palabra encontrada")

else:
    print("palabra no encontrada")