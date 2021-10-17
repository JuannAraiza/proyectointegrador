def main():
    #escribe tu código abajo de esta línea
    nombre= input('Hola, ¿Cual es tu nombre?: ')
    print(f'Bienvenido {nombre} esperamos que te encuentres de lo mejor!')

    input('Presiona <enter> para continuar')

    print('¿Qué es lo que deseas investigar el día de hoy?')
    print('1. Información del Coronavirus     2. Test rápido      3. Casos en México        4. Recomendaciones      5. Salir')
    a = input('Porfavor dinos tu elección(introduce solamente el número): ')
    while a != 1 or 2 or 3 or 4 or 5:
        print('Porfavor introduce un número válido')
        a = input('')




if __name__=='__main__':
    main()
