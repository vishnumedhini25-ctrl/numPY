from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Training data
X = [[500], [1000], [1500], [2000]]
y = [20, 40, 60, 80]

# Create model
model = LinearRegression()

# Train the model
model.fit(X, y)

# Predict
result = model.predict([[2500]])

print("Predicted price:", result)

# Plot original data
plt.scatter(X, y)

# Plot regression line
plt.plot(X, model.predict(X))

# Labels
plt.xlabel("Area (sq.ft)")
plt.ylabel("Price (Lakhs)")
plt.title("Linear Regression")

plt.show()