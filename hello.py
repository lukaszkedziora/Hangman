import sys


def main():
    lista = sys.argv[1:]
    lista2 = len(sys.argv)
    print(hello_world())
    if lista2 <= 1:
        print(hello('name'))
        print_hello('name')
    else:
        print('Hello,', *lista, '!')
    return


def hello_world():          # 1.1
    return 'Hello, World!'  # 1.2


def hello(name):
    name = input('Hello, what is your name? ')
    if name == '':     # 2.1
        return hello_world()
    elif name == 'none':
        return hello_world()
    else:                   # 2.2
        return 'Hello, ' + name + '!'  # 2.3


def print_hello(name):     # 3.1, 3.2 ?!
    print(hello('name'))


if __name__ == "__main__":
    main()
