text1 = input('Enter text1: ')
text2 = input('Enter text2: ')


def print_items(txt1, txt2=''):
    for i in txt1:
        print(i)

    print('\n')

    for i in txt2:
        print(i)


print_items(text1)
print_items(text1, text2)
