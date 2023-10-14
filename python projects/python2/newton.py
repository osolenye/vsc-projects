import math

def f(x):
    return x + math.log(x)

def df(x):
    return 1 + 1 / x

# x0 = 0.8
x0 = 2
x = x0 - f(x0)/df(x0)
e = 0.001
counter = 0

while abs(x-x0) > e:
    counter += 1
    x0 = x
    x = x0 - f(x0)/df(x0)

    print(f'номер итерации: {counter}. текущее приближение: {x}. Epsilon: {abs(x-x0)}')
