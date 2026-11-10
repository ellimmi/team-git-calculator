import math

def power(a, b):
    return a ** b

def square_root(a):
    if a < 0:
        raise ValueError("Ошибка: Корень из отрицательного числа!")
    return math.sqrt(a)

def factorial(a):
    if a < 0:
        raise ValueError("Ошибка: Факториал отрицательного числа!")
    return math.factorial(int(a))