# DICCIONARIOS
producto = {"Nombre" : "Ordenador",
             "Categoría" : "Electrónica",
             "Stock" : 10
            }

# Acceder a clave
print(producto["Categoría"])

# Añadir nueva clave
producto["Precio"] = 750
print(producto["Precio"])

# Modificar clave
producto["Stock"] = 9
print(producto["Stock"])

# Acceder con [] vs .get()
#print(producto["Marca"])
print(producto.get("Marca"))

# SETS
ciudades = ["Valencia", "Madrid", "Barcelona", "Madrid", "Madrid", "Zaragoza", "Valencia"]

# Convertir lista en set con valores únicos
ciudades_unicas = set(ciudades)
print(ciudades_unicas)