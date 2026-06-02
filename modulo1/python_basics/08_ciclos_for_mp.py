print("Ciclo For")
sacramientos = ["Bautizo", "Confirmacion", "Matrimonio"]
for sacramiento in sacramientos:
    print(sacramiento)
print("Recorrer palabras")
for letra in "sacramiento":
    print(letra)
print("Recorrer rango")
for i in range(1,6):
    print(i)
print("Recorrer rango configurar paso")
for i in range(1,10,2):
    print(i)    
print("Enumerar lista")
for i, sacramiento in enumerate(sacramientos):
    print(i, sacramiento)
print("Dos listas a la vez")
nombre=["Ana","Luis"]
edades=[20,25]
for nombre,edad in zip(nombre, edades):
    print(nombre, edad)
print("Control del ciclo")
print("break")
for i in range(10):
    if i==3:
        break
    print(i)
print("continue")
for i in range(5):
    if i==2:
        continue
    print(i)
print("for anidado")
for i in range(3):
    for j in range(2):
        print(i,j)
print("Lista comprehension forma corta")
cuadros = [x**2 for x in range(5)]
print(cuadros)
