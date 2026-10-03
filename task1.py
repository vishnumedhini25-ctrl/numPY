import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.cluster import AgglomerativeClustering

# Data
X = np.array([
    [2, 3],
    [3, 4],
    [4, 3],
    [10, 11],
    [11, 12],
    [12, 11]
])

# Create linkage matrix
Z = linkage(X, method="ward")

# Dendrogram
plt.figure(figsize=(8, 5))

dendrogram(Z)

plt.title("Hierarchical Clustering Dendrogram")
plt.xlabel("Data Points")
plt.ylabel("Distance")

plt.show()


# Hierarchical Clustering
model = AgglomerativeClustering(
    n_clusters=2,
    linkage="ward"
)

labels = model.fit_predict(X)

print("Cluster Labels:")
print(labels)


# Visualize clusters
plt.scatter(X[:, 0], X[:, 1], c=labels)

plt.title("Hierarchical Clustering")
plt.xlabel("X")
plt.ylabel("Y")

plt.show()