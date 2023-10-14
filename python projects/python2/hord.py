import math

def f(x):
    return x + math.log(x)

def h(a, b):
    return a - (f(a) / (f(b) - f(a))) * (b-a)


a = 0.01
b = 1
e = 0.001
counter = 0
horda = h(a, b)

while abs(f(horda)) > e:
    b = horda
    horda = h(a, b)
    counter += 1
    print(f'номер итерации: {counter}. приближенное значение: {horda}. Погрешность: {abs(horda)}')




