import sys

# mi propio comentario

# este comentario es para eliminar una rama



def saludar():
    print("hola a todos")


def main():
    saludar()
    print(sumaNumeros(5, 6))


def sumaNumeros(a, b):
    return a+b


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
