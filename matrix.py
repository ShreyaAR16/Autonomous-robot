import numpy as np

# Coefficient matrix
A = np.array([[1, 1, 1], [4, 3, -1], [3, 5, 3]])

# Constant vector
b = np.array([1, 6, 4])

# Number of equations
n = len(b)

# Initialize solution vector
x = np.zeros(n)

for k in range(n-1):
    for i in range(k+1, n):
        factor = A[i,k]/A[k,k]
        b[i] -= factor*b[k]
        for j in range(k+1, n):
            A[i,j] -= factor*A[k,j]

# Back substitution
x[n-1] = b[n-1]/A[n-1,n-1]
for i in range(n-2, -1, -1):
    sum = b[i]
    for j in range(i+1, n):
        sum -= A[i,j]*x[j]
    x[i] = sum/A[i,i]

print(x)

