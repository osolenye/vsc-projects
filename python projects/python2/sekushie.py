import math

def f(x):
    return x + math.log(x)

x0 = 0.5
x1 = 1.5

e =  0.001 

while abs(x1 - x0) > e:
    da = (f(x1) - f(x0)) / (x1 - x0)
    x2 = x1 - f(x1) / da
    x0, x1 = x1, x2
    print(f"Приближенный корень уравнения: {x2}. Приближение к epsilon: {abs(x1-x0)}" )


root = x2
print(f"Приближенный корень уравнения: {root}.")
