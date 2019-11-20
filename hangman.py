import random
import os


arr_miasta = ['TALLIN', 'PARIS', 'BERLIN', 'DUBLIN', 'LONDON', 'MOSCOW', 'WARSAW', 'LISBON', 'OSLO', 'ROME']
arr_temp = []
arr_dashes = []
arr_all_letters = []
wrong_words = []
arr_lives = []


def main():
    random_city()
    input_letter()
    return


def print_all():
    clear = lambda: os.system('clear')
    clear()
    print('You have', 4-len(arr_lives), 'lives left')
    print('Letters you have choosen: ', *arr_all_letters)
    hangperson()
    print(*arr_dashes)


def input_letter():
    print_all()
    let = input('Give me a letter or word: ')
    repetition(let)


def repetition(let):
    c = arr_all_letters.count(let)
    d = wrong_words.count(let)
    if c == 0 and len(let) == 1:
        arr_all_letters.append(let)
        compare(let)
    elif d == 0 and len(let) > 1:
        wrong_words.append(let)
        compare(let)
    else:
        print('już było')
        input_letter()
    return


def compare(let):
    a = let.upper()
    a1 = let.isalpha()
    wrong_answers = []
    i = 0
    if a1 is True:
        if len(a) > 1:
            x = ''.join(arr_temp)
            if a == x:
                again()
            else:
                for i in range(len(arr_temp)):
                    wrong_answers.append(1)
                    wrong(wrong_answers)
        if len(a) == 1:
            for i in range(len(arr_dashes)):
                if arr_temp[i] == a:
                    arr_dashes[i] = arr_temp[i]
                    if arr_dashes == arr_temp:
                        again()
                else:
                    wrong_answers.append('1')
                    wrong(wrong_answers)
            input_letter()
    else:
        print('Error, wrong sight')
        input_letter()


def again():
    print_all()
    if len(arr_lives) < 4:
        print('You are the WINNER!')
    else:
        print(*arr_temp, '\nThis is the END!')
    a = input('One more time? y/n: ')
    b = a.upper()
    if b == 'Y':
        main()
    else:
        print('Bye, Bye!')
        exit()


def wrong(wrong_answers):
    if len(wrong_answers) == len(arr_temp):
        arr_lives.append('1')
        if len(arr_lives) == 4:
            print('this is end')
            again()
        input_letter()


def random_city():
    word = random.sample(arr_miasta, 1)     # random
    st_c = ''.join(word)
    arr_temp.clear()
    arr_dashes.clear()
    arr_lives.clear()
    arr_all_letters.clear()
    for char in st_c:
        arr_temp.append(char)
        arr_dashes.append('_')
    return


def hangperson():
    i = len(arr_lives)
    if i == 0:
        print('________\n|/ \n|\n| \n| \n| \n| \n|____')
    elif i == 1:
        print('________\n|/   | \n|   (_) \n| \n| \n| \n| \n|____')
    elif i == 2:
        print('________\n|/   | \n|   (_) \n|    | \n|    | \n| \n| \n|____')
    elif i == 3:
        print('________\n|/   | \n|   (_) \n|   /|\ \n|    | \n| \n| \n|____')
    elif i == 4:
        print('________\n|/   | \n|   (_) \n|   /|\ \n|    | \n|   / \ \n| \n|____')
    return


main()


def exit():
    pass
