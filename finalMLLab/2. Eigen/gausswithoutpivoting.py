import numpy as np

def Gauss(A, b):
    n =  len(A)
    if b.size != n:
        raise ValueError("Invalid argument: incompatible sizes between A & b.", b.size, n)
    for pivot_row in range(n-1):
        for row in range(pivot_row+1, n):
            multiplier = A[row][pivot_row]/A[pivot_row][pivot_row]
            #the only one in this column since the rest are zero
            A[row][pivot_row] = multiplier
            for col in range(pivot_row + 1, n):
                A[row][col] = A[row][col] - multiplier*A[pivot_row][col]
            #Equation solution column
            b[row] = b[row] - multiplier*b[pivot_row]
    print("REUSLTS AFTER GUASSIAN ELIMINATION")
    print('--------------------------------------')
    print(A)
    print(b)
    x = np.zeros(n)
    k = n-1
    x[k] = b[k]/A[k,k]
    #print 'b value is ',b[k]
    while k >= 0:
        x[k] = (b[k] - np.dot(A[k,k+1:],x[k+1:]))/A[k,k]
        k = k-1
    return x

if __name__ == "__main__":

    A = np.array([[2,-3,-1,2,3],[4,-4,-1,4,11],[2,-5,-2,2,-1],[5,2,1,3,4]])
    b = np.array([[4],[4],[9],[-5]])
    print("-------------------------------------")
    print("Before Gaussian elimination")
    print(A)
    print(b)
    
    print(Gauss(A,b))
