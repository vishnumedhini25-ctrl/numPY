import matplotlib.pyplot as plt

from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import plot_tree

# Input data
# [Study Hours, Attendance]
X = [
    [1, 50],
    [2, 55],
    [2, 60],
    [3, 65],
    [4, 70],
    [5, 75],
    [6, 80],
    [7, 85],
    [8, 90],
    [9, 95]
]

# 0 = Fail, 1 = Pass
y = [0, 0, 0, 0, 1, 1, 1, 1, 1, 1]

# Create Decision Tree
model = DecisionTreeClassifier(max_depth=3, random_state=42)

# Train
model.fit(X, y)

# New student
new_student = [[5, 78]]

# Prediction
prediction = model.predict(new_student)

print("Prediction:", prediction)

if prediction[0] == 1:
    print("Result: Pass")
else:
    print("Result: Fail")

# Visualize Decision Tree
plt.figure(figsize=(12, 7))

plot_tree(
    model,
    feature_names=["Study Hours", "Attendance"],
    class_names=["Fail", "Pass"],
    filled=True
)

plt.title("Decision Tree")
plt.show()