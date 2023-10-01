def traductor():
    try:
        with open('EN-ES.txt', 'r') as archivo:
            return dict(line.strip().split('=') for line in archivo)
    except FileNotFoundError:
        return {}

def agregar_traduccion():
    palabra_ingles = input("Ingresa la palabra en inglés: ")
    palabra_espanol = input("Ingresa la traducción al español: ")

    diccionario = traductor()
    diccionario[palabra_ingles] = palabra_espanol

    with open('EN-ES.txt', 'w') as archivo:
        for palabra, traduccion in diccionario.items():
            archivo.write(f'{palabra}={traduccion}\n')

def traducir():
    modo, palabra = input("Ingrese el modo (EN-ES o ES-EN) y la palabra (por ejemplo, EN-ES perro): ").split()

    diccionario = traductor()

    if modo == 'EN-ES':
        traduccion = diccionario.get(palabra, 'No se encontró la traducción')
    elif modo == 'ES-EN':
        traduccion = next((key for key, value in diccionario.items() if value == palabra), 'No se encontró la traducción')
    else:
        traduccion = 'Modo no válido'

    print(f'{modo} {palabra} --> {traduccion}')

while True:
    print("\n1. Agregar nueva traducción")
    print("2. Traducir")
    print("3. Salir")
    
    opcion = input("Seleccione una opción (1/2/3): ")
    
    if opcion == '1':
        agregar_traduccion()
    elif opcion == '2':
        traducir()
    elif opcion == '3':
        break
    else:
        print("Opción no válida. Por favor, seleccione 1, 2 o 3.")
    