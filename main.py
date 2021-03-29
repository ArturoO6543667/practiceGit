import sys
# este comentario es para eliminar una rama


def saludar():
    print("hola a todos")


def main():
    saludar()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
