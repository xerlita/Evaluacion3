import funciones

listaequipo = [
]

funciones.menu()
while True: 
    opcion = int(input("¿Que desea realizar?\n"))
    if opcion == 1:
        funciones.registrar_consumo(listaequipo) 
    elif opcion == 2: 
        funciones.listar_consumo(listaequipo)
    elif opcion == 3:
        funciones. imprimir_hoja(listaequipo)
    elif opcion == 4:
        funciones.consumo_porID()