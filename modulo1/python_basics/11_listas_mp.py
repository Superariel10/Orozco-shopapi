print("Listas")
print("Crear Listas")
vacia=[]
print(vacia)
numeros=[1,2,3,4,5,6,7]
print(numeros)
nombres=["Juan","Pedro","Carlos","Maria, Pretra","Juana"]
print(nombres)
mixta=[1, "Hola","Bienvenido al sistema de sacramientos", True, None, 3.4]
print(mixta)
anidada=[1,[5,5,[6,4,4]],5,7]
print(anidada)
print("Acceso a los elementos de una lista")
print(nombres[0])
print(nombres[-1])
print(nombres[1:3])
print(nombres[::-1])

print("CRUD de una lista")
sacramientos=["Bautizo","Confirmacion","Orden sacerdotal","Matrimonio"]
#agregar
sacramientos.append("Confesion")
print(sacramientos)
sacramientos.insert(1,"Comunion")
print(sacramientos)
sacramientos.extend(["Entierro","Confesion"])
#modificar
sacramientos[0]="Bautismo"
print(sacramientos)
#eliminar elementos
sacramientos.remove("Entierro")
print(sacramientos)
eliminado=sacramientos.pop()
print(sacramientos)
eliminado=sacramientos.pop(0)
print(sacramientos)
del sacramientos [0]
print(sacramientos)

print("Buscar valores en los elementos de una lista")
print("Confesion" in sacramientos)
print(sacramientos.index("Confesion"))
print(sacramientos.count("Confesion"))

print("Ordernar una lista")
numeros_desordenados=[3,2,6,34,9,0,1,2]
print(numeros_desordenados)
numeros_desordenados.sort()
print(numeros_desordenados)
numeros_desordenados.sort(reverse=True)
print(numeros_desordenados)
ordenada = sorted(numeros_desordenados)
print(numeros_desordenados)
print(ordenada)

# lista-funcional.py

productos = [
    {"nombre": "Bautizo",    "precio": 9, "stock": 5,  "cat": "scr"},
    {"nombre": "Confirmacion",  "precio": 12,  "stock": 20, "cat": "scr"},
    {"nombre": "Orden sacerdotal",   "precio": 4, "stock": 3,  "cat": "scr"},
    {"nombre": "Matrimonio",  "precio": 6,  "stock": 8,  "cat": "scr"},
    {"nombre": "Confesion",   "precio": 7,  "stock": 0,  "cat": "scr"},
]

# map — transforma cada elemento
precios     = list(map(lambda p: p["precio"], productos))
nombres     = list(map(lambda p: p["nombre"].upper(), productos))
print(precios)   # [9, 12, 4, 6, 7]
print(nombres)   # ['BAUTIZO', 'CONFIRMACION', 'ORDEN SACERDOTAL', 'MATRIMONIO', 'CONFESSION']

# filter — filtra elementos
con_stock   = list(filter(lambda p: p["stock"] > 0, productos))
tech        = list(filter(lambda p: p["cat"] == "tech", productos))
print([p["nombre"] for p in con_stock])

# sorted con key
por_precio  = sorted(productos, key=lambda p: p["precio"])
mas_caro    = sorted(productos, key=lambda p: p["precio"], reverse=True)[0]
print(f"Más caro: {mas_caro['nombre']} ({mas_caro['precio']}€)")

# sum, min, max con key
total       = sum(p["precio"] * p["stock"] for p in productos)
mas_barato  = min(productos, key=lambda p: p["precio"])
print(f"Total inventario: {total}€")
print(f"Más barato: {mas_barato['nombre']}")

# any y all
hay_sin_stock = any(p["stock"] == 0 for p in productos)
todos_tech    = all(p["cat"] == "tech" for p in productos)
print(f"¿Hay sin stock? {hay_sin_stock}")    # True
print(f"¿Todos son tech? {todos_tech}")     # False