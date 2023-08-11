number = int(input('Enter number to be checked: '))


def prime_number(num):
    if num / 1 == num and not num == 1:
        for i in range(2, 10):
            if num == 2:
                print('Is a prime number')
                break
            if num % 2 == 0:
                print('Is not a prime number')
                break
            if num % 2 == 1:
                if num % i == 0:
                    print('Is not a prime number')
                    break
                else:
                    print('Is a prime number')
                    break
    else:
        print('one is not inclusive')


prime_number(number)
