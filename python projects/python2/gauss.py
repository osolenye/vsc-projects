import math

matrix = [
    [1, -4, 0, 2],
    [7, 3, 8, 6],   
    [6, 7, 8, 4]
]

for i in range(4):
    matrix[1][i] -= matrix[0][i] * 7
for i in range(4):
    matrix[2][i] -= matrix[0][i] * 6
for i in range(4):
    matrix[2][i] -= matrix[1][i]  

def x3(x2):
    return -(1/8)*(8+31*x2)
def x1(x2):
    return 2 + 4*x2

print(f'{matrix[0]}\n{matrix[1]}\n{matrix[2]}')
print('x2 будет равен t. Приравняем ее для примера к 1: ')
x2 = 1
print(f'x3 будет равен: -1/8*(8+31x2). При x2 = 1: {x3(x2)}')
print(f'x1 будет равен 2 + 4*x2. При х2 = 1: {x1(x2)}')
print(f'х2 мы взяли равным: {x2}')
