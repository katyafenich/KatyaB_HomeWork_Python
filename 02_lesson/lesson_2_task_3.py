import math

def square(side):
    return math.ceil(side ** 2)

num_side =float(input("Введите введите длину стороны: "))
print(f"Площадь квадрата: {square(num_side)}")