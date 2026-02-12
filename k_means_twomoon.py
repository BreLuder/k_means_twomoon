print("--- SYSTEM CHECK: File is verified ---") # <--- ADD THIS LINE HERE

from k_means_plot import plot_comparison
from k_means_engine import k_means


import numpy as np
import copy
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from sklearn.datasets import make_moons


if __name__ == "__main__":
    print("Initializing data...")
    X, y = make_moons(n_samples=1000, noise=0.1, random_state=42)
    k=2
    max_iterations = 10

    S_initial, initial_centroids, S, final_centroids = k_means(X, k, max_iterations)
    plot_comparison(S_initial, initial_centroids, S, final_centroids, k)

