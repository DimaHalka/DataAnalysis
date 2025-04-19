import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from scipy.cluster.hierarchy import linkage, dendrogram, fcluster

# Artificial data, 3 centers
X, y = make_blobs(n_samples=15, centers=3, cluster_std=1.0, random_state=42)

# Agglomerative clustering, Ward’s method
Z = linkage(X, method='ward')

# Plot the dendrogram
plt.figure(figsize=(10, 5))
dendrogram(Z, labels=np.arange(1, len(X) + 1), leaf_font_size=10)
plt.title("Dendrogram")
plt.xlabel("Objects")
plt.ylabel("Merging distance")
plt.tight_layout()
plt.show()

# Splitting by distance threshold (e.g., 10)
max_d = 10
clusters = fcluster(Z, max_d, criterion='distance')

# Clusers visualization
plt.figure(figsize=(8, 5))
plt.scatter(X[:, 0], X[:, 1], c=clusters, cmap='tab10', s=100, edgecolor='black')
plt.title(f"Agglomerative clustering (cut at height = {max_d})")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.grid(True)
plt.tight_layout()
plt.show()

