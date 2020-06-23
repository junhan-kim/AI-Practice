import numpy as np
from matplotlib import pyplot as plt
 
# slope & coefficient init
slope = 0
coef = 0
 
# x,y dataset
# correlation between study time and test scores
data = [[3, 35], [4, 50], [5, 45], [6, 64], [7, 66], [8, 70]]
x = [i[0] for i in data]
y = [i[1] for i in data]
 
# Least Squared Method
def estimate(x, y):
  x = np.array(x)
  y = np.array(y)
  n = np.size(x)
  x_m, y_m = np.mean(x), np.mean(y)
  m = (np.sum(y*x) - n*x_m*y_m) / (np.sum(x*x) - n*x_m*x_m)
  c = y_m - m*x_m
  return (m, c)

# regression function
def predict(x):
   return slope*x + coef

slope, coef = estimate(x, y)
 
# set y_pred list
y_pred = []
for i in range(len(x)):
   y_pred.append(predict(x[i]))
   print("study time=%.f, real score=%.f, prediction score=%.f" % (x[i], y[i], predict(x[i])))

# plotting graph
plt.scatter(x,y)
plt.plot(x,y_pred, color="red")
plt.show()


