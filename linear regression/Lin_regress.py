import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

x = np.array([n for n in range(40)])
# y = np.array([n * np.random.randint(10) for n in x])
y = np.array([n + np.random.random(1) * 10 for n in x])

X = x.reshape(-1, 1)

X_train = X[:-20]
X_test = X[-20:]

y_train = y[:-20]
y_test = y[-20:]

model = LinearRegression()
model.fit(X_train,y_train)
y_pred = model.predict(X_test)

print(f'Coefficients: {model.coef_}')
print(f'Mean squared error: {mean_squared_error(y_test, y_pred)}')
print(f'Explained variance score: {r2_score(y_test, y_pred)}')

plt.scatter(X_test, y_test, color='red')
plt.plot(X_test, y_pred, color='blue')
plt.show()