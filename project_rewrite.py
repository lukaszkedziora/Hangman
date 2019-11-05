def main():
    print('1-min, 2-max, 3-len, 4-multiply, 5-pow, 6-divmod')
    question = input('What do you want to do? ')
    if question == '1':
        min('x', 'y')
    elif question == '2':
        max('x', 'y')
    elif question == '3':
        len('interable')
    elif question == '4':
        multiply('x', 'y')
    elif question == '5':
        pow('x', 'y')
    elif question == '6':
        divmod('x', 'y')
    return


def again(x):
    x = input('One more time? y/n ')
    if x == 'y':
        main()
    else:
        exit


def min(x, y):
    x = input('min_number x: ')
    y = input('min_number y: ')
    if x < y:
        print('min is: ' + x)
    else:
        print('min is: ' + y)
    print(again(x))
    return


def max(x, y):
    x = input('max_number x: ')
    y = input('max_number y: ')
    if x > y:
        print('max is: ' + x)
    else:
        print('max is: ' + y)
    print(again(x))
    return


def len(iterable):
    iterable = input('input: ')
    count = 0
    for x in iterable:
        count += 1
    print('len: ', count)
    print(again(x))
    return


def multiply(x, y):
    x = input('first number: ')
    y = input('secound number: ')
    counter = 0
    for z in range(int(y)):
        counter += int(x)
    print('multiply: ', counter)
    print(again(x))
    return


def pow(x, y):
    x = input('first number: ')
    y = input('secound number: ')
    counter = int(x)
    for z in range(1, int(y)):
        counter *= int(x)
    print('pow: ', counter)
    print(again(x))
    return


def divmod(x, y):
    x = input('first number: ')
    y = input('secound number: ')
    counter = 0
    result = 0
    result1 = 0
    while counter <= int(x):
        counter += int(y)
        result += 1
    if counter > int(x):
        result1 = result - 1
    print('divmod //: ', result1)
    if int(x) <= int(y):
        if int(x) > 0 and int(y) > 0:
            result1 = int(x) - (result - 1) * int(y)
            print('divmod %: ', result1)
        elif int(x) < 0 and int(y) < 0:
            result1 = int(x) - (result - 1) * int(y)
            print('divmod %: ', result1)
        elif int(x) < 0 and int(y) > 0:
            result1 = int(x) - (result - 1) * int(y)
            print('divmod %: ', result1)
        elif int(x) > 0 and int(y) < 0:
            result1 = int(x) - (result - 1) * int(y)
            print('divmod %: ', result1)
    elif int(x) >= int(y):
        if int(x) > 0 and int(y) > 0:
            result1 = int(x) - (result - 1) * int(y)
            print('divmod %: ', result1)
        elif int(x) < 0 and int(y) < 0:
            result1 = int(x) - (result - 1) * int(y)
            print('divmod %: ', result1)
        elif int(x) < 0 and int(y) > 0:
            result1 = int(x) - (result - 1) * int(y)
            print('divmod %: ', result1)
        elif int(x) > 0 and int(y) < 0:
            result1 = int(x) - (result - 1) * int(y)
            print('divmod %: ', result1)
    print(again(x))
    return


if __name__ == "__main__":
    main()
