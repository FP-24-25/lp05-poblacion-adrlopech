import csv
import collections

RegistroPoblacion = collections.namedtuple('RegistroPoblacion', 'pais, codigo, año, censo')

def lee_poblaciones(ruta_fichero):
    lectura = []
    
    with open(ruta_fichero, encoding="utf-8") as f:
        lector = csv.reader(f, delimiter=",")
        for pais, codigo, año, censo in lector:
            pais = str(pais)
            codigo = str(codigo)
            año = int(año)
            censo = int(censo)
            tupla_lectura= RegistroPoblacion(pais, codigo, año, censo)
            lectura.append(tupla_lectura)
        return(lectura)
    
def calcula_paises(poblaciones):
    paises = {registro.pais for registro in poblaciones}
    return sorted(paises)

def filtra_por_pais(poblaciones, nombre_o_codigo):
    filtrados = []
    for registro in poblaciones:
        if registro.pais == nombre_o_codigo or registro.codigo == nombre_o_codigo:
            filtrados.append((registro.año, registro.censo))
    return filtrados

def filtra_por_paises_y_anyo(poblaciones, anyo, paises):
    resultado = []
    for registro in poblaciones:
        if registro.año == anyo and registro.pais in paises:
            resultado.append((registro.pais, registro.censo))
    return resultado

