juego = [['☢','☢','☢','☢','☢'],['☢','☢','☢','☢','☢'],['☢','☢','☢','☢','☢'],['☢','☢','☢','☢','☢'],['☢','☢','☢','☢','☢']]

correcto = '⚑'
incorrecto = '⚐'
list_pregunta = ['¿Que es python ?\n\n1. juego \n2. lenguaje de programacion  \n3. marca de agua \n4. ninguna de las anteriores ',
'¿Que es HTML?\n\n1. lenguaje de maquetacion \n2. marca de gaseosa \n3. navegador \n4. perro caliente ',
' ¿Cuántos litros de sangre tiene una persona adulta?\n\n1. Tiene entre 2 y 4 litros \n2.Tiene entre 4 y 6 litros \n3.Tiene 10 litros \n4.Tiene 7 litros',
'¿Quién es el autor de la frase "Pienso, luego existo"?\n\n1. Platón \n2.Descartes \n3. Sócrates \n4. Nietzche',
'¿Cuál es el país más grande y el más pequeño del mundo?\n\n1. Rusia y Vaticano \n2. China y Nauru \n3. Canadá y Mónaco \n4. Estados Unidos y Malta ',
'¿Cuál es el grupo de palabras escritas correctamente?\n\n1. Metamorfosis, extranjero, diversidac, equilivrio \n2. Metaformosis, estranjero, diversidad, ekilibrio \n3. Metamorfosis, extrangero, dibersidad, equilibrio \n4. Metamorfosis, extranjero, diversidad, equilibrio',
'¿Cuál es el libro más vendido en el mundo después de la Biblia?\n\n1. El Señor de los Anillos \n2. Don Quijote de la Mancha \n3. El Principito \n4. Cien años de Soledad',
'¿Cuántos decimales tiene el número pi π?\n\n1. Dos \n2. Cien \n3. Infinitos \n4. Mil',
'¿Cuántos jugadores por equipo participan en un partido de voleibol?\n\n1. 3 jugadores \n2. 4 jugadores \n3. 5 jugadores \n4. 6 jugadores',
'¿Quién pintó la obra "Guernica"?\n\n1. Paul Cézanne \n2. Pablo Picasso \n3. Diego Rivera \n4. Salvador Dalí','¿Cuánto tiempo tarda la luz del Sol en llegar a la Tierra?\n\n1. 12 minutos \n2. 1 día \n3. 12 horas \n4. 8 minutos',
'¿Cuál es la nacionalidad de Jorge Mario Bergoglio?\n\n1. Italiana \n2.Española \n3. Mexicana \n4. Argentina',
'¿En qué periodo de la prehistoria fue descubierto el fuego?\n\n1. Neolítico  \n2. Paleolítico \n3. Edad de hielo \n4. Edad de los metales',
'¿A quién se le atribuye la frase "Solo sé que no sé nada"?\n\n1. Nietszche \n2. Sófocles \n3. Salomón \n4. Sócrates',
'¿Cuál es la montaña más alta del continente americano?\n\n1. Monte Everest \n2. Aconcagua \n3. Pico Neblina \n4. Pico Bolívar',
'¿Cuál es la categoría de los premios Nobel que ha recibido más galardones?\n\n1. Física \n2.Química \n3. Medicina \n4. Literatura',
'¿Cuáles son los nombres de los tres reyes magos?\n\n1. Gaspar, Nicolas y Nataniel \n2. Gaspar, Melchor y Baltazar \n3. Simon, Judas y Mateo \n4. Charles, George y Louis',
'¿Cuál es la capital de Mongolia?\n\n1. Muharin Den \n2. Ulán Bator \n3. Pionyang \n4. Daca',
'Carlos Cruz-Diez fue: \n\n1. Artista cinético \n2. Compositor musical \n3. Artista cubista \n4. Escritor de ensayos', 'El número romano MDCLXVI corresponde a:\n\n1. 1991 \n2. 1000100 \n. 1551 \n4. 1666',
'La balalaica, la tambura y el buzuki son:\n\n1. Postres griegos \n2. Platillos turcos \n3. Instrumentos de viento \n4. Instrumentos de cuerda','Edson Arantes do Nascimento es mejor conocido como:\n\n1. Albert Einstein \n2. Pelé \n3. Nicolas Copérnico \n4. Linus Pauling',
'¿Quién era primer ministro de Gran Bretaña cuando la reina Isabel II ascendió al trono?\n\1. Margaret Thatcher \n2. Winston Churchill \n3. Neville Chamberlain \n4. William Shakesperare','¿Qué juego fue creado por el profesor de educación física James Naismith?\n\n1. Ping-pong \n2. Fútbol \n3. Voleibol \n4. Basquetbol','La sigla OTAN significa:\n\n1. Orden Territorial para Almacenes y Negocios \n2. Organización de Técnicos de Aeronáutica \n3. Organización del Tratado del Atlántico Norte \n4. Organización Tripartita de América del Norte'


]
list_respuesta = ['2','1','2','2','1','4','2','3','4','2','4','4','2','4','1','1','2','2','1','4','4','2','2','4','3']

import os
  
contador_preguntas = -1   
def fnt_limpiar():
    global contador_preguntas
    os.system('cls')
    print('AUTOR ->  JUAN JOSE HERNANDEZ DUARTE ')
    contador_preguntas += 1
    print(f'siguiente cuadro es de la respuesta de la pregunta  numero: {contador_preguntas}') 
    fnt_impresion()
    
def fnt_impresion():
    
    global contador
    print('\n')
    for i in range(len(juego)):
        for j in range(len(juego[i])):
            print(juego[i][j], end = '   ')
            
        
        print('\n')

contador= 0
    
    
   
for i in range(len(juego)):
        for j in range(len(juego[i])):
            os.system('cls')
            fnt_limpiar()
            print()
            print(list_pregunta[contador])
            print()
            r = input('-> ')
            if r == list_respuesta[contador]:
                juego[i][j] = correcto
            else:
                juego[i][j] = incorrecto
            contador += 1
# profe no fui capaz de que se impriman las preguntas y las respuestas en el mismo cuadro
# por eso lo deje asi
#podria darme una idea para realzarlo? 
