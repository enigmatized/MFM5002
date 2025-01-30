import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from math import floor
from scipy.stats import binom, expon, norm, norm, uniform, gamma


def plot_hist_and_cdf(X, Y, N, dist):

# ---- Demonstration 1: Histograms ----
# Y should be ~ Uniform(0,1). Let's check by plotting a histogram.

    plt.figure(figsize=(12, 5))

    plt.subplot(1, 2, 1)
    plt.hist(X, bins=50, density=True, alpha=0.7, color='C0')
    plt.title(f"Histogram of X ({dist})")
    plt.xlabel("X")
    plt.ylabel("Density")

    plt.subplot(1, 2, 2)
    plt.hist(Y, bins=50, density=True, alpha=0.7, color='C1')
    plt.title("Histogram of Y = F_X(X) (Should be Uniform)")
    plt.xlabel("Y")
    plt.ylabel("Density")

    plt.tight_layout()
    plt.show()

    # ---- Demonstration 2: Empirical CDF vs. Theoretical CDF ----
    # We can plot the empirical CDF of Y against the theoretical CDF of a uniform(0,1).

    # Sort Y for empirical CDF
    Y_sorted = np.sort(Y)
    ecdf = np.arange(1, N+1) / N  # empirical CDF values go from 1/N to 1

    # Theoretical CDF for Uniform(0,1) is just the line y = x
    plt.figure(figsize=(6, 5))

    plt.plot(Y_sorted, ecdf, label='Empirical CDF of Y')
    plt.plot([0, 1], [0, 1], 'r--', label='CDF of Uniform(0,1)')

    plt.title("Empirical CDF of Y vs. Uniform(0,1) CDF")
    plt.xlabel("Y (sorted)")
    plt.ylabel("CDF")
    plt.legend()
    plt.show()
