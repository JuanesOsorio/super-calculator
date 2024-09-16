run=True
while run == True:
    print("")
    print("")
    print("Bienvenido a la calculadora")
    print("que operación deseas hacer? selecciona el número de la que deseas")
    print("")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

    selection=int(input("..."))
    a = int(input("Dame el número 1...."))
    b = int(input("Dame el número 2...."))
    
    if selection == 1:
        resultado = a + b
        print(f"la respeusta es {resultado}")
        print("")
    elif selection == 2:
        resultado = a - b
        print(f"la resta entre {a} - {b} es: {resultado}")
        print("")
    
