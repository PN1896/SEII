import numpy as np
import pandas as pd
from sklearn import model_selection
from sklearn.linear_model import LinearRegression
import pickle

data = pd.read_csv("C:/Git-Test/SEII-1/data/auto-mpg.csv",";")


#print(data.head())
array = data.values
print (array.shape)
# Select 1st column for Y and the rest for X
Y = array[:,0]
X = array[:,1:5]
#print(X)




test_size = 0.33
X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X, Y, test_size=test_size,)
model = LinearRegression()
model.fit(X_train,Y_train)
# save the model to disk
filename = 'finalized_model.sav'
pickle.dump(model, open(filename, 'wb'))
print(model.score(X_test, Y_test))

# some time later...
# load the model from disk
#loaded_model = pickle.load(open(filename, 'rb'))
#result = loaded_model.score(X_test, Y_test)
##print(result)
