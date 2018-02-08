import numpy as np

def Gauss(A, b):
    print("Before : ")

    print(A)
    print(b)
    print ("\n")

    n =  len(A)
    if b.size != n:
        raise ValueError("Invalid argument: incompatible sizes between A & b.", b.size, n)
    # k represents the current pivot row. Since GE traverses the matrix in the upper 
    # right triangle, we also use k for indicating the k-th diagonal column index.
    for k in range(n-1):
        #Choose largest pivot element below (and including) k
        maxindex = abs(A[k:,k]).argmax() + k
        if A[maxindex, k] == 0:
            raise ValueError("Matrix is singular.")
        #Swap rows
        if maxindex != k:
            A[[k,maxindex]] = A[[maxindex, k]]
            b[[k,maxindex]] = b[[maxindex, k]]
        for row in range(k+1, n):
            multiplier = A[row][k]/A[k][k]
            #the only one in this column since the rest are zero
            A[row][k] = multiplier
            for col in range(k + 1, n):
                A[row][col] = A[row][col] - multiplier*A[k][col]
            #Equation solution column
            b[row] = b[row] - multiplier*b[k]       
    print(A)
    print(b)
    x = np.zeros(n)
    k = n-1
    x[k] = b[k]/A[k,k]
    while k >= 0:
        x[k] = (b[k] - np.dot(A[k,k+1:],x[k+1:]))/A[k,k]
        k = k-1
    return x

if __name__ == "__main__":
    A = np.array([[0.02,0.01,0,0],[1,2,1,0],[0,1,2,1],[0,0,100,200]])
    b = np.array([[0.02],[1],[4],[800]])
    returnval = Gauss(A,b)
    print("Return value ",returnval)
    print (type(returnval))
