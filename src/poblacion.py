import csv
import collections

RegistroPoblacion = collections.namedtuple('RegistroPoblacion', 'pais, codigo, año, censo')

def lee_poblaciones(ruta_fichero):
    lectura = []
    
    with open(ruta_fichero, encoding="utf-8") as f:
        lector = csv.reader(f, delimiter=",")
        for pais, codigo, año, censo in lector:
            pais = str(pais)
            codigo = (codigo)
            año = int(año)
            censo = int(censo)
            tupla_lectura= RegistroPoblacion(pais, codigo, año, censo)
            lectura.append(tupla_lectura)
        return(lectura)
    
def calcula_paises(poblaciones):
    paises = {registro.pais for registro in poblaciones}
    return sorted(paises)

