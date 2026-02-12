import numpy as np
import copy

def centroid_update(S):
  if len(S) == 0:
      return np.array([0, 0])
  sum_x=0
  sum_y=0
  for point in S:
    sum_x = sum_x + point[0]
    sum_y = sum_y + point[1]
  mean_x = sum_x / len(S)
  mean_y = sum_y / len(S)
  new_centroid = np.array([mean_x, mean_y])
  return new_centroid

def k_means(X, k, max_iterations):
  num_rows = X.shape[0]
  random_indices = np.random.choice(num_rows, size=k, replace=False)
  initial_centroids = X[random_indices]
  current_centroids = initial_centroids
  print(initial_centroids)

  for j in range(max_iterations):
    S = [[] for _ in range(k)]
    for element in X:
        # axis=1 make it compute independently
        distances = np.linalg.norm(current_centroids - element, axis=1)
        closest_index = np.argmin(distances)
        S[closest_index].append(element)
    if j == 0:
        S_initial = copy.deepcopy(S)
    current_centroids = np.zeros((k,2))
    for i in range(k):
      current_centroids[i] = centroid_update(S[i])
  return S_initial,initial_centroids, S, current_centroids
