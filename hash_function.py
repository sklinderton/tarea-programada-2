def calcular_hash(fecha: str, cuarto: int, equipo_local: str) -> int:
    """
    Función hash que combina componentes clave para distribución uniforme
    - Fecha (YYYY-MM-DD) convertida a entero
    - Valor ASCII del equipo local
    - Cuarto del juego
    """
    fecha_num = sum(int(part) for part in fecha.split('-'))
    equipo_num = sum(ord(c) for c in equipo_local.upper())
    return (fecha_num * cuarto * equipo_num) % 750