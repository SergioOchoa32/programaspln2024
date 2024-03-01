c="C:\\Users\\Sergio\\Documents\\"
e="texto.txt"
s="archivo_finalizado.txt"

e2=open(c+e,"r")

s2=open(c+s,"w")

s2.write(e2.read())

e2.close()
s2.close()
s3=open(c+s,"r")
print(s3.read())
s3.close()



