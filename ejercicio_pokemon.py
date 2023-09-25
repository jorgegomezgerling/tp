# Se cuenta con una lista de entrenadores Pokémon. De cada uno de estos se conoce: nombre, cantidad de torneos ganados, 
# cantidad de batallas perdidas y cantidad de batallas ganadas.
# Y además la lista de sus Pokémons, de los cuales se sabe: nombre, nivel, tipo y subtipo.
# Se pide resolver
# las siguientes actividades utilizando lista de lista implementando las funciones necesarias:
# a. obtener la cantidad de Pokémons de un determinado entrenador; chek;
# b. listar los entrenadores que hayan ganado más de tres torneos;
# c. el Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados;

# d. mostrar todos los datos de un entrenador y sus Pokémos;
# e. mostrar los entrenadores cuyo porcentaje de batallas ganados sea mayor al 79 %;
# f. los entrenadores que tengan Pokémons de tipo fuego y planta o agua/volador
# (tipo y subtipo);
# g. el promedio de nivel de los Pokémons de un determinado entrenador;
# h. determinar cuántos entrenadores tienen a un determinado Pokémon;
# i. mostrar los entrenadores que tienen Pokémons repetidos;
# j. determinar los entrenadores que tengan uno de los siguientes Pokémons: Tyrantrum, Terrakion o Wingull;
# k. determinar si un entrenador “X” tiene al Pokémon “Y”, tanto el nombre del entrenador
# como del Pokémon deben ser ingresados; además si el entrenador tiene al Pokémon se
# deberán mostrar los datos de ambos;

from lista_lista import Lista
from random import randint

class Trainer():

    def __init__(self, nombre, ctg=0, cbp=0, cbg=0):
        self.nombre = nombre
        self.cbg = cbg
        self.ctg = ctg
        self.cbp = cbp
    
    def __str__(self):
        return f'{self.nombre} --> C. Batallas Ganadas: {self.cbg}- C. Torneos Ganados: {self.ctg} C. Batallas Perdidas: {self.cbp}'

class Pokemon():
    def __init__(self, nombre, nivel, tipo, subtipo=None):
        self.nombre = nombre
        self.nivel = nivel
        self.tipo = tipo
        self.subtipo = subtipo
    
    def __str__(self):
        return f'{self.nombre} es tipo: {self.tipo} - {self.subtipo} y nivel: {self.nivel}'
    

trainer1 = Trainer("Ash", randint(1,10), randint(1,10), randint(1,10))
trainer2 = Trainer("Misty", randint(1,10), randint(1,10), randint(1,10))
trainer3 = Trainer("Brook", randint(1,10), randint(1,10), randint(1,10))
trainer4 = Trainer("Max", randint(1,10), randint(1,10), randint(1,10))
trainer5 = Trainer("May", randint(1,10), randint(1,10), randint(1,10))
trainer6 = Trainer("Giovanni", randint(1,10), randint(1,10), randint(1,10))

entrenadores = [trainer1, trainer2, trainer3, trainer4, trainer5, trainer6]

lista_entrenadores = Lista()
lista_pokemones = Lista()

for trainer in entrenadores: 
    lista_entrenadores.insert(trainer, 'nombre')

pikachu = Pokemon("Pikachu", 10, 'electrico')
milotic = Pokemon("Milotic", 15, 'agua')
charizard = Pokemon("Charizard", 30, "fuego", "volador")
szither = Pokemon("Szither", 25, "agua")
blaziken = Pokemon("Blaziken", 32, "fuego", "lucha")
umbreon = Pokemon("Umbreon", 28, "siniestro")
vaporeon = Pokemon("Vaporeon", 31, "agua")
eevee = Pokemon("Eevee", 18, "normal")
hitmonlee = Pokemon("Hitmonlee", 29, "lucha")
bulbasaur = Pokemon("Bulbasaur", 20, "planta", "veneno")
squirtle = Pokemon("Squirtle", 21, "agua")
jigglypuff = Pokemon("Jigglypuff", 19, "normal", "hada")
gengar= Pokemon("Gengar", 36, "fantasma", "veneno")
machamp = Pokemon("Machamp", 34, "lucha")
gyarados = Pokemon("Gyarados", 35, "agua", "volador")

pokemones = [pikachu, milotic, charizard, szither, blaziken, umbreon, vaporeon, eevee, hitmonlee, bulbasaur, squirtle, jigglypuff, gengar, machamp, gyarados]

for pokemon in pokemones:
    numero_entrenador = randint(0, lista_entrenadores.size()-1)
    entrenador = lista_entrenadores.get_element_by_index(numero_entrenador)
    entrenador[1].insert(pokemon, 'nombre')

def cantidad_pokemones():
    pos = lista_entrenadores.search('Ash', 'nombre')
    if pos is not None:
        valor = lista_entrenadores.get_element_by_index(pos)
        entrenador, sublista = valor[0], valor[1]
        print(f'{entrenador.nombre} tiene {sublista.size()} pokemons')

def torneos_ganados():
    for i in range(0, lista_entrenadores.size()):
        valor = lista_entrenadores.get_element_by_index(i)[0]
        if valor.ctg > 3:
            print(valor.nombre, 'con: ', valor.ctg)

def mayor_torneos():
    mayor_cantidad = lista_entrenadores.get_element_by_index(0)[0].ctg
    pos_mayor = 0

    for pos in range(1, lista_entrenadores.size()):
        entrenador = lista_entrenadores.get_element_by_index(pos)[0]
        if entrenador.ctg > mayor_cantidad:
            pos_mayor = pos
            mayor_cantidad = entrenador.ctg
    
    valor = lista_entrenadores.get_element_by_index(pos_mayor)
    entrenador, sublista = valor[0], valor[1]

    if sublista.size() > 0:
        pokemon_mayor = sublista.get_element_by_index(0)
        for pos in range(1, sublista.size()):
            pokemon = sublista.get_element_by_index(pos)
            if pokemon.nivel > pokemon_mayor.nivel:
                pokemon_mayor = pokemon

    print(f'El pokemon de mayor nivel del entrenador {entrenador.nombre} es {pokemon_mayor.nombre} {pokemon_mayor.nivel} ')
            



torneos_ganados()
mayor_torneos()
print(entrenadores[0])

