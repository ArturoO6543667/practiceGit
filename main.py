
import sys


def saludar():
    print("hola a todos")


def main():
    saludar()
    print(sumaNumeros(5, 6))
    print(restaNumeros(6, 5))
    print(division(2, 0))


def division(a, b):
    if b != 0:
        return a, b
    else:
        return "no se puede dividir entre 0"


def sumaNumeros(a, b):
    return a+b


def restaNumeros(a, b):
    return a-b


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
