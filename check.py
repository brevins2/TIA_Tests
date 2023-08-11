marks = input('Enter your marks: ')


def checkmarks(mark):
    if mark >= 70:
        print('Pass')
    else:
        print('Fail')


checkmarks(int(marks))
