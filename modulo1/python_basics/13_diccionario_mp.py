# diccionarios.py

# Crear diccionarios
vacio    = {}
persona  = {"nombre": "Alberto", "edad": 28, "ciudad": "Villarreal"}
config   = dict(host="localhost", puerto=5432, debug=True)

# Acceso
print(persona["nombre"])              # Alberto
print(persona.get("email"))           # None — no lanza error si no existe
print(persona.get("email", "N/A"))    # N/A — valor por defecto

# Modificar
persona["email"]   = "alberto@email.com"  # añadir/modificar
persona["edad"]    = 29                   # modificar
del persona["ciudad"]                     # eliminar
valor = persona.pop("email")             # eliminar y obtener el valor
print(persona)

# Verificar existencia
print("nombre" in persona)            # True
print("ciudad" in persona)            # False

# Métodos esenciales
print(persona.keys())    # dict_keys(['nombre', 'edad'])
print(persona.values())  # dict_values(['Alberto', 29])
print(persona.items())   # dict_items([('nombre', 'Alberto'), ('edad', 29)])

# Iterar
for clave, valor in persona.items():
    print(f"  {clave}: {valor}")

# update — fusionar diccionarios
persona.update({"ciudad": "Barcelona", "tel": "600111222"})
print(persona)

# Fusionar con | (Python 3.9+)
extra  = {"cargo": "Desarrolladora", "activo": True}
completo = persona | extra
print(completo)

# Diccionarios anidados
empresa = {
    "nombre": "TechCorp",
    "empleados": {
        1: {"nombre": "Juan", "depto": "tech"},
        2: {"nombre": "Maria", "depto": "ventas"},
    },
    "sedes": ["Madrid", "Barcelona"]
}

print(empresa["empleados"][1]["nombre"])   # Juan
empresa["empleados"][3] = {"nombre": "Marta", "depto": "rrhh"}

# setdefault — añadir solo si no existe
persona.setdefault("pais", "España")       # añade "pais"
persona.setdefault("nombre", "Otro")      # no modifica — ya existe