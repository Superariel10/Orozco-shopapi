print("match-case")
comando = input("Comando proceso iniciar/parar/reiniciar")
match comando:
    case "iniciar":
        print("Sistema del sacramiento iniciando")
    case "parar":
        print("deteniendose el sistema del sacramiento")
    case "reiniciar":
        print("reiniciando el sistema del sacramiento")
    case _:
        print(f"comando '{comando}'no encontrado")

print("match condiciones")
numero=7
match numero:
    case n if n<0:
        print(f"{n} es negativo")
    case 0:
        print("Es cero")
    case n if n%2==0:
        print(f"{n} es par")
    case n:
        print(f"{n} es positivo e impar")