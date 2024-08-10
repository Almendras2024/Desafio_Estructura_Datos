# Lista inicial de recordatorios
recordatorios = [
    {"fecha": "2021-07-15", "hora": "09:00", "descripcion": "No hacer nada es Feriado"},
    {"fecha": "2021-05-01", "hora": "09:00", "descripcion": "Día del Trabajo"},
    # Agregar recordarorio Ramada
    {"fecha": "2021-09-18", "hora": "16:00", "descripcion": "Ramadas"},
]

# Agregar el evento del 1 de Enero de 2021 a las 11 de la mañana para “Levantarse y ejercitar"
recordatorios.append({"fecha": "2021-01-01", "hora": "11:00", "descripcion": "Levantarse y ejercitar"})
# Agregar el 2 de Febrero de 2021 a las 6 de la mañana para “Empezar el Año”
recordatorios.append({"fecha": "2021-02-02", "hora": "06:00", "descripcion": "Empezar el Año"})

# Editar el vento del 15 de Julio para que sea el 16 de Julio
for recordatorio in recordatorios:
    if recordatorio["fecha"] == "2021-07-15":
        recordatorio["fecha"] = "2021-07-16"

# Eliminar el evento del Día del Trabajo
recordatorios = [recordatorio for recordatorio in recordatorios if recordatorio["descripcion"] != "Día del Trabajo"]

# Agregar cena de Navidad y de Año Nuevo a las 22 hrs
recordatorios.append({"fecha": "2021-12-24", "hora": "22:00", "descripcion": "Cena de Navidad"})
recordatorios.append({"fecha": "2021-12-31", "hora": "22:00", "descripcion": "Cena de Año Nuevo"})

# Ordenar los recordatorios por fecha y hora
recordatorios.sort(key=lambda x: (x["fecha"], x["hora"]))

# Mostrar los recordatorios actualizados
for recordatorio in recordatorios:
    print(recordatorio)