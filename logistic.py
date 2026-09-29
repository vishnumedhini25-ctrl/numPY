import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

# Input data - Study Hours
X = [[1], [2], [3], [4], [5], [6], [7], [8]]

# Output - Fail = 0, Pass = 1
y = [0, 0, 0, 1, 1, 1, 1, 1]

# Create and train model
model = LogisticRegression()
model.fit(X, y)

# Prediction values for smooth curve
X_test = [[i / 10] for i in range(10, 81)]

# Probability of Pass
y_probability = model.predict_proba(X_test)[:, 1]

# Plot original data
plt.scatter(X, y)

# Plot Logistic Regression curve
plt.plot(X_test, y_probability)

# Labels
plt.xlabel("Study Hours")
plt.ylabel("Probability of Pass")
plt.title("Logistic Regression")

plt.show()