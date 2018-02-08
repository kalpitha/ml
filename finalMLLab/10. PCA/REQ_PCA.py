from scipy import linalg
import operator
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


print("The given Original Matrix is")

print(Data,'\n')

print("Covariance matrix")
CovData=np.cov(Data.T)
print(CovData,'\n')

print("Eigen values")
eigen = np.linalg.eig(CovData);
eigenValues = eigen[0]
print(eigenValues,'\n')

print("Eigen vectors of the covariance matrix")
eigenVectors = eigen[1]
print(eigenVectors,sep="\n")
print ('\n')
indexes = []
eigenValues = list(enumerate(eigenValues))
sortedEigenValues = sorted(eigenValues, key=operator.itemgetter(1),reverse=True)

print("Components in sorted order")

for i in sortedEigenValues:
    print(eigenVectors[i[0]])

