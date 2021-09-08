from numpy import (
    matmul, sin, cos
) 


p = [
    [-1, 2, 5], 
    [10, 12, 5], 
    [4, 7, 2]
]
t = 3.14/2
r = [
    [0, -1, 0], 
    [1, 0, 0], 
    [0, 0, 1]
]

for row in p: print(row)
print (matmul(p,r))