import numpy as np
import pandas as pd
import sklearn
from sklearn import datasets
from sklearn.model_selection import train_test_split

class LogisticRegression:
    _learning_rate = 0.01
    _max_iterations = 100000
    _threshold = 0.01

    def add_intercept(self, x_data):   # add intercept
        intercept = np.ones((x_data.shape[0], 1))
        return np.concatenate((intercept, x_data), axis=1)

    def sigmoid(self, z):  # sigmoid function
        return 1 / (1 + np.exp(-z))

    def cost(self, h, y):  # cost function
        return (-y * np.log(h) - (1 - y) * np.log(1 - h)).mean()

    def fit(self, x_data, y_data):  # train datasets
        num_examples, num_features = np.shape(x_data)

        x_data = self.add_intercept(x_data)
        self._W = np.zeros(x_data.shape[1])   # weights initialization

        for i in range(100000):  # loop for 100000
            z = np.dot(x_data, self._W)  # matrix multiplication
            hypothesis = self.sigmoid(z)

            diff = hypothesis - y_data  # diff between y_data and hypothesis
            cost = self.cost(hypothesis, y_data)

            # partial derivative of cost function : transposed x * diff / n
            gradient = np.dot(x_data.transpose(), diff) / num_examples
            self._W -= 0.01 * gradient   # update theta (learning rate : 0.01)

            # stop learning when the threshold is reached
            if cost < self._threshold:
                return False
            # print cost every 100 iter
            if (i % 1000 == 0):
                print('cost :', cost)

    def predict_prob(self, x_data):
        x_data = self.add_intercept(x_data)
        return self.sigmoid(np.dot(x_data, self._W))

    def predict(self, x_data):  # predict test datasets
        return self.predict_prob(x_data).round()


wine_data = pd.read_csv('winequality-white.csv',delimiter=';',dtype=float)
print(wine_data.head(10))

x_data = wine_data.iloc[:,0:-1]
y_data = wine_data.iloc[:,-1]

y_data = np.array([1 if i>=7 else 0 for i in y_data])
x_data.head(5)

train_x, test_x, train_y, test_y = sklearn.model_selection.train_test_split(x_data, y_data, test_size = 0.3,random_state=42)

lr = LogisticRegression()
lr.fit(train_x, train_y)
print('train completed')

y_pred = lr.predict(test_x)
print("Test Data",sum(y_pred == test_y) / len(test_y))