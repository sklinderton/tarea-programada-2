import os
import struct
from punt_play import PuntPlay

REGISTRO_SIZE = 256
FORMATO_REGISTRO = '256s'
REGISTRO_VACIO = b'\x00' * REGISTRO_SIZE

def inicializar_tabla():
    #Crea/Carga el archivo info.dat con 750 registros vacíos
    if not os.path.exists("info.dat"):
        with open("info.dat", "wb") as f:
            f.write(REGISTRO_VACIO * 750)

def registro_ocupado(posicion: int) -> bool:
    #Verifica si una posición en la tabla está ocupada
    with open("info.dat", "rb") as f:
        f.seek(posicion * REGISTRO_SIZE)
        return f.read(REGISTRO_SIZE) != REGISTRO_VACIO

def escribir_registro(posicion: int, registro: PuntPlay):
    #Escribe un registro en la posición especificada
    registro_str = str(registro)
    registro_bytes = registro_str.ljust(REGISTRO_SIZE).encode()
    
    try:
        with open("info.dat", "r+b") as f:
            f.seek(posicion * REGISTRO_SIZE)
            actual = f.read(REGISTRO_SIZE)
            if actual == REGISTRO_VACIO:
                f.write(registro_bytes)
                return True
    except IOError:
        pass
    
    # Manejo de colisión
    colision_file = f"{posicion}-col.dat"
    with open(colision_file, "ab") as f:
        f.write(registro_bytes)
    return False

def buscar_registros(posicion: int) -> list:
    #Recupera todos los registros en una posición
    registros = []
    
    # Leer registro principal
    with open("info.dat", "rb") as f:
        f.seek(posicion * REGISTRO_SIZE)
        dato = f.read(REGISTRO_SIZE)
        if dato != REGISTRO_VACIO:
            registros.append(dato.decode().strip('\x00'))
    
    # Leer colisiones
    colision_file = f"{posicion}-col.dat"
    if os.path.exists(colision_file):
        with open(colision_file, "rb") as f:
            while True:
                dato = f.read(REGISTRO_SIZE)
                if not dato:
                    break
                registros.append(dato.decode().strip('\x00'))
    
    return registros