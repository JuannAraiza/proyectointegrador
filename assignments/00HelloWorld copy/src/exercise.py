
from matplotlib import pyplot as plt
import numpy as np
def datos():
    estados, positivos, muertes = leer()

    for estado, positivo, muerte  in zip(estados, positivos, muertes):
        print(estado + ', ' + positivo +' ' 'casos confirmados y ' + muerte + ' ' 'muertes')
    input('')
    

def leer():
    estados = []
    positivos = []
    muertes = []

    with open('assignments/00HelloWorld copy/src/data/covid.csv', 'r') as f:
        for line in f:
            lista_line = line.split(',')

            estados.append(lista_line[0])
            positivos.append(lista_line[1])
            muertes.append(lista_line[2])
    return estados, positivos, muertes 

def grafico_barras():
    print("CASOS DE COVID EN MÉXICO")

    plt.rcdefaults()

    estados = ["Ags", "B.C", "B.C.S", "Camp", "Coah", "Col", "Chis", "Chih", "Dgo", "Gto", "Gro", "Hgo", "Jalis", "Edo.MX", "Mich", "Mor", "Nay", "N.L", "Oax", "Pue", "Qro", "Q.Roo", "S.L.P", "Sin", "Son", "Tab", "Tamps", "Tlax", "Vcruz", "Yuc", "Zac"]
    barras = np.arange(len(estados))
    casospositivo = [34525, 63126, 55582, 23359, 90553, 32517, 22683, 66411, 47890, 180155, 75446, 61042, 157096, 368126, 71923, 49022, 33336, 200057, 79256, 122066, 94944, 58650, 101032, 72461, 109040, 138324, 99181, 28856, 120079, 71584, 40967]
    casosmuerte = [2888, 9455, 2325, 1978, 7311, 2131, 208, 8024, 2921, 12302, 5851, 7554, 16522, 32090, 7703, 4619, 2857, 12878, 5166, 15020, 5638, 3941, 6482, 8623, 8410, 5513, 6852, 2744,  13904, 5549, 3269]

    fig, ax = plt.subplots()

    ax.barh(barras, casospositivo, label='Casos Positivo')
    ax.barh(barras, casosmuerte, label='Casos Positivo')
    ax.set_yticks(barras)
    ax.set_yticklabels(estados)
    ax.invert_yaxis()  
    ax.set_xlabel('Casos positivo = Azul       Muertes = Naranja')
    ax.set_title('CDMX - Casos = 957,429   Muertes = 12,302')

    plt.savefig("grafico_barras.png")
    plt.show()

