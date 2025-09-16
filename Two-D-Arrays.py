# ************* Transpose and 90 degree Rotate Matrix *************

arr = [[1,2,3],[4,5,6],[7,8,9]]

# with external variable
res = [[0 for _ in range(len(arr))] for _ in range(len(arr[0]))]

for r in range(len(arr)):
    for c in range(len(arr[0])):
        res[r][c] = arr[c][r] # Transpose
    res[r] = res[r][::-1] # Rotate Array

print(res)

#without

for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        arr[i][j], arr[j][i] = arr[j][i], arr[i][j] # Transpose
    
for i in range(len(arr)):
    arr[i] = arr[i][::-1]  # Rotate Array

print(arr)

# ************* Spiral Matrix *************

a= [[1,  2,  3,  4],
    [5,  6,  7,  8],
    [9,  10, 11, 12],
    [13, 14, 15, 16]]
    

res = []

top = 0 
bottom = len(a) -1

left = 0 
right = len(a[0])-1

while left<=right and top<=right:
    
    for r in range(left,right+1):
        res.append(a[top][r])
    top+=1
    
    for c in range(top,bottom+1):
        res.append(a[c][right])
    right-=1
    
    for r in range(right, left-1, -1):
        res.append(a[bottom][r])
    bottom-=1 
    
    for c in range(bottom, top-1, -1):
        res.append(a[c][left])
    left+=1
        

print(res)
    
# *************  Set Matrix Zeros *************

arr = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]

rows, cols = set(), set()

for r in range(len(arr)):
    for c in range(len(arr[r])):
        if arr[r][c] == 0:
            rows.add(r)
            cols.add(c)

for r in range(len(arr)):
    for c in range(len(arr[r])):
        if r in rows or c in cols:
            arr[r][c] = 0

print(arr)

# *************  Matrix Multiplication *************

import numpy as np 

a = [[1, 2], [3, 4]]
b = [[5, 6], [7, 8]]

m = np.dot(a,b)

print(m)