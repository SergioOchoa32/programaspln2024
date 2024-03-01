dias_laborales=["Lunes","Martes","Miercoles","Jueves","Viernes"]
print("La semana laboral: ", dias_laborales)
print("Dia 1: ", dias_laborales[0])
dias_laborales[4]="Sabado"
print("semana laboral", dias_laborales)
long= len(dias_laborales)
print("la longitud es: ", long)
pos= dias_laborales.index("Miercoles")
print("La posicion de miercoles es: ",pos)
dias_laborales.append("Sabado")
print("Semana laboral: ", dias_laborales)
del dias_laborales[4]
print("Semana laboral: ", dias_laborales)
