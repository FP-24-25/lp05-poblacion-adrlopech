from poblacion import *

def test_poblacion():
    poblaciones = lee_poblaciones('data/population.csv')
    print("Poblaciones:")
    for poblacion in poblaciones:
        print(poblacion)

    paises = calcula_paises(poblaciones)
    print("Paises:")
    for pais in paises:
        print(pais)

    pais_filtrado = 'Arb'
    poblaciones_filtradas = filtra_por_pais(poblaciones, pais_filtrado.upper())
    print(f"Poblaciones en {pais_filtrado}:")
    for poblacion in poblaciones_filtradas:
        print(poblacion)

    paises_filtrados = ['Spain', 'Mexico']
    anyo_filtrado = 1998
    poblaciones_filtradas_anyo = filtra_por_paises_y_anyo(poblaciones, anyo_filtrado, paises_filtrados)
    print(f"Poblaciones en {paises_filtrados} en el año {anyo_filtrado}:")
    for poblacion in poblaciones_filtradas_anyo:
        print(poblacion)

if __name__ == "__main__":
    test_poblacion()