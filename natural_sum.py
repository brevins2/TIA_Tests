num = int(input('Enter number: '))


def find_sum(n):
    i = 1
    total = 0
    while i <= n:
        total = total + i
        i = i + 1
    return total


print(find_sum(num))
