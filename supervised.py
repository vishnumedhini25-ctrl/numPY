from sklearn.tree import DecisionTreeClassifier

# Training data
X = [[2], [3], [4], [5], [6], [7]]
y = ["Fail", "Fail", "Pass", "Pass", "Pass", "Pass"]

# Create model
model = DecisionTreeClassifier()

# Train the model
model.fit(X, y)

# Predict for a new student
result = model.predict([[3]])

print(result)