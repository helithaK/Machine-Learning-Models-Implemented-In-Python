import numpy as np 
from collections import Counter
def euclidean_distance(x1, x2):
    #The below line of code will calculate the 
    #difference of the two numpy arrays
    #then individual elements will be squared
    #next the sum of all the elements in the resultant array will be added up
    #Next squareroot will be taken 
    distance = np.sqrt(np.sum((x1 - x2)**2))
    return distance



class KNN:
    def __init__(self, k = 3):
        self.k = k

    
    def fit(self, X, y):
        self.X_train = X
        self.y_train = y


    
    def predict(self, X):
        predictions = [ self._predict(x) for x in X]
        return predictions

    def _predict(self, x):
        #Compute the distance 
        distances = [euclidean_distance(x,x_train) for x_train in self.X_train]

        #get the closest k
        np.argsort(distances)[:self.k]


        #get the closest k 
        k_indices = np.argsort(distances)[:self.k]
        print(k_indices)
        k_nearest_labels = [self.y_train[i] for i in k_indices]
        print(k_nearest_labels)
        #majority voye
        most_common = Counter(k_nearest_labels).most_common()
        return most_common[0][0]