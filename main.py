# comentario de otro
# comentario de yo
import sys

# mi propio comentario

# este comentario es para eliminar una rama


def saludar():
    print("hola a todos")


def main():
    saludar()
    print(sumaNumeros(5, 6))
    print(restaNumeros(6, 5))


def sumaNumeros(a, b):
    return a+b


def restaNumeros(a, b):
    return a-b
# tarea 1 agregar metodo de multiplicacion y division
#lalalalal

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
