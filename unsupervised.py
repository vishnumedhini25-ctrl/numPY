from sklearn.cluster import KMeans

# Customer spending data
X = [[1000], [1200], [1500], [8000], [8500], [9000]]

# Create model
model = KMeans(n_clusters=2, random_state=0, n_init=10)

# Train and group the data
model.fit(X)

print(model.labels_)