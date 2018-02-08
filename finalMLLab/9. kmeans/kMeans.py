import random

def k_means(data, k):
	# 1. k initial "means" are randomly selected from the data set.
    if k < len(data):
        initialCentroidPos = []
        while(len(initialCentroidPos) != k):
            # random initial centroids
            pos = random.randint(0,len(data)-1)
            if(pos not in initialCentroidPos):
                initialCentroidPos.append(pos)
        #print(initialCentroid)
        centroids = {}
        change = 1
        for i in initialCentroidPos:
            centroids[data[i]] = []
        iterations = 0
        while(change == 1):
            for i in centroids:
                centroids[i] = []
            for i in data:
                dist = max(data)
                centroid = 0
                for j in centroids:
                    if(abs(i-j) < dist):
                        dist = abs(i-j)
                        centroid = j
                centroids[centroid].append(i)
            temp = {}
            for i in centroids:
                mean = round(sum(centroids[i])/len(centroids[i]),2)
                temp[mean] = centroids[i]
            changedCentroids = temp.keys();
            oldCentroids = centroids.keys();
            change = 0;
            if(sorted(changedCentroids) != sorted(oldCentroids)):
                change = 1
            
            centroids = temp;
            iterations += 1;
        print("clusters ")
        print(centroids,'\n')
        print("Iterations : ",iterations)
        return centroids
    	



if __name__ == '__main__':
	Ages = [15,15,16,19,19,20,20,21,22,28,35,40,41,42,43,44,60,61,65]
	print("Final centroids of clusters : ",list(k_means(Ages, 10)))
