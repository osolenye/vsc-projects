import math

def f(x):
    return x + math.log(x)

a = 0.0001
b = 2
eps = 0.001
counter = 0

while abs(b-a)>eps:
    counter += 1
    x0 = (a+b)/2
    if f(x0) * f(a) <= 0:
        b = x0
    elif f(x0) * f(a) > 0:
        a = x0


    print(f'номер итерации: {counter}. нынешнее значение корня: {x0}. приближение к погрешности: {b-a}')

print(f'корень функции: {((a+b)/2)}')    