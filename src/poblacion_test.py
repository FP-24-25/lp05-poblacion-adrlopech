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

if __name__ == "__main__":
    test_poblacion()