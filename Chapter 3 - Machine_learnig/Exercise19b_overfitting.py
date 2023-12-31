""" Overfitting:  Program that does the classification for some value of k and prints out the training and testing accuracy.
""" 

from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
import numpy as np

# do not edit this
# create fake data
x, y = make_moons(
    n_samples=500,  # the number of observations
    random_state=42,
    noise=0.3
)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=42)

# Define a list of k values to test
k_values = [5]

for k in k_values:
    # Create a classifier and fit it to our data
    knn = KNeighborsClassifier(n_neighbors=k)    
    knn.fit(x_train, y_train)
    
    train_acc = knn.score(x_train, y_train)
    test_acc = knn.score(x_test, y_test)
    
    print("k = %d" % k)
    print("training accuracy: %f" % train_acc)
    print("testing accuracy: %f" % test_acc)
    print()