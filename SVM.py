import matplotlib.pyplot as plt
from sklearn.svm import SVC

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

# Create SVM model
model = SVC(kernel="linear")

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

# Plot data
for i in range(len(X)):
    if y[i] == 0:
        plt.scatter(X[i][0], X[i][1])
    else:
        plt.scatter(X[i][0], X[i][1])

# Plot new student
plt.scatter(
    new_student[0][0],
    new_student[0][1],
    marker="*",
    s=250
)

# Get SVM coefficients
w = model.coef_[0]
b = model.intercept_[0]

# Create decision boundary
x_values = [1, 9]

y_values = [
    -(w[0] * x + b) / w[1]
    for x in x_values
]

plt.plot(x_values, y_values)

plt.xlabel("Study Hours")
plt.ylabel("Attendance (%)")
plt.title("SVM Classification")

plt.show()