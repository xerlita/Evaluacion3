def menu(): 
    print("1. Registrar consumo")
    print("1. Listar todos los consumos")
    print("3. Imprimir hoja consumo")
    print("4. Buscar consumo por ID")
    print("5. SALIR")

def registrar_consumo(lista,):
    import random 
    codigo = random.randint(1000,9999)
    nombre = input("Ingrese jugador: ")
    edad = int(input("Ingrese su edad: "))
    equipo= input("Ingrese su equipo: ")
    viernes = int(input("Ingrese cuantas tazas de café tomo el día viernes: "))
    sabado = int(input("Ingrese cuabtas tazas de café tomo el dia sábado: "))
    domingo = int(input("Ingrese cuantas tazas de café tomo el día domingo: "))
    lista.append(codigo, nombre, edad, equipo, viernes, sabado, domingo)

def listar_consumo(lista):
    print("ID Consumo\t\tJugador\t\tEdad\t\tEquipo\t\tViernes\t\tSábado\t\tDomingo")
    for jugador in lista: 
        print(f"{jugador[0]}\t\t{jugador[1]}\t\t{jugador[2]}\t\t{jugador[3]}\t\t{jugador[4]}\t\t{jugador[5]}\t\t{jugador[6]}")


def imprimir_hoja(lista):
    

def consumo_porID():