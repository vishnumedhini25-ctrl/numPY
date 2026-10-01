import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Customer data
# [Age, Income]
X = [
    [20, 20],
    [22, 25],
    [25, 30],
    [27, 28],
    [45, 70],
    [48, 75],
    [50, 80],
    [52, 85],
    [65, 40],
    [68, 45]
]

# Create K-Means model
model = KMeans(n_clusters=3, random_state=42, n_init=10)

# Train the model
model.fit(X)

# Get cluster labels
labels = model.labels_

print("Cluster Labels:")
print(labels)

# Get cluster centers
print("Cluster Centers:")
print(model.cluster_centers_)

# Predict cluster for a new customer
new_customer = [[30, 35]]

prediction = model.predict(new_customer)

print("New Customer Cluster:", prediction)