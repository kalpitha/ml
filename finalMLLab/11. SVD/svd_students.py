from scipy import linalg
import numpy as np
Data=np.array([[4.9,3.0,1.4,0.2],
	[4.7,3.2,1.3,0.2],
	[4.6,3.1,1.5,0.2],
	[5.0,3.6,1.4,0.2],
	[5.4,3.9,1.7,0.4],
	[4.6,3.4,1.4,0.3],
	[5.0,3.4,1.5,0.2],
	[4.4,2.9,1.4,0.2],
	[4.9,3.1,1.5,0.1],
	[5.4,3.7,1.5,0.2]])

print("The given Matrix is : ")
print(Data,'\n')

[m,n] = Data.shape

print("Rows : ", m,' ',"Columns : ", n , '\n')
#U = Data*Data.T(Data)
#print("Original Matrix is Decomposed into U Sigma and V Transpose as ")
#print(" ")
U, s, V = np.linalg.svd(Data)

print('U : ',U,'\n')
print('Shape of U : ', U.shape, '\n')

print("Eigen values : ")
print(s,'\n')

print('V',V,'\n')
print('Shape of V : ',V.shape, '\n')
#Fill the missing code and print the sizes of U matrix, Sigma matrix and V Tranpose matrix

            





