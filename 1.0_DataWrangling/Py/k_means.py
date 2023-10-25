from sklearn.cluster import KMeans
import numpy as np

# Sample data points
data = np.array([[1, 2], [5, 8], [1.5, 1.8], [8, 8], [1, 0.6]])

# Create KMeans object with 2 clusters
kmeans = KMeans(n_clusters=2)

# Fit the data to the KMeans algorithm
kmeans.fit(data)

# Get cluster labels and centroids
labels = kmeans.labels_
centroids = kmeans.cluster_centers_

print("Cluster Labels:", labels)
print("Centroids:", centroids)