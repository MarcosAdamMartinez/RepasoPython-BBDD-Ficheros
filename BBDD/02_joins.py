# ¿Qué te parece si intentas hacer tú una consulta que relacione 3 tablas? Por ejemplo:
# "Dime el nombre de los Pokémon y el nombre de su Tipo (Fuego, Agua, etc) "
# "buscando en la tabla pokemon, pokemon_tipo y tipo"

import mysql.connector

try:

    connection = mysql.connector.connect(host="localhost",
                                         user="dam2",
                                         password="asdf.1234",
                                         database="pokemondb")

    if connection.is_connected():

        cursor = connection.cursor()

        query = """SELECT pokemon.nombre as pokemon, tipo.nombre as tipo FROM pokemon 
                   JOIN pokemon_tipo ON pokemon.numero_pokedex = pokemon_tipo.numero_pokedex
                   JOIN tipo ON pokemon_tipo.id_tipo = tipo.id_tipo"""

        cursor.execute(query)

        for row in cursor:
            print(row[0], "-", row[1])

except mysql.connector.Error as error:
    print(error)