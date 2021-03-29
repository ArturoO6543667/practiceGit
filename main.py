import sys
#mi propio comentario

def saludar():
    print("hola a todos")


def main():
    saludar()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
