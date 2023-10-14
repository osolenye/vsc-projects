import math

def matrix():
    return [
    [3, 7, -3],
    [1, -4, 4],
    [1, 1, 0]
]

m = matrix()

free = [33, -8, 4]

def det(m):
    det = (
        m[0][0] * m[1][1] * m[2][2] +
        m[0][1] * m[1][2] * m[2][0] +
        m[0][2] * m[1][0] * m[2][1] -
        m[0][2] * m[1][1] * m[2][0] -
        m[0][0] * m[1][2] * m[2][1] -
        m[0][1] * m[1][0] * m[2][2]
    )
    return det
determinant = det(m)

if determinant != 0:
    x = 0
    xm = m
    for i in range(3):
        xm[i][0] = free[i]
    x = det(xm)
    m = matrix()
    
    y = 0
    ym = m
    for i in range(3):
        ym[i][1] = free[i]
    y = det(ym)
    m = matrix()

    z = 0
    zm = m
    for i in range(3):
        zm[i][2] = free[i]
    z = det(zm)
    m = matrix()
    
    print(f'x = {x}, y = {y}, z = {z}')