pi = 3.14
radius = float(input('Enter radius: '))


def compute_area(p, r):
    area = p * r * r
    return area


print(compute_area(pi, radius))
