def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "No se puede dividir por cero"
    else:
        return a / b

def main():
    print("Calculadora Simple")
    print("Operaciones disponibles:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. DivisiOn")

    opcion = input("Ingrese el numero de la operación que desea realizar: ")

    if opcion not in ['1', '2', '3', '4']:
        print("Opcion invalida")
        return

    num1 = float(input("Ingrese el primer numero: "))
    num2 = float(input("Ingrese el segundo numero: "))

    if opcion == '1':
        print("Resultado:", suma(num1, num2))
    elif opcion == '2':
        print("Resultado:", resta(num1, num2))
    elif opcion == '3':
        print("Resultado:", multiplicacion(num1, num2))
    elif opcion == '4':
        print("Resultado:", division(num1, num2))

if __name__ == "__main__":
    main()
