import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

def plot_comparison(S_initial, centroids_initial, S_final, centroids_final, k):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))
    colors = cm.rainbow(np.linspace(0, 1, k))

    # Initial Configuration
    for i in range(k):
        pts = np.array(S_initial[i])
        if pts.size > 0:
            ax1.scatter(pts[:, 0], pts[:, 1], color=colors[i], alpha=0.5, s=20)
    ax1.scatter(centroids_initial[:, 0], centroids_initial[:, 1],
                color='black', marker='X', s=150, edgecolors='white', label='Initial')
    ax1.set_title(f"Initial Configuration (K={k})")
    ax1.grid(True, linestyle='--', alpha=0.5)

    #Final Configuration
    for i in range(k):
        pts = np.array(S_final[i])
        if pts.size > 0:
            ax2.scatter(pts[:, 0], pts[:, 1], color=colors[i], alpha=0.5, s=20)
    ax2.scatter(centroids_final[:, 0], centroids_final[:, 1],
                color='black', marker='X', s=150, edgecolors='white', label='Final')
    ax2.set_title(f"Final Result (K={k})")
    ax2.grid(True, linestyle='--', alpha=0.5)

    plt.tight_layout()
    plt.show()
    plt.savefig('kmeans_result.png', dpi=300) 
    print("Result saved as 'kmeans_result.png'!")