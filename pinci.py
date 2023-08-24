picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
title = 'PICNIC ITEMS'


def picnic_function(titleextensions, itemExtensions, valueExtensions):
    print(title.center(titleextensions, '-'))
    for item in picnicItems.keys():
        print(f'{item.ljust(itemExtensions, ".")}   {str(picnicItems[item]).rjust(valueExtensions, " ")}')


picnic_function(17, 12, 4)
print('\n')
picnic_function(28, 20, 4)
