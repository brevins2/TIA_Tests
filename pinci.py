picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
title = 'PICNIC ITEMS'


def picnic_function():
    print(title.center(17, '-'))
    for item in picnicItems.keys():
        values = str(picnicItems[item])
        key = item
        print(f'{key.ljust(12, ".")}   {values.rjust(4, " ")}')


def picnic_fun2():
    print(title.center(28, '-'))
    for item in picnicItems.keys():
        values = str(picnicItems[item])
        key = item
        print(f'{key.ljust(20, ".")}  {values.rjust(4, " ")}')


picnic_function()
print('\n')
picnic_fun2()