import math 
def main():
    #escribe tu código abajo de esta línea
    print('Este es un programa acerca del Coronavirus')
    print('------------------------------------------')
    nombre= input('Hola, ¿Cual es tu nombre?: ')
    print(f'Bienvenido {nombre} esperamos que te encuentres de lo mejor!')
    input('<ENTER>')

    print('¿Qué es lo que deseas investigar el día de hoy?')
    print('1. Información del Coronavirus    2. Test rápido     3. Casos en México     4. Recomendaciones para evitar    5. Salir del programa')
    a = 0
    while a == 0:
        x = int(input('<PRINCIPAL>Porfavor dinos el número de tu elección(introduce solamente el número): '))
        while x < 1 or x > 5:
            print('Porfavor introduce un número válido')
            x = int(input(''))
        if x == 1:
            print('Información escencial acerca del Coronavirus SARS-Cov-2')
            input('<ENTER>')
            print('Toda la información es brindada por el gobierno de México')
            input('<ENTER>')
            print('¿Qué es lo que deseas saber acerca del coronavirus?')
            print('(1)¿Qué es? (2)¿Cuáles son los sintomas? (3)¿Cuáles son las personas más vulnerables? (4)¿Qué hacer si tengo sintomas? (5)Salir')
            l = 0
            while l == 0:
                n = int(input('<INFORMACIÓN>Elige una de las opciones (coloca solamente el número): '))
                while n < 1 or n > 5:
                    print('Porfavor introduce un número válido')
                    n = int(input(''))
                if n == 1:
                    print('¿QUÉ ES EL COVID-19?')
                    input('')
                    print('El coronavirus o también llamado COVID-19 es un virus proveniente de China de un origen desconocido.')
                    input('')
                    print('Que aunque se tiene sospechas o ideas de donde surgió, todavía no se tiene el dato comprobado o ')    
                    print('confirmado por alguna institución, se dice que es un virus que surgió a partir del murcielago, ya que')
                    print('allá en Wuhan, que es de la ciudad donde surgió el virus, es muy común comer este tipo de alimento.')
                    input('')
                    print('A partir de ahi el virus a ser altamente contagioso se fue expandiendo por todo el mundo, provocando asi')
                    print('una pandemia a nivel mundial, la cual desafortunadamente a acabado con la vida de millones de personas, y')
                    print('que todavía en la actualidad sigue con un auge muy grande.') 
                    input('')
                elif n == 2:
                    print('PRINCIPALES SINTOMAS DEL COVID-19')
                    input('')
                    print('Una de las principales fortalezas de esta enfermedad y que ha hecho que muchas personas no le tomen importancia,')
                    print('es que los sintomas que esta provoca, facilmente pueden ser confundidos por otra enfermedad o cualquier otro mal estar, ')
                    print('ya que dentro de sus principales sintomas se encuentran:')
                    input('')
                    print('1.- Tos')
                    input('')
                    print('2.- Fiebre')
                    input('')
                    print('3.- Dolores de cabeza')
                    input('')
                    print('4.- Dolor en los ojos')
                    input('')
                    print('5.- Dolor en la garganta')
                    input('')
                    print('6.- Dificultad para respirar')
                    input('')
                    print('7.- Perdida de sentidos como el olfato y el gusto')
                    input('')
                    print('Además que se ha ido descubriendo que puede provocar otros sintomas adicionales poco comunes, como por ejemplo,')
                    print('dolores de estomago, vomitos y cuerpo cortado. ')
                    input('')
                    print('Esos son algunos de los sintomas más comunes que se han presentado en casos positivos de COVID-19')
                    input('')
                elif n == 3:
                    print('Personas más vulnerables al COVID-19')
                    input('')
                    print('Este nuevo virus lo que lo ha catalogado como altamente peligroso, es que no sabe a ciencia exacta como es que')
                    print('le va a afecar a las personas, ya que incluso hasta la persona más sana, que hace ejercicio constantemente,')
                    print('que come saludable, que esta al pendiente de su historial médico, hasta a esa persona le puede afectar de manera negativa.')
                    input('')
                    print('Pero ciertamente como cualquier enfermedad tiene a su grupo de personas que tienen un mayor riesgo de pasarlo mál con el virus,')
                    print('y este grupo de personas son:')
                    input('')
                    print('1.- Personas mayores o de la tercera edad')
                    input('')
                    print('2.- Mujeres embarazadas')
                    input('')
                    print('3.- Personas que padezcan de alguna enfermedad terminal')
                    input('')
                    print('Como ya antes se mencionó esta enfermedad es letal, aunque muchas personas tienden a compararla con una gripa,')
                    print('ciertamente no lo es y puede cobrar la vida de hasta el más sano.')
                    input('')
                elif n == 4:
                    print('Que hacer si padece de sintomas')
                    input('')
                    print('Las ventajas que se tienen hoy en día comparado con las que se tenía cuando inició la pandemia no tienen comparación,')
                    print('ya que hoy en día los medios que se ofrecen para ayudar a combatir el COVID-19 son muchas, por lo que el gobierno')
                    print('de México ha ofrecido varias líneas teléfonicas para acudir en caso de tener sintomas o de tener la enfermedad, ')
                    print('las cuales son: ')
                    input('')
                    print('800 0044 800')
                    input('o')
                    print('55 56 58 11 11')
                    input('')
                    print('Además que queda de más decir que hay que quedarse en casa, ya que siempre hay que proteger a los demás y evitar')
                    print('que esta enfermedad se siga propagando, cuidate mucho!')
                    input('')
                elif n == 5:
                    l =+1    
        elif x == 2:
            print('TEST RÁPIDO')
            input('<ENTER>')
            print('A continuación se presentará un test rápido de COVID-19!(contesta con si o no) ')
            input('<ENTER>')
            s = 0
            b = input('Tienes temperatura de > 37.5º?: ')
            c = input('Sientes tos?: ')
            d = input('Sientes dificultad para respirar?: ')
            e = input('Eres capaz de percibir sabores?: ')
            f = input('Sientes dolor muscular?: ')
            if b == ('si'):
                s =+ 1
            elif c == ('si'):
                s =+1
            elif d == ('si'):
                s =+ 1
            elif e == ('no'):
                s =+ 1
            elif f == ('si'):
                s =+ 1
            if s > 0:
                print('CUIDADO!, es probable que seas positivo al COVID-19')
                print('¡De todas maneras visita a un médico profesional para que se te haga la prueba necesaria')
                print('y no tomes como única evidencia o prueba este test rápido!')
                input('<ENTER>')
            else:
                print('¡Enhorabuena! no sientes ningún sintoma común del COVID-19') 
                input('<ENTER>')
        elif x == 3:
            grafico_barras()
            datos()
            pp = 2769289 // 32
            pm = 230728 // 32
            print(f'El promedio a nivel nacional de casos positivos en es de: {pp}')
            print(f'El promedio de muertes a nivel nacional es de: {pm}')

        elif x == 4:
            print('RECOMENDACIONES PARA EVITAR CONTAGIARSE')
            input('<ENTER>')
            print('A continuación se presentarán algunas recomendaciones que fueron brindadas por el gobierno de México para ')
            print('evitar lo más que se pueda ser infectado por este nuevo virus.')
            input('')
            print('Aunque como tal es una tarea muy dificil, debido a la manera en que se transmite el virus, el cual lo hace por el aire,')
            print('viajando por la saliva que emitimos y asi exparsiendose a una velocidad increible.')
            input('')
            print('Claramente es una tarea dificil tratar de seguir con la vida evitando ser contagiado, sin embargo,')
            print('hay medidas que podemos tomar para tratar de vivir nuestra vida lo más normal posible, aunque no lo será.')
            input('')
            print('El gobierno de México, a traves de su página web oficial ha recomendado ciertas medidas para evitar contagiarse,')
            print('las cuales son las siguientes:')
            input('')
            print('1.- Usar el cubrebocas todo el tiempo que salgas a la calle')
            input('')
            print('2.- Lavarse las manos por lo menos 20 segundos, asegurandose de limpiarlas de buan manera')
            input('')
            print('3.- Al salir a la calle, evitar a toda costa estarse tocando la nariz, los ojos y boca, sin antes haberse limpiado las manos')
            input('')
            print('4.- Si en alguna ocasión llegas a toser o estornudar, siempre cubrirse con el brazo')
            input('')
            print('5.- Evitar lo más que se pueda las multitudes, y promover la sana distancia ')
            input('')
            print('Estas son algunas de las recomendaciones que nos da el gobierno para evitar contagiarse, aunque claro esta')
            print('que será una tarea dificil debido a las necesidades que tenemos como ciudadanos')
            input('')
            print('Y no sobra decir que si puedes quedate en casa, protegete y protege a los que amas.')
        elif x == 5:
            a =+1
    print('Adiós! Nos vemos pronto!') 
    print('Y recuerda siempre, cuidate y cuida a los demás, que ellos también te cuidan!')
         

if __name__=='__main__':
    main()
