import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier

# X = [Study Hours, Attendance]
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

# Create KNN model
model = KNeighborsClassifier(n_neighbors=3)

# Train the model
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

# Visualization
for i in range(len(X)):
    if y[i] == 0:
        plt.scatter(X[i][0], X[i][1])
    else:
        plt.scatter(X[i][0], X[i][1])

# New student
plt.scatter(
    new_student[0][0],
    new_student[0][1],
    marker="*",
    s=200
)

plt.xlabel("Study Hours")
plt.ylabel("Attendance (%)")
plt.title("KNN Classification")

plt.show()