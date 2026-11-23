
from sklearn.linear_model import LinearRegression
import sklearn
scikit-learn

model = LinearRegression()
model.fit(X, y)
predictions = model.predict(X_test)
