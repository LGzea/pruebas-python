from datetime import datetime

# Preguntar la fecha de nacimiento al usuario
fecha_nacimiento_str = input("Ingresa tu fecha de nacimiento (formato: YYYY-MM-DD): ")

# Convertir la cadena de fecha a un objeto datetime
fecha_nacimiento = datetime.strptime(fecha_nacimiento_str, "%Y-%m-%d")

# Obtener la fecha actual
fecha_actual = datetime.now()

# Calcular la diferencia en años y días
diferencia = fecha_actual - fecha_nacimiento
edad_en_anios = diferencia.days // 365
dias_adicionales = diferencia.days % 365

# Mostrar los resultados
print(f"Tienes {edad_en_anios} años y {dias_adicionales} días.")
