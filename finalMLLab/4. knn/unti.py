import csv
import random
import operator
import numpy
def dataload(file,split,train=[],test=[]):
    with open(file,'r') as csvfile:
        lines=csv.reader(csvfile)
        data=list(lines)
        for x in range(len(data)-1):
            for y in range(4):
                data[x][y]=float(data[x][y])
            # introducing randomness here
            if(random.random()<split):
                train.append(data[x])
            else:
                test.append(data[x])
'''
trainingSet=[]
testSet=[]
dataload('IRIS.csv', 0.66, trainingSet, testSet) #0.66 is the split
print('Length of Training after dataload : ',len(trainingSet))
print('Length of Testing after dataload : ',len(testSet))'''

#Calculating Euclidean diastance

#this is Euclidean distance
'''
def Edistance(x,y,z):
    
	val=0.0
	n = 2
	for i in range(z):
		val += (float(y[i])-float(x[i]))**n
	return numpy.power(val,1.0/n)
#for n = 2 the Accuracy is 95.45
'''

#this is Manhattan Distance
'''
def Edistance(x,y,z):
    val=0.0
    for i in range(z):
        val += abs(float(y[i])-float(x[i]))
    return val
#the Accurancy is 39.285
'''

#this is minkowski Distance
def Edistance(x,y,z):
    val = 0.0
    n = 2
    for i in range(z):
        val += (float(y[i])-float(x[i]))
    return numpy.power(numpy.power(val,n),1.0/n)
#the Accuracy is 75.7575


#Checking this function
'''
x1 = [2, 2, 2]
x2 = [4, 4, 4]
distance = Edistance(x1, x2, 3)
print("Eucledian distance ",distance,"\n")'''

#Returning K nearest neighbours based on distance
def Neighbors(train, test, k):
    distances = []
    length = len(test)-1
    for x in range(len(train)):
        dist = Edistance(test, train[x], length)
        distances.append((train[x], dist))
    distances.sort(key=operator.itemgetter(1))
    neighbors = []
    for x in range(k):
        neighbors.append(distances[x][0])
    return neighbors

#Checking this function
train = [[2, 2, 2,'a'], [4, 4, 4,'b']]
test = [5, 5, 5]
k = 2
#print(Neighbors(train, test, 1))

#Voting the classes obtained from Neighbours
def Response(neighbors):
	Votes = {}
	for x in range(len(neighbors)):
		response = neighbors[x][-1]
		if response in Votes:
			Votes[response] += 1
		else:
			Votes[response] = 1
	sortedVotes = sorted(Votes.items(), key=operator.itemgetter(1), reverse=True)
	return sortedVotes[0][0]

#Checking response
'''
neighbors = [[1,1,1,'a'], [2,2,2,'a'], [3,3,3,'b']]
response = Response(neighbors)
print("Response : ", response,'\n')'''

#Calculating Accuracy
def Accuracy(testSet, predictions):
	correct = 0
	for x in range(len(testSet)):
		if testSet[x][-1] == predictions[x]:
			correct += 1
	return (correct/float(len(testSet))) * 100.0

#Checking accuracy
'''
testSet = [[1,1,1,'a'], [2,2,2,'a'], [3,3,3,'b']]
predictions = ['a', 'a', 'a']
accuracy = Accuracy(testSet, predictions)
print("Accuracy : ",accuracy,'\n')'''

#Combining all functions to get KNN

trainingSet=[]
test=[]
split = 0.67
dataload('IRIS.csv', split, trainingSet, test)
print('Length of Training set after dataload : ',len(trainingSet))
print('Length of Testing set after dataload : ',len(test))
predictions=[]
k = 3
for x in range(len(test)):
	neighbors = Neighbors(trainingSet, test[x], k)
	result = Response(neighbors)
	predictions.append(result)
	print('Predicted = ',result,', Actual = ',test[x][-1])
accuracy =Accuracy(test, predictions)
print("Accuracy  ",accuracy,'\n')
