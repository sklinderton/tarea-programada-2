import os
from hash_function import calcular_hash
from file_manager import inicializar_tabla, escribir_registro, buscar_registros, registro_ocupado
from punt_play import PuntPlay

def cargar_datos():
    #Carga datos desde archivos CSV de la temporada
    data_path = os.path.join("data", "segundaprogramada")
    
    for filename in os.listdir(data_path):
        if filename.endswith(".csv"):
            with open(os.path.join(data_path, filename), 'r') as f:
                next(f)  # Saltar cabecera
                for linea in f:
                    datos = linea.strip().split(',')
                    try:
                        # Extraer datos del CSV (ajustar índices según estructura real)
                        game_id = datos[0]
                        teams = datos[1]
                        yards = float(datos[2])
                        quarter = int(datos[3])
                        date = datos[4]
                        time = datos[5]
                        
                        # Crear objeto y calcular hash
                        play = PuntPlay(game_id, teams, yards, quarter, date, time)
                        equipo_local = teams.split('@')[1].strip()
                        pos = calcular_hash(date, quarter, equipo_local)
                        
                        # Escribir registro
                        escribir_registro(pos, play)
                        
                    except (IndexError, ValueError) as e:
                        print(f"Error procesando línea: {linea} - {str(e)}")

def mostrar_menu():
    #Interfaz de usuario principal
    print("\n=== SISTEMA DE REGISTROS NFL ===")
    print("1. Cargar datos de temporada")
    print("2. Buscar por posición")
    print("3. Salir")
    return input("Seleccione una opción: ")

def main():
    #Función principal de ejecución"""
    inicializar_tabla()
    
    while True:
        opcion = mostrar_menu()
        
        if opcion == '1':
            cargar_datos()
            print("\nDatos cargados exitosamente!")
            
        elif opcion == '2':
            try:
                pos = int(input("Ingrese posición a buscar (0-749): "))
                if 0 <= pos <= 749:
                    resultados = buscar_registros(pos)
                    if resultados:
                        print(f"\nRegistros encontrados en posición {pos}:")
                        for idx, reg in enumerate(resultados, 1):
                            print(f"{idx}. {reg}")
                    else:
                        print("\nNo se encontraron registros en esta posición")
                else:
                    print("\nError: La posición debe estar entre 0 y 749")
            except ValueError:
                print("\nError: Debe ingresar un número válido")
                
        elif opcion == '3':
            print("\nSaliendo del sistema...")
            break
            
        else:
            print("\nOpción no válida. Intente nuevamente")

if __name__ == "__main__":
    main()