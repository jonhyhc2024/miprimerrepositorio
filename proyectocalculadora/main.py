from calculadora import Calculadora

def mostrar_menu():
    print("Seleccione una operación:")
    print("1. Sumar dos números")
    print("2. Restar")
    print("3. Dividir")
    print("4. Multiplicar")
    print("5. Sumar más de dos números")
    print("6. Salir")

def obtener_numeros():
    a = float(input("Ingrese el primer número: "))
    b = float(input("Ingrese el segundo número: "))
    return a, b

def obtener_lista_numeros():
    numeros = input("Ingrese los números separados por espacio: ")
    return list(map(float, numeros.split()))

def main():
    calc = Calculadora()
    
    while True:
        mostrar_menu()
        opcion = input("Elija una opción (1/2/3/4/5/6): ")

        if opcion == '1':
            a, b = obtener_numeros()
            resultado = calc.sumar(a, b)
            print(f"Resultado: {a} + {b} = {resultado}")

        elif opcion == '2':
            a, b = obtener_numeros()
            resultado = calc.restar(a, b)
            print(f"Resultado: {a} - {b} = {resultado}")

        elif opcion == '3':
            a, b = obtener_numeros()
            resultado = calc.dividir(a, b)
            print(f"Resultado: {a} / {b} = {resultado}")

        elif opcion == '4':
            a, b = obtener_numeros()
            resultado = calc.multiplicar(a, b)
            print(f"Resultado: {a} * {b} = {resultado}")

        elif opcion == '5':
            numeros = obtener_lista_numeros()
            resultado = calc.sumar_multiples(numeros)
            print(f"Resultado: {' + '.join(map(str, numeros))} = {resultado}")

        elif opcion == '6':
            print("Saliendo...")
            break

        else:
            print("Opción no válida, por favor intente de nuevo.")


main()

    