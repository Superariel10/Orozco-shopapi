print("condicionales simples")
edad=input("Incluye edad?")
if (int(edad)>=18):
    print("Mayor de edad")

print("condicionales dos caminos")
temperatura=input("Incluye temperatura?")
if (int(temperatura)>=38):
    print("temperatura alta, no apto para el sacramiento")
else:
    print("temperatura normal, apto para el sacramiento")
    
print("condicionales multiples")
sacramiento=input("Incluir edad?")
if (int(sacramiento)>=4):
    print("Bautizo")
elif (int(sacramiento)>=12):
    print("Confirmacion")
elif (int(sacramiento)>=18):
    print("Confesion")
else:
    print("Matrimonio")
    
print("condicionales if anidados")
tiene_reserva=True
dinero=25
inscripcion="iglesia"
if (tiene_reserva):
    if(dinero>=20):
        if inscripcion=="iglesia":
            print("Tu inscripcion cuesta $20. Pago confirmado")
        else: 
            print("Inscripcion disponible")
    else:
        print("Dinero insuficiente")
else:
    print("No tiene reserva")
    
print("condicionales if anidados bono")
es_empleado=True
antiguedad=365
desempeño=9
salario=2000
if (es_empleado):
    if(antiguedad>=365):
        if desempeño >= 8:
            print("Puede optar al bono")
            if salario >= 1000:
                print("bono de $100 del servicio")
            else:
                print("bono de $200 del servicio")
        else: 
            print("No puede optar al bono")
    else:
        print("No cumple la antiguedad requerida")
else:
    print("No es un empleado")