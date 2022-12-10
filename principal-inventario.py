'''
from datetime import date,time,datetime
localTime = date.today()
print(localTime)
def fecha(a,m,d):
    print("AA/MM/DD")
    movieDate = date(a,m,d)
    operation =  localTime - movieDate
    return operation
print(fecha(2021,8,22))
'''
class persona:
    nombre: input("Ingrese nombre:\n")
    apellido: input("Ingrese apellido\n")
    documento: int(input("Ingrese cedula:\n"))
    correo: input("Ingrese nombre:\n")
    clienteId: int(input("Ingrese el id unico\n"))

class pelicula:
    nombre: input("Ingrese nombre de pelicula:\n")
    genero: input("Genero al que pertence la pelicula:\n")
    ano: int(input("Año de publicación:\n"))
    duracion: input("Duración de la pelicula\n")
    
    
    
    
    